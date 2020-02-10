###############
###Imports#####
###############
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Article
import datetime



#############
##register###
#############
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/login/')
    else:
        form = UserCreationForm()


    return render(
        request,
        "registration/register.html",
        {
            'form':form
        }
        
   )
#############
##dashboard##
#############

def dashboard(request):
    username = request.user 

    obj = Article.objects.get(user=username)

    context = {
            'object':  obj
        }

    return render(
        request,
        "dashboard/index.html", context)

def post(request):
    ############
    #save#to#db#
    ############
    if request.method == 'POST':
        title = request.POST['title']
        picture = request.POST['picture']
        mainContent = request.POST['mainContent']
        user = request.POST['username']
        date = datetime.datetime.now()
        url = request.POST['url']



        article = Article(user = user, title=title, picture = picture, mainContent = mainContent, date = date, url = url)
        article.save()

        return redirect('dashboard')



    return render(
        request,
        "dashboard/post.html",
        {
            
        }
   )
