from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('account/,',views.userAccount,name="account"),
    path('login/', views.login_page,name="login"),
    path('logout/', views.logout_user,name="logout"),
    path('register/', views.register_user,name="register"),
    path('',views.profiles,name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('create-skill/',views.createSkill,name="create-skill"),
    path('update-skill/<str:pk>/',views.updateSkill,name="update-skill"),
    path('user-info/',views.userInfo,name="user-info"),
    
    path('delete-skill/<str:pk>/',views.deleteSkill,name="delete-skill"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),
]
