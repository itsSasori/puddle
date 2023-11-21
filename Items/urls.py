from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<str:pk>/',views.detail,name='detail'),
    path('new-items/',views.new_items,name='new-items'),
    path('dashboard/',views.dashboard,name='dashboard'),    
    path('delete-item/<str:pk>/',views.delete_items,name='delete-item'),    
    path('edit-item/<str:pk>/',views.edit_items,name='edit-item'),    
  
]