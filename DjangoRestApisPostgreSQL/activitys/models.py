from django.db import models

class Activity(models.Model):
    property_id = models.IntegerField()
    schedule = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_at = models.CharField(max_length=255)
    update_at = models.CharField(max_length=255)  
    status = models.CharField(max_length=255)


"""
class Property(models.Model):
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