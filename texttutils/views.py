from django.http import HttpResponse
from django.shortcuts import render

def index(request):

   return render(request,'index.html')


def analyze(request):
    #get the text
    djtext=(request.POST.get('text', 'default'))

    # Check check
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps =   (request.POST.get('fullcaps', 'off'))
    shortcaps =  (request.POST.get('shortcaps', 'off'))
    newlineremover =  (request.POST.get('newlineremover', 'off'))
    Extraspaceremover = (request.POST.get('Extraspaceremover', 'off'))
    countcaps = (request.POST.get('countcaps', 'off'))




    #Analyze the text
    if removepunc == "on":
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
       analyzed = " "
       for char in djtext:
           if char not in punctuations:
               analyzed = analyzed + char
       params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
       djtext = analyzed


    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext == analyzed


    if (shortcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'changed to lowercase', 'analyzed_text': analyzed}
        djtext == analyzed


    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext == analyzed


    if (Extraspaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]== " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Space','analyzed_text':analyzed}
        djtext == analyzed


    if (countcaps == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1

        params = {'purpose':'Count The Number Of Character','analyzed_text':analyzed}
        djtext == analyzed


    if (removepunc != "on" and fullcaps != "on" and shortcaps != "on" and newlineremover != "on" and Extraspaceremover != "on" and countcaps != "on"):
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)


