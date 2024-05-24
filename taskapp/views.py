

# Create your views here.
from django.shortcuts import render, redirect
from .models import Profile, PortfolioItem, Project
from .forms import ProfileForm, PortfolioItemForm, ProjectForm

def profile(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form, 'profiles': profiles})

def portfolio(request):
    items = PortfolioItem.objects.all()

    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioItemForm()

    return render(request, 'portfolio.html', {'form': form, 'items': items})

def project(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ProjectForm()

    return render(request, 'project.html', {'form': form, 'projects': projects})
