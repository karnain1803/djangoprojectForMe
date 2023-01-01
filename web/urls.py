import profile

from django.urls import path

from taskmanager.web.views import profile_view
app_name = 'profile'

urlpatterns = [
    path('profile/', profile_view, name="profile")
]
