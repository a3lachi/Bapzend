import datetime

import json
from django.http import HttpResponse , HttpResponseNotFound , JsonResponse
from django import forms
from django.shortcuts import render
from rest_framework import viewsets , generics
from .serializers import BapzSerializer
from .serializers import CustomerSerializer
from .models import Bapz
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import jwt
import os 

DIR_BASE = './media/images/'

class BapzView(generics.ListAPIView):
    serializer_class = BapzSerializer
    queryset = Bapz.objects.all()


@csrf_exempt 
def BapzId(request) :
    serializer_class = BapzSerializer

    if request.method == 'POST':
        id = json.loads(request.body )['id']
        prod = Bapz.objects.filter(id=id)
        if (len(prod)==1) :
            name = ''.join(prod[0].productname.split(' '))
            res = []
            for filename in os.listdir(DIR_BASE) :
                cc = filename.split('.jpg')[0]
                if cc[:-1] == name : 
                    res.append(filename)
            return JsonResponse({'found':"yes",'src':res,'data':serializers.serialize('json', prod)})
        else :
            return JsonResponse({'found':"no"})
    else :
        return JsonResponse({'info':"notPOST" })    

@csrf_exempt 
def BapzCatView(request):
    serializer_class = BapzSerializer

    if request.method == 'POST':
        json_data = json.loads(request.body ) 

        try : 
            cat = json_data['cat']
        
            queryset = Bapz.objects.filter(category=cat)
            data = []
            for lop in queryset :
                name = lop.productname 
                id = lop.id
                nospacename = ''.join(name.split(' '))
                res=[]
                for filename in os.listdir(DIR_BASE) :
                    cc = filename.split('.jpg')[0]
                    if cc[:-1] == nospacename : 
                        res.append(filename)
                data.append([name,sorted(res)[:2],id,int(lop.price.split('$')[1].split('.')[0]) ])
                        
            # data = serializers.serialize('json', names)
            
            return JsonResponse({'info':"catview" , 'data':data})
        except KeyError :
            queryset = Bapz.objects.filter(category='t-shirts')[:2] |  Bapz.objects.filter(category='shoes')[:2] | Bapz.objects.filter(category='pants')[:2] |  Bapz.objects.filter(category='watches')[:2] | Bapz.objects.filter(category='bags')[:2] | Bapz.objects.filter(category='sweats')[:2] 
            data = []
            for lop in queryset :
                name = lop.productname 
                id = lop.id 
                nospacename = ''.join(name.split(' '))
                res=[]
                for filename in os.listdir(DIR_BASE) :
                    cc = filename.split('.jpg')[0]
                    if cc[:-1] == nospacename : 
                        res.append(filename)
                data.append([name,sorted(res)[:2],id,lop.price])

            
            return JsonResponse({'lol':"notcat",'data':data})
    else :
        return JsonResponse({'lol':"notPOST" })



@csrf_exempt 
def BapzProduct(request) :
    serializer_class = BapzSerializer
    print('hgjfdsgfh-------------',Bapz.objects.filter(category='shoes')[0])

    if request.method == 'POST':
    #     for filename in os.listdir(DIR_BASE) :
    #         cc = filename.split('.jpg')[0]
    #         if cc[:-1] == toAdd : 
    #             res.append(filename)
    
    #     id = Bapz.objects.filter(productname="BAPE STA")[0].id
        # data = serializers.serialize('json', queryset)
    # data = {'toAdd': toAdd, 'results': queryset}
        return JsonResponse({'info':"new", 'src':'res' ,'id':'id'})
    else :
        return JsonResponse({'lol':"notPOST" })





class CustomerForm(forms.Form):
    email = forms.EmailField()
    pwd = forms.CharField(widget=forms.Textarea)

@csrf_exempt 
def GetCustomer(request):
    serializer_class = CustomerSerializer
    if request.method == 'POST':
        try: 
            json_data = json.loads(request.body ) 

            ## Login 
            if len(json_data)==2 :
                em = json_data['email']
                pd = json_data['pwd']
                usr = Customer.objects.filter(email=em , pwd=pd)
                if len(usr)>0 :
                    token = jwt.encode({"email":em , "brr":str(datetime.datetime.now())}, key='secret')  ## added brr to make jwt unique
                    usr.update(jwt= token)
                    return JsonResponse({'isUser':"yes" , "jwt":token})
                else :
                    return JsonResponse({'isUser':"no"})  
                
            ## Register
            elif len(json_data)>2 :
                em = json_data['email']
                pd = json_data['pwd']
                frstnm = json_data['firstname']
                lstnm = json_data['lastname']
                usrnm = json_data['username']
                if len(Customer.objects.filter(email=em))>0 :
                    return JsonResponse({'info':"exist"}) 
                else :
                    token = jwt.encode({"email":em , "brr":str(datetime.datetime.now())}, key='secret')
                    Customer.objects.create(email=em , pwd=pd , jwt=token , frstname=frstnm , lstname=lstnm , usrname=usrnm )
                    
                    return JsonResponse({'info':"new" , 'jwt':token})

        except :
            return HttpResponseNotFound("Brr")  
    else :
        return HttpResponseNotFound("Brr")    



@csrf_exempt 
def UpdateCommands(request) :
    serializer_class = CustomerSerializer
    
    if request.method == 'POST':
        try: 
            json_data = json.loads(request.body ) 
            print(json_data['date'])
            
            jwwt =  json_data['jwt']
            cmds  = Customer.objects.get(jwt=jwwt).commands + '//' +json_data['cmds'] + '|' + json_data['date'] + '|' + json_data['adrs']

            usr = Customer.objects.filter(jwt=jwwt)
            
            usr.update(commands= cmds)


            return JsonResponse({'info':"mrboha" }) 
            

        except :
            print('ZML')
            return JsonResponse({'info':"error"}) 

@csrf_exempt 
def getUserCommandsByJwt(request) :
    if request.method == 'POST':
        try : 
            json_data = json.loads(request.body ) 
            jwwt =  json_data['jwt']
            cus = Customer.objects.filter(jwt=jwwt)
            if len(cus)>0 :
                cmds = cus[0].commands
                em = cus[0].email
                pwd = cus[0].pwd
                frnm = cus[0].frstname
                lstnm = cus[0].lstname
                usrnm = cus[0].usrname

                dates = [  a.split('|')[1] for a in cmds.split('//') if len(a)>2]   

                adrs = [  a.split('|')[2] for a in cmds.split('//') if len(a)>2]    
                
                ids =[[ b.split(',')[-1] for b in a.split('@')[:-1] ] for a in  [ a.split('|')[0]  for a in cmds.split('//') if len(a)>2]  ] 
                # print(ids)
                brb = [[ b.split(',')[1:-1] for b in a.split('@')[:-1] ] for a in  [ a.split('|')[0]  for a in cmds.split('//') if len(a)>2]  ]
                
                src = []

                for i in range(len(ids)) :
                    res=[]
                    for j in range(len(ids[i])) :
                        try :
                            cus = Bapz.objects.filter(id=ids[i][j])[0].productname
                            prc = Bapz.objects.filter(id=ids[i][j])[0].price
                            rn = ''.join(cus.split(" "))
                            ch = []
                            for filename in os.listdir(DIR_BASE) :
                                cc = filename.split('.jpg')[0]
                                if cc[:-1] == rn : 
                                    ch.append(filename)
                            res.append([cus,sorted(ch)[0],prc]+brb[i][j])
                        except:
                            pass
                    src.append([dates[i],res,adrs[i]])

                
                return JsonResponse({'user':'yes', 'data':src, 'info':[em,pwd,frnm,lstnm,usrnm]}) 
            else : 
                return JsonResponse({'user':'no'}) 
        except :
            return JsonResponse({'info':'couldnt try','data':'-'}) 