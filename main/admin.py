from django.contrib import admin
from .models import News


# class NewsAdmin(admin.ModelAdmin):
# 	list_display = ('__str__', 'slug')
# 	class meta:
# 		model = News
# Register your models here.
admin.site.register(News)


# superuser user:micaeltargino  password: access2000