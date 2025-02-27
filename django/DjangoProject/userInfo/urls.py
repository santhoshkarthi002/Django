from django.urls import path
from .views import *

urlpatterns = [
    path('userInfo/', UserInfoView.as_view()),
    path('userInfo/<int:id>/', UserInfoDetailViewBYID.as_view()),
    # path('designation/', designationView.as_view()),
]