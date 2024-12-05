from django.contrib import admin
from django.urls import path
#from rest_framework import routers
#from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
# from mac.views import authenticate
from mac import views


urlpatterns = [
    # path('', include(router.urls)),
    # path('authenticate', authenticate),
    # path('', include(msg_router.urls)),
    path('incidents/', views.incident_list),

]
