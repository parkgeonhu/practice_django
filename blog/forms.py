from django import forms

from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number',)