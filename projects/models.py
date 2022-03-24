from enum import unique
from hashlib import blake2b
from django.db import models
import uuid
from users.models import Profile

class BaseModel(models.Model):
    """
    BaseModel
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(BaseModel):
    owner= models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True,blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField('Tag', blank=True) 
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering=['created_at']
    


class Review(BaseModel):
    VOTE_TYPE=(
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    # owner
    project = models.ForeignKey(Project,on_delete=models.CASCADE)   
    body = models.TextField(null=True, blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    
    
    def __str__(self) -> str:
        return self.value
    


class Tag(BaseModel):
    name = models.CharField(max_length=200)
    
    
    def __str__(self) -> str:
        return self.name
    