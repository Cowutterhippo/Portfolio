from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from blog.models import Post

# class LoginForm(AuthenticationForm):
# 	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name':'username'}))
# 	password = forms.CharField(label="password", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name':'passwprd'}))

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'category', 'is_public', 'content']

# class LoginForm(ModelForm):
