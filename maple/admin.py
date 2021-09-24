from django.contrib import admin
from .models import Menu, Application, Chicken, Beef, Side

# Register your models here.
admin.site.register(Menu)
admin.site.register(Application)
admin.site.register(Chicken)
admin.site.register(Beef)
admin.site.register(Side)