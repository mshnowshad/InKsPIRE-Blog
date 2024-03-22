
from django import forms
from .models import PostModel

#signup 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		

	#helptext removed
	def __init__(self, *args, **kwargs):
		super(SignUpForm,self).__init__(*args, **kwargs)
		
		for fieldname in ['username','email','password1','password2']:
			self.fields[fieldname].help_text = None
		
	






# add post
class PostModelForm(forms.ModelForm):

	description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
	class Meta:
		model = PostModel
		fields = ('title','description','category','image')