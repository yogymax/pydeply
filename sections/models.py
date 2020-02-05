from django.db import models


# Create your models here.
class Student(models.Model):
    studName = models.CharField('stud_name',max_length=100)
    studAge = models.IntegerField('stud_age')
    studFees = models.FloatField('stud_fees')
    studAddress = models.TextField('stud_adr',max_length=100)
    active = models.CharField('isactive',max_length=10,default='Y')
    deptref = models.ForeignKey('Dept',on_delete=models.CASCADE,related_name='studsref')

class Course(models.Model): #MM
    subjName = models.CharField('subj_name',max_length=50)
    subjCode = models.CharField('subj_code', max_length=50)
    active = models.CharField('isactive', max_length=10, default='Y')
    studentsref = models.ManyToManyField(Student,related_name='coursesref')

    @staticmethod
    def dummyCourse():
        return Course(id=0,subjName='',subjCode='')

class Dept(models.Model): #M-1 1M
    deptName = models.CharField('dept_name', max_length=50)
    deptCode = models.CharField('dept_code', max_length=50)
    active = models.CharField('isactive',max_length=10,default='Y')

    @staticmethod
    def dummy_dept():
        return Dept(id=0,deptName='',deptCode='')

class Address(models.Model):
    cityName = models.CharField('adr_city', max_length=50)
    pinCode = models.CharField('pin_code', max_length=50)
    active = models.CharField('isactive',max_length=10,default='Y')
    studref = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='adrref')
