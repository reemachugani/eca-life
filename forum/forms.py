from django.forms import ModelForm, Textarea
from forum.models import Post, Forum

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['created', 'creator', 'thread']
        widgets = {
			'body': Textarea(attrs={'cols':68, 'rows': 25},),
		}

class CommentForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={'cols':78, 'rows': 5},),
        }

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ('title','description',)
        widgets = {
            'description': Textarea(attrs={'cols':68, 'rows': 5},),
        }