from django.conf.urls import url 
from activitys import views 

urlpatterns = [ 
    #url(r'^api/tutorials$', views.tutorial_list),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/activitys$', views.list_activitys)
]