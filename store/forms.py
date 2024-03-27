
from dataclasses import fields
from django import forms
from .models import PostModel

#update Informations of an user
from .models import ProfileModel

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
		





#update Informations of an user

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email']
		
	def __init__(self, *args, **kwargs):
		super(UserUpdateForm,self).__init__(*args, **kwargs)
		
		for fieldname in ['username','email']:
			self.fields[fieldname].help_text = None
		

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['image']









