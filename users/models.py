from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=300,blank=True,null=True)
    short_intro= models.CharField(max_length=200,blank=True,null=True)
    bio= models.TextField(blank=True,null=True)
    profile_image= models.ImageField(null=True,blank=True,upload_to='profiles/', default='profiles/user-default.png')
    social_github=models.CharField(max_length=200,blank=True,null=True)
    social_linkedIn=models.CharField(max_length=200,blank=True,null=True)
    social_website=models.CharField(max_length=200,blank=True,null=True)
    social_youtube=models.CharField(max_length=200,blank=True,null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return str(self.user.username)
    

class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    desription = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)
    
    
    


