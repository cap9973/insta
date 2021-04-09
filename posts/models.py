from django.db import models
from django.utils.translation import gettext_lazy as _
from core import models as core_models


class PostModel(core_models.HistoryModel):
    user_id = models.ForeignKey('users.User',related_name='post_model', on_delete=models.CASCADE)
    content = models.TextField(_('내용'), max_length=200)
    images = models.ImageField(upload_to='files', blank=True, null=True)
    like=models.ManyToManyField('users.User', related_name='likes', blank=True)


    class Meta:
        db_table = 'posts_to'
        verbose_name = _('게시글')
        verbose_name_plural = _('게시글')


    def __str__(self):
        return self.content




