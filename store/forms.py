from django import forms
from .models import PostModel

class PostModelForm(forms.ModelForm):

	description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	class Meta:
		model = PostModel
		fields = ('title','description','category','image')