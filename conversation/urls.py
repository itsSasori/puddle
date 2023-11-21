from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns=[
    path('new-conversations/<str:pk>/',views.new_conversation,name="new-conversation"),
    path('conversations-detail/<str:pk>/',views.conversation_detail,name="conversation-detail"),
    path('inbox/',views.inbox,name="inbox")
  
]