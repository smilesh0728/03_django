from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text="슬러그 헬프")
    description = models.CharField('description', max_length=100)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('Create Date', auto_now_add=True)
    modify_dt = models.DateTimeField('Modify Date', auto_now=True)
    # 사용자를 foreignkey로 할당하기 위한 field 생성
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager(blank=True)

    # Post를 출력할 때, 타이틀을 보여줌
    def __str__(self):
        return self.title
    # 절대 주소 출력
    def get_absolute_url(self):
        return reverse('board:post_detail', args=(self.slug,))

    # 이전 페이지
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    # 다음 페이지
    def get_next(self):
        return self.get_next_by_modify_dt()

    # 저장 시,  slug 자동 생성을 위한 메소드 (저장할 때 타이틀값 받아 만들어서 넣어준다는 뜻)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)