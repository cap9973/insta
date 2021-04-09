from django.db import models
from django.utils.translation import gettext_lazy as _
from core import models as core_models
# Create your models here.



class ReviewModel(core_models.HistoryModel):
    review_content = models.CharField(_('댓글'),  max_length=120)
    post_content=models.ForeignKey('posts.PostModel', related_name='review_model', on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', related_name='review_model', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews_to'
        verbose_name = _('댓글')
        verbose_name_plural = _('댓글')

    def __str__(self):
        return str(self.review_content)
