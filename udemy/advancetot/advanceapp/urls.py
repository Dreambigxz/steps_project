
from django.urls import path


from . import views



urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('student_list/', views.Student_list_view.as_view(), name='list'),
    path('<int:pk>/school_detail/', views.Student_detail_view.as_view(), name='detail'),

    #CRUD
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.SchoolUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='delete'),

    #####function base view####
    path('school/', views.index, name='school'),
    path('register/', views.schoolForm, name='register'),
    path('<int:question_id>/students/', views.student, name='student'),
]