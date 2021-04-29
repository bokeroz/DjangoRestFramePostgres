from rest_framework import serializers 
from activitys.models import Activity
"""
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')
"""

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = '__all__'

"""
class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = Property
		fields = '__all__'



class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey
		fields = '__all__'
"""