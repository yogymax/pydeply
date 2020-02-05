

''''''
#from sections.views import EmpOperations
'''
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from sections.views import *
urlpatterns = [
'''

#get post
'''
    path('student/save/',persit_student_info), #save or update - -welcome page
    path('student/edit/<int:stid>',edit_student_page),#fetch for edit
    path('student/delete/<int:stid>',delete_student_page), #delete - -soft
    path('student/welcome/',welcome_student_page), #welcome page

    path('course/save/', persit_course_info),  # save or update - -welcome page
    path('course/edit/<int:crid>', edit_course_page),  # fetch for edit
    path('course/delete/<int:crid>', delete_course_page),  # delete - -soft
    path('course/welcome/', welcome_course_page),  # welcome page

    path('dept/save/', persit_dept_info),  # save or update - -welcome page
    path('dept/edit/<int:dpid>', edit_dept_page),  # fetch for edit
    path('dept/delete/<int:dpid>', delete_dept_page),  # delete - -soft
    path('dept/welcome/', welcome_dept_page),  # welcome page
'''
    #url(r'^newemp/', EmpOperations.as_view(), name='emp_ops'),
#]
