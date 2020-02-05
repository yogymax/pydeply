from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from restapi.models import Student


class StudentSer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   #all --json
        #fields = ('active','salary') #only given
        #exclude = ('active','salary') #only excluding
