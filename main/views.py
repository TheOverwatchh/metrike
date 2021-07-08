from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from .models import News
# Create your views here.
def index(request):
    news = News.objects.all()
    return render(request, "main/index.html", {
        "news": news,
    })
def newsPage(request,slug, id): 
    try:
        news = News.objects.get(id=id)
    except:
        return HttpResponseRedirect(reverse("index"))     
    return render(request, "main/newsPage.html", {
        "news": news
    })


# class NewsSlugView(DetailView):
#     queryset = News.objects.all()
#     template_name = "main/index.html"

#     def get_object(self, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         instance = get_object_or_404(News, slug = slug)
#         try:
#             instance = News.objects.get(slug = slug)
#         except News.MultipleObjectsReturned:
#             qs = News.objects.filter(slug = slug)
#             instance =  qs.first()
#         return instance


# def product_detail_view(request, pk = None, *args, **kwargs):
#     instance = News.objects.get_by_id(pk)
#     print(instance)
#     if instance is None:
#         raise Http404("Esse produto não existe!")
#     context = {
#         'object': instance
#     }
#     return render(request, "main/index.html", context)
