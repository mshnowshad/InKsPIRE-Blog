from django.urls import path
from .views import *
urlpatterns = [
	path('',home,name='home'),
	path('about/',about,name='about'),
	path('blog/',blog,name='blog'),
	path('contact/',contact,name='contact'),
	path('signin/',signin,name='signin'),
	path('signup/',signup,name='signup'),
	path('service/',service,name='service'),

	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),
	# path('',home,name='home'),

	



]