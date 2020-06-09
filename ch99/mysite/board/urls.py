from django.urls import path, re_path
from board import views

app_name = 'board'
urlpatterns = [
    # /board/

    path('', views.PostLV.as_view(), name ='index'),

    # /board/제목-슬러그-주소 (\w )
    re_path(r'^board(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name = 'post_detail'),
    path('search/', views.SearchFormView.as_view(), name="search"),

    # 생성: http://127.0.0.1:8000/board/add/
    path('add/', views.PostCreateView.as_view(), name="add",),

    # 수정: http://127.0.0.1:8000/board/1/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update",),

    # 삭제: http://127.0.0.1:8000/board/1/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete",),


    # tag 관련 추가
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]

