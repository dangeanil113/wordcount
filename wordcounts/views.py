from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
 return render(request,'home.html',{'name':'New Website'})

def contact(request):
    return HttpResponse('<h2> hello guys this website id under development if you have some suggestions then contect me this is My no 8855063465 Email:dangeanil113@gmail.com</h2>')
def about(request):
    return render(request,'about.html')

def count(request):
    data= request.GET['fulltextarea']
    word_list = data.split()
    length=len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1

            sort_list=sorted(worddictionary.items(), key = operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':data,'word':length,'worddictionary':sort_list})
