# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .forms import PersonalInfoForm, PasswordForm, ProfileForm, ConsentForm

User = get_user_model()

def registration_step1(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            request.session['step1_data'] = form.cleaned_data
            return redirect('registration_step2')
    else:
        form = PersonalInfoForm()
    
    return render(request, 'registration/personal_info.html', {'form': form, 'step': 1})

def registration_step2(request):
    if 'step1_data' not in request.session:
        return redirect('registration_step1')
    
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            request.session['step2_data'] = form.cleaned_data
            return redirect('registration_step3')
    else:
        form = PasswordForm()
    
    return render(request, 'registration/password_form.html', {'form': form, 'step': 2})

def registration_step3(request):
    if 'step1_data' not in request.session or 'step2_data' not in request.session:
        return redirect('registration_step1')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                file_name = default_storage.save(f'temp/{profile_picture.name}', ContentFile(profile_picture.read()))
                request.session['profile_picture_path'] = file_name
            else:
                request.session['profile_picture_path'] = None
            return redirect('registration_step4')
    else:
        form = ProfileForm()
    
    return render(request, 'registration/profile_form.html', {'form': form, 'step': 3})

def registration_step4(request):
    if not all(key in request.session for key in ['step1_data', 'step2_data']):
        return redirect('registration_step1')
    
    if request.method == 'POST':
        form = ConsentForm(request.POST)
        if form.is_valid():
            # Create user with all collected data
            step1_data = request.session['step1_data']
            step2_data = request.session['step2_data']
            
            user = User.objects.create_user(
                username=step1_data['username'],
                email=step1_data['email'],
                phone=step1_data['phone'],
                address=step1_data['address'],
                password=step2_data['password1'],
                terms_accepted=form.cleaned_data['terms_accepted']
            )
            
            profile_picture_path = request.session.get('profile_picture_path')
            if profile_picture_path and default_storage.exists(profile_picture_path):
                with default_storage.open(profile_picture_path, 'rb') as temp_file:
                    permanent_name = f'profiles/{user.id}_{os.path.basename(profile_picture_path)}'
                    user.profile_picture.save(permanent_name, ContentFile(temp_file.read()))
                default_storage.delete(profile_picture_path)
            
            for key in ['step1_data', 'step2_data', 'profile_picture_path']:
                request.session.pop(key, None)
            
            messages.success(request, 'Registration completed successfully!')
            return redirect('registration_success', user_id=user.id)
    else:
        form = ConsentForm()
    
    return render(request, 'registration/consent_form.html', {'form': form, 'step': 4})

def registration_success(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return render(request, 'registration/success.html', {'user': user})
    except User.DoesNotExist:
        return redirect('registration_step1')

@require_GET
def check_email_unique(request):
    email = request.GET.get('email', '')
    if email:
        exists = User.objects.filter(email=email).exists()
        return JsonResponse({'unique': not exists})
    return JsonResponse({'unique': True})