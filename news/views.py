from django.shortcuts import render, redirect, get_object_or_404
from news.forms import CreateCategoryForm, CreateNewsForm
from news.models.category_model import Categories
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


def create_categories(request):
    form = CreateCategoryForm()

    if request.method == "POST":
        form = CreateCategoryForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)


def create_news(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            created_news = form.save()

            categories = form.cleaned_data["categories"]
            for category in categories:
                created_news.add_category(category)

            return redirect("home-page")

    context = {"form": form}

    return render(request, "news_form.html", context)
