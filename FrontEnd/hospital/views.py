from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomLoginForm, AdminCreateUserForm 
from django.views import View

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

class createUserView(View):
    def get(self, request):
        form = AdminCreateUserForm()
        return render(request, 'admin_create_user.html', {'form': form})
    
    def post(self, request):
        form = AdminCreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrator')
        return render(request, 'admin_create_user.html', {'form': form})
    
