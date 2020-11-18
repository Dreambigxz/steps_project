from django.urls import path

from . import views

urlpatterns= [

    path('', views.BaseView.as_view(), name='home'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.CreatePost.as_view(), name='newPost'),
    path('<int:pk>/edit/', views.EditPost.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
    path('draft/', views.DraftListView.as_view(), name='draft'),
    path('<int:pk>/comment/', views.create_comment, name='comment'),
    path('<int:pk>/approvecomment/', views.comment_approve, name='approve_comment'),
    path('<int:pk>/removecomment/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
]