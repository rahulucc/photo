from django.db import models

class image(models.Model):

    field_name = models.ImageField(upload_to='documents/')

