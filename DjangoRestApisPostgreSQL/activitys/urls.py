from django.conf.urls import url 
from django.urls import include, path
from activitys import views 

urlpatterns = [ 
    url(r'^api/welcome$', views.welcome),
    url(r'^api/activitys$', views.list_activitys),
    url(r'^api/activitys/create$', views.create_activitys),    
    path('api/activitys/update/<int:activity_id>', views.update_activitys),
    path('api/activitys/delete/<int:activity_id>', views.delete_activitys),
]
