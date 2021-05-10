from django.contrib import admin
from .models import News, Parceiros


# class NewsAdmin(admin.ModelAdmin):
# 	list_display = ('__str__', 'slug')
# 	class meta:
# 		model = News
# Register your models here.
admin.site.register(News)
admin.site.register(Parceiros)


# superuser user:micaeltargino  password: access2000