from django.urls import path
from .views import user_profile

urlpatterns = [
    path(r'^user/(?P<username>[a-zA-Z]+)/$', user_profile),
]
    