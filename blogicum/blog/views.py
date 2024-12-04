from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404
from .models import Post, Category


def index(request):
    now = timezone.now()

    posts = Post.objects.filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    if post.pub_date > timezone.now():
        raise Http404("Публикация еще не доступна")

    if not post.is_published:
        raise Http404("Публикация не найдена или недоступна")

    if not post.category.is_published:
        raise Http404("Категория публикации не доступна")

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404("Категория не существует или недоступна")

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    return render(request,
                  'blog/category.html',
                  {'category': category, 'post_list': post_list})
