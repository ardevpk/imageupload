from django.db import models
import os
# Create your models here.
# def getcurrentusername(instance, filename):
#     return "/{0}/{1}/".format(os.rename(filename, f"{instance.user}-{filename}"))
def getcurrentusername(instance, filename):
    file, ext = filename.split('.')
    if instance.user:
        return 'image/{}/{}.{}'.format(instance.user, file, ext)
    

class upload(models.Model):
    user = models.CharField(max_length=254)
    image = models.ImageField(upload_to=getcurrentusername)