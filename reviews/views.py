from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from .models import ReviewModel
from .forms import ReviewCreateForm
from posts import models as post_models

class PostCreateReView(CreateView):
    template_name ='review/create_review.html'
    model = ReviewModel
    # success_url = reverse_lazy('post:_post')
    form_class = ReviewCreateForm


    def form_valid(self, form):
        connet=form.save(commit=False)
        connet.review_content =form.cleaned_data.get('review_content')
        post=post_models.PostModel.objects.get(pk=self.kwargs['pk'])
        connet.post_content=post
        connet.user_id=self.request.user
        connet.save()
        return super().form_valid(form)


    def get_success_url(self):

        return reverse_lazy('posts:_post')


class PostDeleteReview(DeleteView):
    model = ReviewModel
    template_name = 'review/delete_review.html'
    success_url = reverse_lazy('posts:_post')


class ReViewList(ListView):
    template_name = 'review/review_list.html'
    model = ReviewModel



    def get_context_data(self, **kwargs):
        context = super(ReViewList, self).get_context_data(**kwargs)
        # context['post_post']=ReviewModel.objects.get(id=self.kwargs['pk'])
        context['post']=self.kwargs['pk']

        return context



class ReViewContentList(ListView):
    template_name = 'review/review_contentlist.html'
    model = ReviewModel



    def get_context_data(self, **kwargs):
        context = super(ReViewContentList, self).get_context_data(**kwargs)
        context['post_post']=ReViewContentList.objects.all()
        return context


