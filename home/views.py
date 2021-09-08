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
    if request.method == 'GET':
        results = True
        return render(request,"veronica.html",{'results':results})
    if request.method == "POST":
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
            # A boolean var takes the leaast space so idts that this will slow down the server too much
            h1RES = False
            h2RES = False
            h3RES = False
            h4RES = False
            h5RES = False
            h6RES = False
            pRES = False
            anRES = False
            alRES = False
            divRES = False
            divtagRES = False
            titleRES = False
            sourceurlRES = False
            alltagnamesRES = False
            htmlRES = False
            bodyRES = False
            classnameRES = False
            idnameRES = False
            strongRES = False
            emRES = False
            uRES = False
            results = True
            response = []
            url = request.POST.get('url')
            response = False
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html.parser')
                html_content = requests.get(url).text
                soupxml = BeautifulSoup(html_content, "lxml")
            except:
                messages.error(request,"Check the URL you have Entered")
                return redirect('veronica')

            # Parse the html content
            if  request.POST.get('html') == "on" :
                html.append(soupxml.prettify()) # print the parsed data of html
                htmlRES = True
                response = True
            split_url= urlsplit(url)
    
            #SPLITTING URL  
            ht = split_url.scheme
            webad= split_url.netloc

            homepage = ht + "://" + webad 

            # HEADER 1 TAG
            if request.POST.get('h1') == "on" :
                for i in soup.find_all('h1'):
                    h1.append(i.get_text())
                h1RES = True
                response = True


            # HEADER 2 TAG
            if request.POST.get('h2') == "on" :
                for i in soup.find_all('h2'):
                    h2.append(i.get_text())
                h2RES = True
                response = True
                
            # HEADER 3 TAG
            if request.POST.get('h3') == "on" :
                for i in soup.find_all('h3'):
                    h3.append(i.get_text())
                h3RES = True
                response = True
            # HEADER 4 TAG
            if request.POST.get('h4') == "on" :
                for i in soup.find_all('h4'):
                    h4.append(i.get_text())
                h4RES = True
                response = True
            # HEADER 5 TAG
            if request.POST.get('h5') == "on" :
                for i in soup.find_all('h5'):
                    h5.append(i.get_text())
                h5RES = True
                response = True
            # HEADER 6 TAG
            if request.POST.get('h6') == "on" :
                for i in soup.find_all('h6'):
                    h6.append(i.get_text())
                h6RES = True
                response = True

            # PARAGRAPH TAG
            if request.POST.get('p') == "on" :
                for i in soup.find_all('p'):
                    p.append(i.get_text())
                pRES = True
                response = True

            # ANCHOR Name TAG
            if request.POST.get('an') == "on" :
                for i in soup.find_all('a'):
                    an.append(i.get_text())
                anRES = True
                response = True
            
            # ANCHOR Links TAG
            if request.POST.get('al') == "on" :

                for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
                    # display the actual urls
                    al.append(link.get('href'))
                alRES = True
                response = True

            # IMAGES 
            if request.POST.get('img') == "on" :

                for img in soup.find_all('img', attrs={'src': re.compile("^https://")}):
                    if img.has_attr('src'):
                        image.append(img['src'])
                response = True
                
                for img in soup.find_all('img', attrs={'data-pin-media': re.compile("^https://")}):
                    if img.has_attr('data-pin-media'):
                        image.append(img['data-pin-media'])

                for img in soup.find_all('img', attrs={'srcset': re.compile("^https://")}):
                    if img.has_attr('srcset'):
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        print(img['srcset'])
                        image.append(img['srcset'])
                response = True

            # DIVISION TEXT
            if request.POST.get('divtext') == "on" :

                for i in soup.find_all('div'):
                    sde = i.get_text('div')
                    div.append(sde.replace("div",""))
                divRES = True
                response = True

            # DIVISION TAG
            if request.POST.get('divtag') == "on" :
                divtag.append(soupxml.div)
                divtagRES = True
                response = True

            
            # ALL TAGS NAMES
            if request.POST.get('alltags') == "on" :

                for i in soup.findAll(True):
                    x= "<" + i.name + ">" #first time i concatenated strings in python :)
                    alltagnames.append(x)
                alltagnames = True
                response = True

            # TITLE PAG NAME
            if request.POST.get('title') == "on" :
                title.append(soupxml.title.text)        
                titleRES = True
                response = True

            # BODY TAG
            if request.POST.get('body') == "on" :
                body.append(soupxml.body)
                response = True
                bodyRES = True

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
                classRes = True
                response = True
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
                idRES = True
                response = True

            # STRONG
            if request.POST.get('strong') == "on" :
                for i in soup.find_all( 'strong' ):
                    strong.append(i.get_text())
                strongRES = True
                response = True
            # ITALICS
            if request.POST.get('em') == "on" :
                for i in soup.find_all( 'em' ):
                    em.append(i.get_text())
                emRES = True
                response = True

            # UNDERLINE
            if request.POST.get('u') == "on" :
                for i in soup.find_all( 'u' ):
                    u.append(i.get_text())
                uRES = True
                response = True
            
            if  image == False and h1 == False and h2 == False and h3 == False and h4 == False and h5 == False and h6 == False and p == False and an == False and al == False and image == False and div == False and divtag == False and sourceurl == False and alltagnames == False and html == False and body == False and classname == False and idname == False and strong == False and em == False and u == False and title == False and response == False and h1RES == False and h2RES == False and h3RES == False and h4RES == False and h5RES == False and h6RES == False and pRES == False and anRES == False and alRES == False and divRES == False and divtagRES == False and titleRES == False and sourceurlRES == False and alltagnamesRES == False and htmlRES == False and bodyRES == False and classnameRES == False and idnameRES == False and strongRES == False and emRES == False and uRES == False:
                results = False
            context={
                'image': image,
                'h1':h1,
                'h2':h2,
                'h3':h3,
                'h4':h4,
                'h5':h5,
                'h6':h6,
                'p':p,
                'an':an,
                'al':al,
                'image':image,
                'div':div,
                'divtag':divtag,
                'sourceurl':sourceurl,
                'alltagnames':alltagnames,
                'html':html,
                'body':body,
                'classname':classname,
                'idname':idname,
                'strong':strong,
                'em':em,
                'u':u,
                'title':title,
                'response':response,
                'h1RES':h1RES,
                'h2RES':h2RES,
                'h3RES':h3RES,
                'h4RES':h4RES,
                'h5RES':h5RES,
                'h6RES':h6RES,
                'pRES':pRES,
                'anRES':anRES,
                'alRES':alRES,
                'divRES':divRES,
                'divtagRES':divtagRES,
                'titleRES':titleRES,
                'sourceurlRES':sourceurlRES,
                'alltagnamesRES':alltagnamesRES,
                'htmlRES':htmlRES,
                'bodyRES':bodyRES,
                'classnameRES':classnameRES,
                'idnameRES':idnameRES,
                'strongRES':strongRES,
                'emRES':emRES,
                'uRES':uRES,
                'results':results,
            }
            responseRES = True
    return render(request,"veronica.html",context)

def mediascrap(request):
    return render (request,'comingsoonmedia.html')

def founder(request):
    return render (request,'comingsoonfounder.html')

def handler404(request, exception):
    return render(request,'404.html')

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
