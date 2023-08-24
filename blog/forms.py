from django import forms
from . models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'f_image', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]