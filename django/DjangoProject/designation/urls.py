from django.urls import path
from .views import *

urlpatterns = [
    path('designation/', DesignationView.as_view(), name='add designation'),
    path('designation/', DesignationView.as_view(), name='get all designation'),
    path('designation/<int:id>/', DesignationDetailViewBYID.as_view(), name='designation-detail'),
    path('designation/<int:id>/', DesignationDetailViewBYID.as_view(), name='delete designation'),
]