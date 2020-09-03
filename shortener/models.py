from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    
class URLShortener(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, help_text="URL name e.g Tinny",default="No name", blank=True)
    description = models.TextField( null=True, blank=True, default='None Given', help_text = "Give a brief description about the site")
    active = models.BooleanField(default=True)
    url = models.URLField(help_text = "e.g. http(s)://www.name_of_website.com")
    unique_id = models.CharField(max_length=20, unique=True, help_text='Type in a I.D or one will be automatically assigned to your URL', blank=True)
    
    
    def __str__(self):
        return f'{self.url} : {self.unique_id}'
        
class Record(models.Model):
    url = models.ForeignKey(URLShortener, models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.url} accessed on {self.created_on}'
    
    
