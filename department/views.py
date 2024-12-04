from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm, UserEditForm
from django.contrib.auth.models import User


def index(request):
    teachers = Teacher.objects.all()
    paginator = Paginator(teachers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'department/index.html', context)


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'department/detail.html', context)


def course_detail(request, course_slug):
    course = get_object_or_404(Course, id=course_slug)
    teachers = Teacher.objects.filter(courses=course).order_by('name')
    context = {
        'course': course,
        'teachers': teachers
    }
    return render(request, 'department/course.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('department:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request,
                  'registration/registration_form.html',
                  context)


@login_required
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('department:index')
    else:
        form = TeacherForm()
    context = {
        'form': form
    }
    return render(request, 'department/create.html', context)


@login_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('department:teacher_detail',
                            teacher_id=teacher_id)
    else:
        form = TeacherForm(instance=teacher)
    context = {
        'form': form
    }
    return render(request, 'department/create.html', context)


@login_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('department:index')
    context = {
        'teacher': teacher
    }
    return render(request, 'department/create.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': request.user,
        'profile': user,
    }
    return render(request, 'department/profile.html', context)


@login_required
def edit_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('department:profile',
                            username=request.user.username)
    else:
        form = UserEditForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'department/user.html', context)
