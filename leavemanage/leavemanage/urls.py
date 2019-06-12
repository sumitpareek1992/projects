"""leavemanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from app1.views import user_register,home_view,logout_view
from app1.models import Leave, LeaveType
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
    path('',home_view),
    path('register/', user_register),
    path('index/', login_required(TemplateView.as_view(template_name='app1/index.html'))),
    path('leave/',login_required(ListView.as_view(
        model=Leave,
        #template_name="app1/leave_list.html"
        ))),
    path('leave_create/', login_required(CreateView.as_view(
        model=Leave,
        #fields="__all__",
        fields=["desc","type","leavedate","user"],
        success_url="/leave/"
        #template_name="app1/leave_form.html"
        ))),
    re_path('leave_update/(?P<pk>[0-9]+)', login_required(UpdateView.as_view(
        model=Leave,    
        fields=["desc","type","leavedate","user"],
        success_url="/leave/",
        template_name="app1/leave_update_form.html"
        ))),
    re_path('leave_delete/(?P<pk>[0-9]+)',login_required(DeleteView.as_view(
        model=Leave,
        success_url="/leave",
        #template_name="app1/leave_confirm_update.html"
        ))),
    path('leavetype/', ListView.as_view(
        model=LeaveType,
        #template_name="app1/leavetype_list.html"
        )),
    path('leavetype_create/',CreateView.as_view(
        model=LeaveType,
        fields="__all__",
        success_url="/leavetype/",
        )),
    re_path('leavetype_update/(?P<pk>[0-9]+)',login_required(UpdateView.as_view(
        model=LeaveType,
        #fields=["desc","type","leavedate","user"],
        fields="__all__",
        success_url="/leavetype",
        template_name="app1/leavetype_update_form.html"
        ))),
    re_path('leavetype_delete/(?P<pk>[0-9]+)',DeleteView.as_view(
        model=LeaveType,
        success_url="/leavetype/",
        )),
]
