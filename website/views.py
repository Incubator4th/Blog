from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django import forms
from website.models import Article
import datetime
from markdown import markdown
from taggit.models import Tag
from django.core.paginator import Paginator
# Create your views here.



def index(request):
    return page(request,0)

def article(request,id):
    jsonfile =  Article.objects.filter(id=id)[0]
    tags = Tag.objects.filter(article__id=id)
    print(tags)
    if jsonfile:
        jsonfile.content = markdown(jsonfile.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        print(jsonfile)
        print(jsonfile.tags)
        return render(request,'article.html',{'jsonfile':jsonfile,'tags':tags})
    else:
        jsonfile = {
            "id": id,
            "title": "This is title",
            "mod_date": str(datetime.datetime.now()),
            "content": "You're looking at article %s." % id
        }
        return render(request, 'article.html', {'jsonfile': jsonfile})

def test_article(request):
    return render(request,'article.html')

def page(request,pagenum):
    articles = Article.objects.all().order_by('-id')
    if len(articles) > 5:
        p = Paginator(articles, 5)
        thispage = p.page(pagenum)
        has_previous = thispage.has_previous()
        has_next = thispage.has_next()
    else:
        thispage = articles
        has_previous = False
        has_next = False
    for article in thispage:
        article.content = markdown(article.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    return render(request, 'index.html', {'thispage': thispage,
                                          'has_previous': has_previous,
                                          'has_next': has_next})


def showmyinfo():
    about_me = "一个普通程序员的普通博客"
    all_tags = Tag.objects.all()
    print(all_tags)

def orderBytags(request,tagname):
    articles = Article.objects.filter(tags__name__in=[tagname])
    print(articles)
    for article in articles:
        article.content = markdown(article.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    return render(request, 'index.html', {'thispage': articles,
                                          'has_previous': False,
                                          'has_next': False})