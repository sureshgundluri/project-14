from django.shortcuts import render

def htmlfile(request):
    return render(request,'htmlfile1.html')

def suresh(request):
    return render(request,'htmlfile2.html')