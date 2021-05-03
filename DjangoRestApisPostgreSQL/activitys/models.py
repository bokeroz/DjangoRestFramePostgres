from django.db import models
from django.utils import timezone

class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Activity(models.Model):
    property_id = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()  
    status = models.CharField(max_length=35)

    def __str__(self):
        return self.schedule

class Survey(models.Model):
    activity_id = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    answers = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answers




  