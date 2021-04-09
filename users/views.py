from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignUpForm

class UserLoginView(LoginView):

    template_name = 'users/login.html'
    # success_url = reverse_lazy('posts:_post')

    def form_valid(self, form):
        self.request.session['email']=form.cleaned_data.get('email')

        return super().form_valid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('posts:_post')





class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('posts:_post')
    # initial = {
    #     'username': 'jesse94@yahoo.com',
    #     'email': 'jesse94@yahoo.com',
    # }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)
