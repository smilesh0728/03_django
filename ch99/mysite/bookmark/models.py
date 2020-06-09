from django.db import models
# 추가
from django.contrib.auth.models import User


# Create your models here.
#모델지정
class Bookmark(models.Model):
    # 타이틀 필드
    title = models.CharField('TITLE', max_length=100, blank=True)
    #URL필드
    url = models. URLField('URL', unique=True)

    # 사용자를 foreignkey로 할당하기 위한 field 생성
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        # return "%s %s" %(self.title,"가나다가")
        return self.title


