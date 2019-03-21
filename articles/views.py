from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import Article,Comment
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,"articles/article_list.html",{'articles':articles })

def article_detail(request, slug):
    #return HttpResponse(slug)
    articles = Article.objects.all().order_by('-date')
    article = Article.objects.get(slug=slug)
    comments = article.comments.all().order_by('-comment_date')
    return render(request, 'articles/article_detail.html',{'article':article,'articles':articles,'comments':comments})

def bilim(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/bilim.html',{'articles':articles})

def teknoloji(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/teknoloji.html',{'articles':articles})

def biltek_nostalji(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/bilteknostalji.html',{'articles':articles})

def about(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,"articles/about.html", {'articles':articles })

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("articles:detail",kwargs={"slug":article.slug}))

def all(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/all.html',{'articles':articles})    
