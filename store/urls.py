from django.urls import path
from .import views
urlpatterns = [
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('blog/',views.blog,name='blog'),
	path('contact/',views.contact,name='contact'),
	path('signin/',views.signin,name='signin'),
	path('signup/',views.signup,name='signup'),
	path('service/',views.service,name='service'),
	path('add_post/',views.add_post,name='add_post'),
	path('category/<str:foo>',views.category,name="category"),
	path('product/<int:pk>', views.product,name='product'),
	path('search/',views.search,name='search'),
    

	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),

	



]