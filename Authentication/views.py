from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Task
# Create your views here.
import datetime

@api_view(['POST'])
def addtask(request):
    try:
        print ("request.data: "), request.data
        addob =Task(**request.data)
        addob.created_date = datetime.datetime.now()
        addob.save()
        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def getalltask(request):

     print ("getting all data")
     data = Task.objects.all().values()

     return Response(data)


@api_view(['PUT'])
def updatetask(request):
    try:
        mobile_number = request.data['mobile_number']
        Employee_Id = request.data['id']
        task=Task.objects.get(Employee_Id=Employee_Id)
        task.mobile_number=mobile_number
        task.save()
        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print (e)

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def deltask(request):
    Employee_Id = request.data['id']
    print ("id is", Employee_Id)
    d = Task.objects.filter(id=Employee_Id)
    d.delete()
    return Response("Deleted")