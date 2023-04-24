from django.contrib import admin
from app1.models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_display=('id','rdate','moviename','hero','heroine','rating')
admin.site.register(Movie,MovieAdmin)
# Register your models here.
