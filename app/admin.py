from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Movie)
admin.site.register(Details)
admin.site.register(Hero_details)