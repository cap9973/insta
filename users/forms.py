from django import forms
from . import models


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "패스워드"}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "패스워드 확인"}))

    class Meta:
        model = models.User
        fields = ['username', 'email', 'password', 'password1', ]




    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "해당 이메일은 이미 사용 중입니다..", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.data.get('password1')
        if password != password1:
            raise forms.ValidationError(f"{password}, {password1}패스워드가 일치하지 않습니다")

        else:
            return password

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data('password')
        user = models.User.objects.create_user(email, username, password)
        user.save()

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user.email = email
        user.set_password(password)
        user.save()
