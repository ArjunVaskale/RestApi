from django.views.generic import View 

from django.http import HttpResponse

from updates.models import Update as UpdateModel

from .mixins import CSRFExemptMixin

import json 



class UpdateModelDetailAPIViews(CSRFExemptMixin ,View):
    def get( self  , request , id , *args , **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize() 
        return HttpResponse( json_data , content_type='application/json')

    def post( self  , request , *args , **kwargs):
        return HttpResponse( json_data , content_type='application/json')


    def put( self  , request , *args , **kwargs):
        return HttpResponse( json_data , content_type='application/json')

    def delete( self  , request , *args , **kwargs):
        return HttpResponse( json_data , content_type='application/json')

class UpdateModelListAPIViews(CSRFExemptMixin ,View):
    def get( self  , request , *args , **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize() 
        return HttpResponse( json_data , content_type='application/json')

    def post( self, request, *args, **kwargs):
        data = json.dumps({"message": "unknown data "})
        return HttpResponse( data , content_type='application/json' )

    def delete( self  , request , *args , **kwargs):
        data = json.dumps({"message": "You can't delete data "})
        return HttpResponse( data , content_type='application/json')