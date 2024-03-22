from django.urls import path
from .import views



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
	path('signin/',views.sign_in,name='sign_in'),
	path('signin/',views.sign_in,name='signin'),
    
	path('logout',views.logout_user,name="logout")
    
    
	# path('',home,name='home'),
	# path('',home,name='home'),

	



]