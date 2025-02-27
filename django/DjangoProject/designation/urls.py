from django.urls import path
from .views import *

urlpatterns = [
    path('designation/', DesignationView.as_view(), name='add and get designation'),
    path('designation/<int:id>/', DesignationDetailViewBYID.as_view(), name='get and delete designation bassed on id'),
]