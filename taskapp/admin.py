
from django.contrib import admin

from taskapp.models import PortfolioItem, Project,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(PortfolioItem)
admin.site.register(Project)
