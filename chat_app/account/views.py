from django.shortcuts import redirect, render
from account.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, f"You have successfully signed up.")
            return redirect('chat:index')
    form = RegisterForm()
    return render(request, 'account/auth-register.html', {'form':form})


class CustomLoginView(LoginView):
    template_name = 'account/auth-login.html'
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        messages.success(self.request, "You have successfully logged in.") # Add your custom success message here
        return super().form_valid(form)