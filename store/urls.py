
from django.urls import path
from .import views

#video number 7
from django.contrib.auth import views as auth_view   # এই মডিউলটি ক্লাস-ভিত্তিক ভিউ (ডিজাঙ্গো ১.১১ এ প্রবর্তিত) লগইন, লগআউট, পাসওয়ার্ড রিসেট এবং পাসওয়ার্ড পরিবর্তন করার মতো সাধারণ প্রামাণীকরণ টাস্কগুলি


urlpatterns = [
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('blog/',views.blog,name='blog'),
	path('contact/',views.contact,name='contact'),
	path('service/',views.service,name='service'),
	path('add_post/',views.add_post,name='add_post'),
	path('category/<str:foo>',views.category,name="category"),
	path('product/<int:pk>', views.product,name='product'),
	path('search/',views.search,name='search'),
    
	path('signup/',views.sign_up,name='sign_up'),
    
	path('signin/',auth_view.LoginView.as_view(template_name="users/signin.html"),name="sign_in"),
    
	path('logout/',views.logout_user,name="logout")
    
    
	# path('',home,name='home'),
	# path('',home,name='home'),

	



]