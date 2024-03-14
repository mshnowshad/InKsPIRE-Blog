from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User






# Categories of Products
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	#@daverobb2011
	class Meta:
		verbose_name_plural = 'categories'






# All of our Products
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='post_images/')
    published_in = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-published_in',)
 
    def __str__(self):
        return self.title


