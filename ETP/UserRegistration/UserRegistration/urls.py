"""
URL configuration for UserRegistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.views import (
    registration_step1, registration_step2, registration_step3, 
    registration_step4, registration_success, check_email_unique
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration_step1, name='registration_step1'),
    path('step2/', registration_step2, name='registration_step2'),
    path('step3/', registration_step3, name='registration_step3'),
    path('step4/', registration_step4, name='registration_step4'),
    path('success/<int:user_id>/', registration_success, name='registration_success'),
    path('check-email/', check_email_unique, name='check_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
