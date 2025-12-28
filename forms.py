from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '标题', 'text': '内容'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}