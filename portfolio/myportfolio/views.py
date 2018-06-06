from django.shortcuts import render
from .models import Projects
# Create your views here.
def project_list(request):
    projects = Projects.project_list()
    return render(request,'index.html',{"projects":projects})
