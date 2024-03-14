from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import PostModel
from django.contrib import messages

def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                print("Authenticated user:", request.user)  # Debug statement
                instance.author = request.user
                instance.save()
                messages.success(request, 'Post added successfully')
                return redirect('home')
            else:
                print("User is not authenticated")  # Debug statement
    else:
        form = PostModelForm()

    return render(request, 'store/add-post.html', {'form': form})


def home(request):
	posts = PostModel.objects.all()
	
	return render(request,'store/index.html',{'posts':posts})


def about(request):
	return render(request,'store/about.html')

def blog(request):
	posts = PostModel.objects.all()
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
