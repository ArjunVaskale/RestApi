from django.db import models

from django.core.serializers import serialize

from django.conf import settings

import json 



def upload_update_image(instance , filename):
    return "updates/{user}/{filename}".format(user = instance.user , filename = filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #      qs = self 
    #      return serialize('json' , qs , fields=('user' , 'content' , 'image') )

    #  def serialize(self):
    #      qs = self 
    #      final_array = [] 
    #      print('innner')
    #      for obj in qs:
    #          stuct = json.loads(obj.serialize())
    #          final_array.append(stuct)
    #      print('innner')
    #      return json.dumps(final_array)


         def serialize(self):
             list_values = list( self.values('user' ,'content' , 'image') )
             print( list_values )
             return json.dumps(list_values)
      

class UpdateManager(models.Manager):
    def get_queryset(self):
        print('called update manager')
        return UpdateQuerySet(self.model , using = self._db)



class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    content     = models.TextField( blank = True , null = True)
    image       = models.ImageField(upload_to = upload_update_image , blank = True , null = True)
    updated   = models.DateTimeField(auto_now = True)
    timestamp   = models.DateTimeField(auto_now_add = True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""


    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ''       
        data = {
            "content" : self.content,
            "user" : self.user.id ,
            "image" : image ,
        }
       

        data = json.dumps(data)
    
        return data
