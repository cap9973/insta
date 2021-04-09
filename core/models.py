from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class HistoryModel(models.Model):
    created_at = models.DateTimeField(
        _('생성일'),
        auto_now_add=True,
        editable=False,
        blank=True,
        help_text=_(
            '데이터가 생성된 일자입니다.'
        ),
    )
    updated_at = models.DateTimeField(
        _('수정일'),
        auto_now=True,
        editable=False,
        blank=True,
        null=True,
        help_text=_(
            '데이터가 수정된 사용자입니다.'
        ),
    )
    class Meta:
        abstract=True


