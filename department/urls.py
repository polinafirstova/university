from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/<int:teacher_id>/',
         views.teacher_detail,
         name='teacher_detail'),
    path('teachers/create/',
         views.create_teacher,
         name='create_teacher'),
    path('teachers/<int:teacher_id>/edit/',
         views.edit_teacher,
         name='edit_teacher'),
    path('teachers/<int:teacher_id>/delete/',
         views.delete_teacher,
         name='delete_teacher'),
    path('courses/<slug:course_slug>/',
         views.course_detail,
         name='course_detail'),
    path('auth/registration/', views.registration, name='registration'),
    path('auth/password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change_form.html'
         ),
         name='password_change'),
    path('auth/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'
         ),
         name='password_change_done'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
