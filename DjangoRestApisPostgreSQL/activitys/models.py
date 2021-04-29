from django.db import models

"""
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
"""

class Activity(models.Model):
    ide =  models.IntegerField()
    property_id = models.IntegerField()
    schedule = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_at = models.CharField(max_length=255)
    update_at = models.CharField(max_length=255)  
    status = models.CharField(max_length=255)


"""
class Property(models.Model):
    ide = models.IntegerField()
    title = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)



class Survey(models.Model):
    activity_id = models.IntegerField()
    answers = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
"""    