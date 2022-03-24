from email import message
import profile
from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm,SkillForm
# Create your views here.
from django.http import JsonResponse
from django.core.serializers import serialize
from .utils import searchProjects, paginateProfiles

def login_page(request):
    page='login'
    context={'page':page}
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User not found')

        user = authenticate(request,username=username,password= password)
        
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
             messages.error(request,'Username or password is incorrect!')

    print(context)    
    return render(request,'users/login_register.html',context)

def profiles(request):
    profiles,search_query = searchProjects(request)
    custom_range, profiles, paginator = paginateProfiles(request,profiles,3)
    context = {'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
    return render(request,'users/profiles.html',context)


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(desription__exact="")
    other_skills = profile.skill_set.filter(desription="")  
    context = {'profile':profile,'topSkills':top_skills,'otherSkills':other_skills}
    return render(request,'users/user-profile.html',context)

def logout_user(request):
    logout(request)
    messages.info(request,'User was logged out successfully')
    return redirect('login')

def register_user(request):
    page='register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            print(user.username)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account created!')
            
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'An error has occured during the registration process')
    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects= profile.project_set.all()
    context={'profile':profile,'skills':skills,'projects':projects}

    
    return render(request,'users/account.html',context)

@login_required(login_url="login")
def editAccount(request):
   
    profile = request.user.profile
    form= ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url="login")
def createSkill(request):
    profile = request.user.profile   
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,'Skill was added successfully!')
            return redirect('account')
    context={'form':form}
    
    return render(request,'users/skill_form.html',context)



@login_required(login_url="login")
def updateSkill(request,pk):
    profile = request.user.profile   
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance= skill)
    if request.method == "POST":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'Skill was updated successfully!')
            return redirect('account')
    context={'form':form}
    
    return render(request,'users/skill_form.html',context)


@login_required(login_url="login")
def userInfo(request):
    user = request.user
    user = serialize('json',user)
    context = {'user':user}
    return JsonResponse(context,safe=False)


@login_required(login_url="login")
def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect('account')
    context = {'object':skill}
    return render(request,'delete-template.html',context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('account')
    context={'object':project}
    return render(request,'delete-template.html',context)
    
    
