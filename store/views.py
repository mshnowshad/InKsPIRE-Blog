import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import PostModel, Category


from .forms import PostModelForm
from django.contrib.auth.models import User  # Import the User model


#signup
from .forms import SignUpForm
from django.contrib.auth import authenticate, login,logout




def sign_in(request):
	return render(request,'users/signin.html')


#signup
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered successfully!")
            return redirect('home')
        else:
            messages.success(request,"whoops ! somw problem!")
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm()  # Initialize the form object
        return render(request, 'users/signup.html', {'form': form})
    


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')





def search(request):
    if request.method == 'POST':  # Corrected the case of 'POST'
        searched = request.POST.get('searched')  # Corrected retrieving data from request
        prods = PostModel.objects.filter(
            Q(title__icontains=searched) |
            Q(description__icontains=searched) |
            Q(category__name__icontains=searched) |  # Added missing comma
            Q(author__username__icontains=searched)  # Changed to username, adapt as needed
        )
        
        if not prods:
            messages.success(request, "Hmm, Your Searched Item Isn't in Our Blog. Keep Scrolling for More!")  # Corrected error message
            return redirect('blog')
        else:
            return render(request, 'store/search.html', {'searched': searched, 'prods': prods})
    else:
        return render(request, 'store/search.html')




def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:  # Debug statement
                instance.author = request.user
                instance.save()
                messages.success(request, 'Post added successfully')
                return redirect('home')
            else:
                return redirect('signin')  # Debug statement
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




def category(request,foo):
    # postt = PostModel.objects.all()
    # Replace hypens with space
    # foo = foo.replace('-',' ')
    
    try:
        category = Category.objects.get(name=foo)
        posts = PostModel.objects.filter(category=category)
        
        return render(request,'store/category-posts.html',{'posts': posts,'category':category})
        
        
    except:
        messages.success(request,("that category does't work"))
        return redirect('home')





def contact(request):
	return render(request,'store/contact.html')





def service(request):
	return render(request,'store/services.html')






def product(request,pk):
    prodviews = PostModel.objects.get(id=pk)
    return render(request,'store/productview.html',{'prodviews':prodviews})
