from django.contrib.auth.forms import UserCreationForm
from main.models import Buyer


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer
