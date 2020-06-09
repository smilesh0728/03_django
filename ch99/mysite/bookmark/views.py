from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# 1)bookmark_list.html 파일로 자동으로 연결
# 2)html 파일로 object_list를 넘겨 줌
# listview 상속
class BookmarkLV(ListView):
    model = Bookmark
    #참고 LV=listview

#1) bookmark_detail.html 파일로 자동으로 연결
#2) html 파일로 object를 넘겨줌

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')