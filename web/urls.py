import profile

from django.urls import path

from web.views import profile_view, RegisterView

app_name = 'profile'

urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('register', RegisterView.as_view(), name="register")
]
