from django.urls import path
from . import views

urlpatterns = [
   	#first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
       
    #path('<int:patches_id>', views.index, name='patchlizt'),
    
    #este es el dashboard prototipo (patchList.html)
    #path('', views.index, name='patchlizt'),
]