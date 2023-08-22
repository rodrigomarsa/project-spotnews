from django.shortcuts import render
from news.models.news_model import News


def index(request):
    context = {"all_news": News.objects.all()}
    return render(request, "home.html", context)
