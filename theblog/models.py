from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=25)
	def __str__(self):
		return self.name

class Post(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
	title=models.CharField(max_length=50,null=False,blank=True,default=" ")
	body=models.TextField() #body of post containing text field
	published= models.DateTimeField(auto_now=True) #displays the time
	Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
	image = models.ImageField(upload_to='images/%Y/%m/%d',default='1.png')

	def __str__(self):
		return '{} published on {}' .format(self.title,self.published)