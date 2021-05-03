from rest_framework import serializers 
from activitys.models import Activity, Property, Survey

class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = Property
		fields = ['title', 'address', 'description', 'create_at', 'update_at', 'disabled_at', 'status']

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['property_id','schedule', 'title', 'create_at', 'update_at', 'status']

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey
		fields = ['activity_id', 'answers', 'create_at']