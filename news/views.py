from django.shortcuts import render, get_object_or_404
from news.models.news_model import News
from django.http import Http404


def index(request):
    context = {"all_news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, news_id):
    try:
        news = get_object_or_404(News, id=news_id)
        return render(request, "news_details.html", {"news": news})
    except Http404:
        return render(request, "404.html")
