from django.shortcuts import redirect, render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy 

class CustomLoginForm(AuthenticationForm):
    type = forms.ChoiceField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('fdo', 'Front Desk'), ('deo', 'Data Entry')])

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('afterlogin')
    authentication_form = CustomLoginForm

    def get_success_url(self):
        print(self.success_url)
        return self.success_url

# Create your views here.
def home_view(request):
    return render(request, "index.html")


def afterlogin_view(request):
    if request.method == "POST":
        print(request.POST['username'])
    return redirect('home')