from django.urls import path
from . import views

urlpatterns = [
   	#first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
       
    path('logout', views.logout, name='logout'),

    #path('<int:listing_id>', views.listing, name='listing'),
]