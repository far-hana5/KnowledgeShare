from django.shortcuts import render, redirect
from .models import Blog, Category

def posts_by_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return redirect('home')   

    posts = Blog.objects.filter(status='Published', category=category)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
