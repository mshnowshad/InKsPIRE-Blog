from django.db import models
import datetime
from django.utils import timezone
#day 8 | profile
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator



# Categories of Products
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'



class PostModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='post_images/')
    published_in = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-published_in',)

    def __str__(self):
        return self.title
    



class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    image = models.ImageField(default='default.jpg',upload_to='profileImg/',validators=[FileExtensionValidator(['png','jpg'])])
    
    def __str__(self):
      return self.user.username
      


