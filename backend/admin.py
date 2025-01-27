from django.contrib import admin

from backend.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    # list display
    list_display = ('name','id')

admin.site.register(Category,CategoryAdmin)