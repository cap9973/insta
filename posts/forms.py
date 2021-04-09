from django import forms
from . import models
from users.models import models as user_model


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ('content', 'images',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = models.PostModel
        fields = ('content', 'images')
