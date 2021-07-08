
from django.urls import path
from . import views
# from main.views import NewsSlugView

urlpatterns = [
    path("", views.index, name="index"),
    path("noticias/<str:slug>/<int:id>", views.newsPage, name="newsPage"),
]
