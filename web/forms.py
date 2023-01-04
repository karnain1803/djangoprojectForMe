from django.contrib.auth.forms import UserCreationForm


class Buyer:
    pass


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer
