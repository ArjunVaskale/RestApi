from django.shortcuts import render

from django.core.serializers import serialize

from django.http import JsonResponse , HttpResponse 

import json 

from restapi. mixins import JsonResponseMixin

from django.views.generic import View

from .models import Update

def json_example_view(request):
    data = {
        "count": 100  ,
        "content" : "some content message",
    }
    #return JsonResponse(data)
    json_data = json.dumps( data )
    
    return HttpResponse(json_data ,content_type = 'application/json')

class JsonCBV(View):
    def get(self , request , *args , **kwargs):
        data = {
        "count": 100 ,
        "content" : "some content message",
        }
        return JsonResponse(data)



class JsonCBV2( JsonResponseMixin ,View):
    def get(self , request , *args , **kwargs):

        data = {
            "count": 100 ,
            "content" : "some content message",
        }
        return self.render_to_Json_response(data)



class SerializedDetailView( JsonResponseMixin ,View):
    def get(self , request , *args , **kwargs):
        obj = Update.objects.get(id = 2 )
        # data = serialize("json" , [obj] , fields=('user' , 'content'))
        # json_data = data

        # data = {
        #     "user" : obj.user.username , 
        #     "content" : obj.content ,
        # }
        # json_data = json.dumps(data)
        json_data = obj.serialize()

        return HttpResponse(json_data ,content_type = 'application/json')



class SerializedListView( JsonResponseMixin ,View):
    def get(self , request , *args , **kwargs):
        #qs = Update.objects.all()
        # data = serialize("json" , qs , fields=('user' , 'content'))
        # json_data = data  
        # print(data)

        # data = {
        #     "user" : obj.user.username , 
        #     "content" : obj.content ,
        # }
        # json_data = json.dumps(data)


        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data , content_type = 'application/json')