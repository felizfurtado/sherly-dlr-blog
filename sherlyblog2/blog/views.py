from django.shortcuts import render , get_object_or_404 , redirect
from .models import Blog
from django.core.paginator import Paginator

def home(request):
    blog_list = Blog.objects.all().order_by('-created_at')

    paginator = Paginator(blog_list, 10)  # 👈 10 blogs per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, "index.html", {"blogs": blogs})


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, "blog_detail.html", {"blog": blog})


def create_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.POST.get('image')
        content = request.POST.get('content')

        Blog.objects.create(
            title=title,
            category=category,
            image=image,
            content=content
        )

        return redirect('home')

    return render(request, "create_blog.html")