from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import Blogs, Comment
from  .models import Author
from django.core.paginator import Paginator

from .forms import BlogForm


def blogs(request):
    bloglist = Blogs.objects.all()
    page = request.GET.get('page',1)
    paginator= Paginator(bloglist,5)
    blogs = paginator.page(page)
    return render(request, 'blog.html', {'ob': bloglist,'blogs':blogs})


def get_user(user):
    a = Author.objects.filter(author=user)
    return a[0]


def create_blog(request):
    form = BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        # instance = form.save(commit=False)
        # instance.user = request.user
        # instance.save()
        # form.instance.Author = Author.objects.get(author=request.user.username)
        form.instance.author = get_user(request.user)
        form.save()
        form = BlogForm()
    contex = {'form': form}
    return render(request, 'blogform.html', contex)


def create_comment(request):
    if request.method == 'POST':
        nam = request.POST['name']
        eid = request.POST['email']
        web = request.POST['website']
        # date = request.POST['date']
        msg = request.POST['message']
        print(nam)
        print(eid)
        comment = Comment.objects.create(name=nam, email=eid, website=web, message=msg)
        comment.save()
    return redirect('blog')
    # return render(request, 'blog.html')


def article(request, id):
    obj1 = get_object_or_404(Blogs, id=id)
    obj2 = Comment.objects.all()
    obj3 = Comment.objects.count()
    obj4 = Blogs.objects.all()
    return render(request, 'article.html', {'ob': obj1, 'ob2': obj2, 'ob3': obj3, 'ob4': obj4})
def delete_blog(request,id=None):
    query=get_object_or_404(Blogs,id=id)
    query.delete()
    return redirect('blog')
def update_blog(request,id):
    instance = get_object_or_404(Blogs,id=id)
    form = BlogForm(request.POST or None,request.FILES or None,instance = instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect('blog')
    context={
        "title":instance.title,
        "content":instance.content,
        "image":instance.image,
        "instance":instance,
        "form":form,
    }
    return render(request,"blogform.html",context)
