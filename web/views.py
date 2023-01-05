from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, FormView

from web.forms import Buyer, RegisterForm


@login_required
def profile_view(request):
    return render(request, 'web/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)