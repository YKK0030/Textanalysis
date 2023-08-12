
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def analyzed(request):
    #GET TEXT
    inputtext=request.GET.get('text','default')

    #CHECK VALUE OF CHECK BOXES
    removepunct= request.GET.get('removepun','off')
    fullcaps =request.GET.get('fullcapstext','off')
    lineremover=request.GET.get('newlineremover','off')
    charcount=request.GET.get('count','off')
    spaceremove=request.GET.get('spaceremover','off')
    print(removepunct)
    print(inputtext)

    #CHECK WHICH BOX IS ON
    if removepunct == "on":
        analyzed=inputtext
        punc = '''()[]{}:";',.?/!@#$%^&*_+-='''
        analyzed=""
        for char in inputtext:
            if char not in punc:
                analyzed =analyzed + char
        pro = {'purpose': 'Remove Punction', 'analyzed': analyzed}
        return render(request,'analysis.html',pro)
    elif(fullcaps == 'on'):

        analyzed=""
        for char in inputtext:
            analyzed = analyzed + char.upper()
        pro = {'purpose': 'Changed to uppercase', 'analyzed': analyzed}
        return render(request, 'analysis.html', pro)
    elif(spaceremove=='on'):
        analyzed=""
        for index,char in enumerate(inputtext):
            if not(inputtext[index] == " " and inputtext[index + 1] == " "):
                analyzed=analyzed +char
        pro = {'purpose': "Remove extra space", 'analyzed': analyzed}
        return render(request, 'analysis.html', pro)
    elif(lineremover == 'on'):
        analyzed=""
        for char in inputtext:
            if char !='\n':
                analyzed = analyzed + char.upper()
        pro = {'purpose': 'Line is removed', 'analyzed': analyzed}
        return render(request,'analysis.html',pro)
    elif(charcount == 'on'):
        analyzed=""
        count=0
        for char in inputtext:
            count=count+1
        pro = { 'purpose':'count no. of character', 'analyzed' :count}
        return render(request,'analysis.html',pro)
    else:
        return HttpResponse("Error")
