from django.urls import path
from . import views

urlpatterns = [
   	path('', views.index, name='approvalzlist'),
    path('details/', views.details, name='approvaldetail'),
    path('details/approvaltracking/', views.tracking, name='approvaldetail'),
    path('logout', views.logout, name='logout'),
    
    #path('<int:approvalDetail_id>', views.details, name='listing'), #views.listing refers to the listing method.

    #first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
]