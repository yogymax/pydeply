from sections.models import Student

class StudentCrudOp:

    @staticmethod
    def get_list_students():
        return Student.objects.all().filter(active='Y').all()

    @staticmethod
    def get_single_student(stid):
        sts = Student.objects.filter(id=stid,active='Y')
        if len(sts)>0:
            return sts[0]

    @staticmethod
    def get_dummy_student():
        return Student(id=0,studName='',studFees=0.0,studAddress='',studAge=0)

    @staticmethod
    def delete_student(stid):
        dbst = StudentCrudOp.get_single_student(stid)
        if dbst:
            #dbst.delete()
            dbst.active='N'
            dbst.save() #update
            return "Record Removed..!"
        else:
            return "Cannot delete as no record...!"

    @staticmethod
    def save_update_student(stud):
        dbst = StudentCrudOp.get_single_student(stud.id)
        stud.save()
        if dbst:
            return 'Record Updated'
        else:
            return "Record Added"
