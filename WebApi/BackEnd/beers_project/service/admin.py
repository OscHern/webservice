from django.contrib import admin

# Register your models here.

from .models import Beer, Kind, Selection, User


admin.site.register(Beer)
admin.site.register(Kind) 
admin.site.register(Selection)
admin.site.register(User)

