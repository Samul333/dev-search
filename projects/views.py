from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utils  import searchProjects, paginateProjects

def projects(request):
    projects,search_query = searchProjects(request)
    results = 3
    custom_index, projects, paginator = paginateProjects(request,projects,results)
     
    context={'projects':projects,'search_query':search_query,'paginator':paginator,'custom_range':custom_index}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print(projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj})
    


@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    
    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        owner = request.user.profile
        
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = owner
            project.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,"projects/project_form.html",context)



@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    
    project = profile.project_set.get(id=pk)
    context = {'object':project}
    return render(request,'projects/delete_object.html',context)