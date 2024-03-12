
from django.shortcuts import render
from.models import Post


# Create your views here.



def home(request):
	posts = Post.objects.all()
	return render(request,'store/index.html',{'posts':posts})


def about(request):
	return render(request,'store/about.html')

def blog(request):
	posts = Post.objects.all()
	return render(request,'store/blog.html',{'posts':posts})


def contact(request):
	return render(request,'store/contact.html')





def service(request):
	return render(request,'store/services.html')





def signin(request):
	return render(request,'store/signin.html')





def signup(request):
	return render(request,'store/signup.html')





# def contact(request):
# 	return render(request,'store/contact.html')




# def contact(request):
# 	return render(request,'store/contact.html')




# def contact(request):
# 	return render(request,'store/contact.html')
