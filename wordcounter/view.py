from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')
def count(request):
    counter=request.GET['counter']
    wordlist=counter.split()
    return render(request, 'count.html',{'counter':counter, 'count1': len(wordlist)})
def about(request):
    return render(request,'about.html')

