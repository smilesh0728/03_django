from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from board.models import Post
from django.views.generic import FormView
from board.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
# 댓글

from django.conf import settings

# Create your views here.

# ListView 상속
class PostLV(ListView):
    model = Post

    # 1) post_list.html을 자동으로 참조 -> post_all.html 지정
    template_name = 'board/post_all.html'

    # 2) object_list를 post_all.html에 전달 -> posts를 전달
    context_object_name = 'posts'
    paginate_by = 2

# DetailView 상속
# 1) post_detail.html을 자동으로 참조
# 2) object를 post_detail.html에 전달
class PostDV(DetailView):
    model = Post

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'board/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'content']
    # fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('board:index')


class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('board:index')

#Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model= Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

class PostDV(DetailView):
    model = Post

    # 댓글 관련 메소드 추가
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context