from django import forms
from . import models

class ReviewCreateForm(forms.ModelForm):

    class Meta:
        model = models.ReviewModel
        fields = ('review_content',)


class ReviewUpdateForm(forms.ModelForm):

    class Meta:
        model =models.ReviewModel
        fields = ('review_content', 'post_content',)







