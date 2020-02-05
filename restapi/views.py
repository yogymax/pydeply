from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from restapi.serialization import StudentSer
from restapi.models import Student

#`create() -- POST`, `retrieve()--GEt single`, `update()--put`,`partial_update() --patch`, `destroy()--delete` and `list() -- get all
class StudentOperations(ModelViewSet): #6--uri
    queryset = Student.objects.all()
    serializer_class = StudentSer