# from django.urls import path

from django.urls import path
from .views import addtask, getalltask, updatetask, deltask


urlpatterns = [
    path('addtask/',addtask),
    path('getalldata/', getalltask),
    path('updatedata/', updatetask),
    path('deldata/', deltask),

]