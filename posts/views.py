from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PostModel
from .forms import PostCreateForm, PostUpdateForm
from reviews.models import ReviewModel
import json


class PostList(ListView):
    template_name = 'post/post_list.html'
    model = PostModel
    context_object_name = 'target'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['review_post']=ReviewModel.objects.all()
        context['post_count']=PostModel.objects.all().count()
        return context


class PostCreate(CreateView):
    template_name = 'post/post_create.html'
    model = PostModel
    success_url = reverse_lazy('posts:_post')
    form_class = PostCreateForm
    context_object_name = 'post_create'

    def form_valid(self, form):
        comment=form.save(commit=False)
        comment.images =form.cleaned_data.get('images')
        comment.content=form.cleaned_data.get('content')
        comment.user_id=self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:_post')


class PostUpdateView(UpdateView):
    model=PostModel
    template_name = 'post/post_update.html'
    form_class =PostUpdateForm
    success_url = reverse_lazy('posts:_post')


class PostDeleteView(DeleteView):
    model=PostModel
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('posts:_post')


def likes(request):
    if request.is_ajax():
        post_id=request.GET['blog_id']
        post=PostModel.objects.get(id=post_id)


        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인일때
            message='로그인을 해주세요'
            context={'like_count':post.like.count(), 'message':message }
            return HttpResponse(json.dumps(context), content_type='application/json')

        user=request.user
        if post.like.filter(id=user.id).exists(): #이미 좋아요를 누른 유저일 때
            post.like.remove(user) #like field에 현재 유저 삭제
            message='좋아요 취소'
        else:
            post.like.add(user)
            message='좋아요'
        context={'like_count':post.like.count(), 'message':message}

        return HttpResponse(json.dumps(context), content_type='application/json')






