
from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username', 'password1','password2']
        labels={
            'first_name ':'Name'
        }
        
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
    # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Enter Project Title'})
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields=['name','username','email','location','bio','short_intro','profile_image','social_github','social_linkedIn','social_website','social_youtube']
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
    # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Enter Project Title'})
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(ModelForm):
    class Meta:
        model= Skill
        fields= '__all__'
        exclude = ['owner']
    
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
    # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Enter Project Title'})
    
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
