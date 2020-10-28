from django.views.generic import View 

from django.http import HttpResponse

from updates.models import Update as UpdateModel

from .mixins import CSRFExemptMixin

from restapi.mixins import HttpResponseMixin 

import json 



class UpdateModelDetailAPIViews(HttpResponseMixin ,CSRFExemptMixin ,View):

    is_json = True

    def get( self  , request , id , *args , **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize() 
        return self.render_to_response(json_data)

    def post( self  , request , *args , **kwargs):
        json_data = {}
        return self.render_to_response(json_data)


    def put( self  , request , *args , **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete( self  , request , *args , **kwargs):
        json_data = {}
        return self.render_to_response(json_data , status = 403)
 
class UpdateModelListAPIViews(HttpResponseMixin ,CSRFExemptMixin ,View):


    is_json = True


    def get( self  , request , *args , **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize() 
        return self.render_to_response(json_data)

    def post( self, request, *args, **kwargs):
        data = json.dumps({"message": "unknown data "})
        return self.render_to_response(data , status= 400)

    def delete( self  , request , *args , **kwargs):
        data = json.dumps({"message": "You can't delete data "})
        return self.render_to_response(data , status= 403)
