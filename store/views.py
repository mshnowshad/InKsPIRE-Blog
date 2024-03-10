from django.shortcuts import render

# Create your views here.



def home(request):
	return render(request,'store/index.html')



def about(request):
	return render(request,'store/about.html')

def blog(request):
	return render(request,'store/blog.html')


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
