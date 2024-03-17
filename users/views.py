from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.





def signin(request):
	return render(request,'users/signin.html')





def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')


	else:
		form = UserCreationForm()
	return render(request,'users/signup.html',{'form':form})