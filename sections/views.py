from django.shortcuts import render
from sections.servicecode import StudentCrudOp as service
from sections.models import *
#from django.views.generic import View
'''
class EmpOperations(View):

    def get(self,req):
        print(req.GET)
        print(req.POST)
        print(req.path)
        if "edit" in req.path:

            return render(req, 'student.html',
                          {
                              "students": service.get_list_students(),
                              "student": service.get_single_student(int(req.path.split("/")[-1]))
                          }
                          )
        elif "delete" in req.path:
            msg = service.delete_student(int(req.path.split("/")[-1]))
        return render(req, 'student.html',
                      {
                          "students": service.get_list_students(),
                          "student": service.get_dummy_student()
                      }
                      )

    def post(self,req):
        msg = ''
        if req.method == 'POST':
            keyval = req.POST
            stud = Student(id=keyval['stid'], studName=keyval['stnm'], studAge=keyval['stage'],
                           studAddress=keyval['stadr'], studFees=keyval['stfees'])
            msg = service.save_update_student(stud)

        return render(req, 'student.html',
                      {
                          "actionmsg": msg,
                          "students": service.get_list_students(),
                          "student": service.get_dummy_student()
                      }
                      )

'''

def generic_student_return(req,id=0,dummy=True,msg=None):
    stud = service.get_dummy_student()
    if dummy==False:
        stud=service.get_single_student(id)
    return render(req,'student.html',
                  {
                     "students": service.get_list_students(), #table info
                     "student" : stud, # to bind with form data
                      "studflag" : 1, # which form to showcase -1Yes
                      "courseflag" : 0, # which form to showcase - 0No
                      'deptflag':0,
                      'courselist' : Course.objects.all().filter(active='Y'), #student can select course
                      "depts" : Dept.objects.all().filter(active='Y')
                  }
                  )

def persit_student_info(req):
    print('inside persist student info..')
    msg = ''
    if req.method =='POST':
        keyval = req.POST
        #subjs = req.POST.getlist('studcrs')
        #print('subjs--', subjs)
        stud = Student(id=keyval['stid'],studName=keyval['stnm'],studAge=keyval['stage'],studAddress=keyval['stadr'],studFees=keyval['stfees'])
        stud.deptref = Dept.objects.get(id=int(keyval['dept'])) #dept
        msg = service.save_update_student(stud) #student
        subjs = req.POST.getlist('studcrs')

        for subj in subjs: # 2,5,1
            stud.coursesref.add(Course.objects.get(id=int(subj)))
            stud.save() #update -- 3rd table entry

        print('subjs--',subjs)

    return generic_student_return(req,msg=msg)


def edit_student_page(req,stid):
    return generic_student_return(req,id=stid,dummy=False)

def delete_student_page(req,stid):
    msg = service.delete_student(stid)
    return generic_student_return(req,msg=msg)

def welcome_student_page(req):
   return generic_student_return(req)


#--------------------------------------------------------------
def generic_course_return(req,id=0,dummy=True,msg=None):
    course = Course.dummyCourse()
    if dummy==False:
        course=Course.objects.filter(id=id,active='Y')[0]
    return render(req, 'student.html',
                  {
                      "courses": Course.objects.all().filter(active='Y'),
                      "course": course,
                      "studflag": 0,
                      "courseflag": 1,
                      'deptflag':0,
                      "actionmsg" : None
                  }
                  )




def welcome_course_page(req):
    return generic_course_return(req)

def persit_course_info(req):
    msg = ''
    if req.method =='POST':
        keyval = req.POST
        cr = Course(id=keyval['crid'],subjName=keyval['crnm'],subjCode=keyval['crcode'])
        cr.save()
        msg = "Course Record Saved..!"
    return generic_course_return(req,msg)

def edit_course_page(req,crid):
    return generic_course_return(req,crid,False)

def delete_course_page(req,crid):
    cr = Course.objects.get(id=crid)
    msg = ''
    if cr:
        cr.active='N'
        cr.save()
        msg="Record removed..!"
    return generic_course_return(req,msg=msg)

#----------------------------------------------------------------
def generic_dept_return(req,id=0,dummy=True,msg=None):
    dept = Dept.dummy_dept()
    if dummy==False:
        dept=Dept.objects.filter(id=id,active='Y')[0]
    return render(req, 'student.html',
                  {
                      "depts": Dept.objects.all().filter(active='Y'),
                      "dept": dept,
                      "studflag": 0,
                      "courseflag": 0,
                      'deptflag':1,
                      "actionmsg" : None
                  }
                  )

def welcome_dept_page(req):
    return generic_dept_return(req)

def persit_dept_info(req):
    msg = ''
    if req.method =='POST':
        keyval = req.POST
        dp = Dept(id=keyval['dpid'],deptName=keyval['dpnm'],deptCode=keyval['dpcd'])
        dp.save()
        msg = "Dept Record Saved..!"
    return generic_dept_return(req,msg)

def edit_dept_page(req,dpid):
    return generic_course_return(req,dpid,False)

def delete_dept_page(req,dpid):
    dp = Dept.objects.get(id=dpid)
    msg = ''
    if dp:
        dp.active='N'
        dp.save()
        msg="Dept Record removed..!"
    return generic_dept_return(req,msg=msg)
