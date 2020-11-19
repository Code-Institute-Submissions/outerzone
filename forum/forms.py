from django import forms
from .models import UserProfile


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
