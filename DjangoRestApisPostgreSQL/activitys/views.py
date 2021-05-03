from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import Activity, Property, Survey
from .serializers import ActivitySerializer, PropertySerializer, SurveySerializer
from rest_framework.decorators import api_view
import json
from datetime import date

# Create your views here.
@api_view(["GET"])
def welcome(request):
  content = { 'message': 'Welcome Activitys App!' }
  return JsonResponse(content, status=200)

@api_view(["GET"])
def list_activitys(request):
  propertys = Property.objects.filter()
  serializer = PropertySerializer(propertys, many=True)
  return JsonResponse({'Activitys': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_activitys(request):
  payload = json.loads(request.body)  
  
  act = Property.objects.filter(schedule=payload["schedule"])
  if( act.count() > 1):
    return JsonResponse({'activity': "Ya esta registrada la fecha"}, safe=False, status=status.HTTP_200_OK)

  propertyc = Property.objects.create(
    title = payload["title"],
    address = payload["address"],    
    description = payload["description"],
    schedule = payload["schedule"],
    create_at = date.today(),
    update_at = date.today(),
    disabled_at = date.today(),
    status = payload["status"],
  )
  serializerproperty= PropertySerializer(propertyc)
  """
  activity = Activity.objects.create(
    property_id = propertyc.id,
    schedule = payload["schedule"],    
    title = payload["title"],
    create_at = date.today(),
    update_at = date.today(),
    status = payload["status"],
  )
  serializeractivity = ActivitySerializer(activity)

  
  survey = Survey.objects.create(
    activity_id = serializeractivity.id,
    answers = payload["answers"],    
    create_at = date.today()
  )
  serializersurvey = SurveySerializer(survey)
  """
  return JsonResponse({'Activity': serializerproperty.data}, safe=False, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def update_activitys(request, activity_id):
  payload = json.loads(request.body)
  try:
    property_item = Property.objects.filter(id=activity_id)      
    
    property_item.update(
      title = payload["title"],
      address = payload["address"],    
      description = payload["description"],
      schedule = payload["schedule"],    
      update_at = date.today(),
      disabled_at = date.today(),
      status = payload["status"],
    )
    propertys = Property.objects.get(id=activity_id)
    serializer = PropertySerializer(propertys)    
    """
    activity_item = Activity.objects.filter(id=property_id)   
    activity = Activity.objects.update(
      property_id = propertyc.id,
      schedule = payload["schedule"],    
      title = payload["title"],
      create_at = date.today(),
      update_at = date.today(),
      status = payload["status"],
    )
    serializeractivity = ActivitySerializer(activity)
    survey_item = Survey.objects.filter(id=property_id)   
    survey = Survey.objects.create(
      activity_id = survey_item.id,
      answers = payload["answers"],    
      create_at = date.today()
    )
    serializersurvey = SurveySerializer(survey)
    """
    return JsonResponse({'activity': serializer.data}, safe=False, status=status.HTTP_200_OK)
  except Exception:
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_activitys(request, activity_id):  
  try:
    property_item = Property.objects.filter(id=activity_id)      
    if(property_item.count() = 0):
      return JsonResponse({'activity': 'dont found'}, safe=False, status=status.HTTP_200_OK)
    property_item.delete()    
    return JsonResponse({'delete activity': 'ok'}, safe=False, status=status.HTTP_200_OK)
  except Exception:
    return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)