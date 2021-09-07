from django.shortcuts import render, redirect, HttpResponse
from django.http import request
from django.http.response import HttpResponseRedirect

from bs4 import BeautifulSoup #imported Beautiful Soup
from urllib.parse import urlsplit, urlunsplit
import requests #In order to work with the HTML, we will have to get the HTML as a string.

import re
from django.contrib import messages

def home(request):
    return render(request,"index.html")
    
def veronica(request):
    image = []
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    h5 = []
    h6 = []
    p =  []
    an = []
    al = []
    div= []
    divtag = []
    title = []
    sourceurl = []
    alltagnames = []
    html = []
    body = []
    classname = []
    idname = []
    strong = []
    em = []
    u = []
    linktag= []
    linksrc= []
    styletag= []
    stylesrc= []
    scripttag= []
    scriptsrc= []
    response = []
    mess = []
    if request.method == "POST":
        url = request.POST.get('url')
        response = "TRUE"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        html_content = requests.get(url).text
        soupxml = BeautifulSoup(html_content, "lxml")

        #CHECK CONDITION#
        statehtml = request.POST.get('html'),
        statebody = request.POST.get('body'),
        stateh1 = request.POST.get('h1'),
        stateh2 = request.POST.get('h2'),
        stateh3 = request.POST.get('h3'),
        stateh4 = request.POST.get('h4'),
        stateh5 = request.POST.get('h5'),
        stateh6 = request.POST.get('h6'),
        statep = request.POST.get('p'),
        statean = request.POST.get('an'),
        stateal = request.POST.get('al'),
        stateimg = request.POST.get('img'),
        statedivtext = request.POST.get('divtext'),
        statedivtag = request.POST.get('divtag'),
        statealltags = request.POST.get('alltags'),
        statetitle = request.POST.get('title'),
        stateclass = request.POST.get('class'),
        stateid = request.POST.get('id'),
        statestrong = request.POST.get('strong'),
        stateem = request.POST.get('em'),
        stateu = request.POST.get('u'),
        #CHECK CONDITION#


        # Parse the html content
        if  request.POST.get('html') == "on" :
            html.append(soupxml.prettify()) # print the parsed data of html

        split_url= urlsplit(url)
  
        #SPLITTING URL  
        print(split_url.scheme)
        print(split_url.netloc)
        ht = split_url.scheme
        webad= split_url.netloc

        homepage = ht + "://" + webad 
        print(homepage)   

        # HEADER 1 TAG
        if request.POST.get('h1') == "on" :
            for i in soup.find_all('h1'):
                h1.append(i.get_text())

        # HEADER 2 TAG
        if request.POST.get('h2') == "on" :
            for i in soup.find_all('h2'):
                h2.append(i.get_text())
            
        # HEADER 3 TAG
        if request.POST.get('h3') == "on" :
            for i in soup.find_all('h3'):
                h3.append(i.get_text())
        
        # HEADER 4 TAG
        if request.POST.get('h4') == "on" :
            for i in soup.find_all('h4'):
                h4.append(i.get_text())

        # HEADER 5 TAG
        if request.POST.get('h5') == "on" :
            for i in soup.find_all('h5'):
                h5.append(i.get_text())
        
        # HEADER 6 TAG
        if request.POST.get('h6') == "on" :
            for i in soup.find_all('h6'):
                h6.append(i.get_text())

        # PARAGRAPH TAG
        if request.POST.get('p') == "on" :
            for i in soup.find_all('p'):
                p.append(i.get_text())

        # ANCHOR Name TAG
        if request.POST.get('an') == "on" :
            for i in soup.find_all('a'):
                an.append(i.get_text())
        
        # ANCHOR Links TAG
        if request.POST.get('al') == "on" :

            for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
                # display the actual urls
                al.append(link.get('href'))

        # IMAGES 
        if request.POST.get('img') == "on" :

            for img in soup.find_all('img', attrs={'src': re.compile("^https://")}):
                if img.has_attr('src'):
                    image.append(img['src'])
            
            for img in soup.find_all('img', attrs={'data-pin-media': re.compile("^https://")}):
                if img.has_attr('data-pin-media'):
                    image.append(img['data-pin-media'])

        # DIVISION TEXT
        if request.POST.get('divtext') == "on" :

            for i in soup.find_all('div'):
                sde = i.get_text('div')
                div.append(sde.replace("div",""))            

        # DIVISION TAG
        if request.POST.get('divtag') == "on" :
            divtag.append(soupxml.div)

        
        # ALL TAGS NAMES
        if request.POST.get('alltags') == "on" :

            for i in soup.findAll(True):
                x= "<" + i.name + ">" #first time i concatenated strings in python :)
                alltagnames.append(x)

        # TITLE PAG NAME
        if request.POST.get('title') == "on" :
            title.append(soupxml.title.text)        

        # BODY TAG
        if request.POST.get('body') == "on" :
            body.append(soupxml.body)

        #-------------------------FOR CLASS NAMES------------------------------------
        # ITERATE class names
        if request.POST.get('class') == "on" :
            tags = {tag.name for tag in soup.find_all()}
            for tag in tags:
            
                # FIND ALL ELEMENT OF A TAG
                for i in soup.find_all( tag ):
                
                    # IF A TAG HAS AN ATTRIBUTE OF CLASS
                    if i.has_attr( "class" ):
                    
                        if len( i['class'] ) != 0:
                            classname.append(i['class'])
            #-------------------------FOR ID NAMES------------------------------------
        # ITERATE id names
        if request.POST.get('id') == "on" :
            tags = {tag.name for tag in soup.find_all()}

            for tag in tags:
            
                # FIND ALL ELEMENT OF A TAG
                for i in soup.find_all( tag ):
                
                    # IF A TAG HAS AN ATTRIBUTE OF ID
                    if i.has_attr( "id" ):
                    
                        if len( i['id'] ) != 0:
                            idname.append(i['id'])

        # STRONG
        if request.POST.get('strong') == "on" :
            for i in soup.find_all( 'strong' ):
                strong.append(i.get_text())
        # ITALICS
        if request.POST.get('em') == "on" :
            for i in soup.find_all( 'em' ):
                em.append(i.get_text())
        # UNDERLINE
        if request.POST.get('u') == "on" :
            for i in soup.find_all( 'u' ):
                u.append(i.get_text())

    return render(request,"veronica.html",{'image': image,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6,'p':p,'an':an,'al':al,'image':image,'div':div,'divtag':divtag,'sourceurl':sourceurl,'alltagnames':alltagnames,'html':html,'body':body,'classname':classname,'idname':idname,'strong':strong,'em':em,'u':u,'linktag':linktag,'styletag':styletag,'scripttag':scripttag,'linksrc':linksrc,'stylesrc':stylesrc,'scriptsrc':scriptsrc,'title':title,'response':response,'mess':mess,})

def mediascrap(request):
    return render (request,'comingsoonmedia.html')

def founder(request):
    return render (request,'comingsoonfounder.html')

def handler404(request, exception):
    return render(request,'404.html')

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
