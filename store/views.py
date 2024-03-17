from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import PostModel,Category
from django.contrib import messages
from django.db.models import Q



# def search(request):
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         #query the products model
#         searched = Product.objects.filter(
#                 Q(name__icontains=searched) | 
#                 Q(description__icontains=searched) | 
#                 Q(category__name__icontains=searched)
#             )
        
      
#         if not searched:
#             messages.success(request,"Your searched product is doesn't exists ")
#             return redirect('home')
            
        
#         else:
#             return render(request, 'search.html',{'searched':searched,'categories':categories})
        
#     else:
        
#         return render(request, 'search.html',{'categories':categories})






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





def signin(request):
	return render(request,'store/signin.html')





def signup(request):
	return render(request,'store/signup.html')


def product(request,pk):
    prodviews = PostModel.objects.get(id=pk)
    return render(request,'store/productview.html',{'prodviews':prodviews})
