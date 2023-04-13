from django.views import View
from django.http import HttpRequest,JsonResponse
from .models import Student,Subject
import json


# Create your views here.
class StudentView(View):
    def get(self,request:HttpRequest):
        subjects=Subject.objects.all()
        result={}
        for subject in subjects:
            students=Student.objects.filter(rating=subject)
            result[subject.name]=[]
            for student in students:
                result[subject.name].append({'student_name':student.name,'rate':student.rate})
        return JsonResponse(result)
    def post(self,request:HttpRequest):
        data = request.body.decode()
        data=json.loads(data)
        name=data.get('name')
        rate=data.get('rate')
        sub=data.get('subject_id')
        try:
            subject=Subject.objects.get(id=sub)
            student=Student.objects.create(name=name,rate=rate,rating=subject)
            student.save()
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success':False})
class SubjectView(View):
    def post(self, request:HttpRequest):
        data=request.body.decode()
        data=json.loads(data)
        name=data.get('name')
        try:
            subject=Subject.objects.get(name=name)
            return JsonResponse({'success':'This subject has created already'})
        except:
            subject=Subject.objects.create(name=name)
            subject.save()
            return JsonResponse({'success':True})
    
        
