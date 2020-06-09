"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

#개별적인 뷰는 각 어플에서 처리하도록 주석처리
#from bookmark.views import BookmarkLV, BookmarkDV
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    #bookmark 앱의 url은 bookmark/url.py에서 정의
    path('bookmark/', include('bookmark.urls')),
    # board 앱의 url은 board/urls.py에서 정의
    path('board/', include('board.urls')),

    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',UserCreateView.as_view(),name='register'),
    path('accounts/register/done/',UserCreateDoneTV.as_view(),name='register_done'),

    #path('',HomeView.as_view(), name='home'),

    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]


