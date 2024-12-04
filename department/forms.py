from django import forms
from .models import Teacher
from django.contrib.auth import get_user_model


User = get_user_model()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'name',
            'position',
            'image',
            'full_time',
            'additional_work',
            'audience',
            'courses'
        ]
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
