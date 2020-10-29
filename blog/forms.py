#forms.py
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',) 
		#we want only title & text exposed. 
		#author is person who is currently logged in
		# Created_date should be automatically set when we create a post(in code)