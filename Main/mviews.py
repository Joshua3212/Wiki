###################
####Imports########
###################
from django.shortcuts import render, redirect
from Accounts.models import Article
import datetime



# Create your views here.

##################
####Home##########
##################
def home(request):

    
    return render(
        request,
        "Main/index.html", 
        {
            

        }
    )


##################
####Articles######
##################
def article_dynamic(request, slug):
    obj = Article.objects.get(url=slug)
    
    context = {
            'object':  obj
        }

    return render(
        request,
        "article/article_main.html", context )


def article_delete(request, slug):                    #delete article
    obj = Article.objects.get(url=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/article/')


    context = {
            'object':  obj
        }

    return render(
        request,
        "article/article_delete.html", context )

def article_edit(request, slug):                    #delete article
    obj = Article.objects.get(url=slug)

    if request.method == 'POST':
        obj.delete()

        title = request.POST['title']
        picture = request.POST['picture']
        mainContent = request.POST['mainContent']
        user = request.POST['username']
        date = datetime.datetime.now()
        url = request.POST['url']

        article = Article(user = user, title=title, picture = picture, mainContent = mainContent, date = date, url = url)
        article.save()

        return redirect('/article/')

    context = {
            'object':  obj
        }

    return render(
        request,
        "article/article_edit.html", context )


###################
###Articles#List###
###################
def article(request):
    article = Article.objects.all() #get articles
    search_term = ''
    
    if 'search' in request.GET: 
        search_term = request.GET['search']
        article = article.filter(title=search_term)


    

    context = {'article' : article, 'search_term' : search_term} #array articles

    
    return render(
        request,
        "article/article.html", context
    )
#########################
####proced there^^^######
#########################
