from django.contrib import admin

from .models import ItemStore, Category, Menu

admin.site.register(ItemStore)
admin.site.register(Category)
admin.site.register(Menu)
