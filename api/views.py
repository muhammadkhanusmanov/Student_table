from django.http import HttpRequest,JsonResponse
from django.views import View
from .models import Subject,Student
import json

# Create your views here.

class StudentView(View):
    def get(self,request:HttpRequest):
        students=Student.objects.all()
        result={}
        for student in students:
            result[student.id]=[{'student_name':student.name}]
            subjects=Subject.objects.filter(rating=student)
            for subject in subjects:
                result[student.id].append({'subject_name':subject.name,'rating':subject.rate})
        return JsonResponse(result)
    def post(self,request:HttpRequest):
        data=request.body.decode()
        data=json.loads(data)
        name=data.get('name',None)
        try:
            student=Student.objects.create(name=name)
            student.save()
            return JsonResponse({'result':'Created','id':student.id})
        except:
            return JsonResponse({'result':'Failed'})

class SubjectView(View):
    def get(self,request:HttpRequest):
        subjects=Subject.objects.all()
        result={}
        for subject in subjects:
            if not subject.name in result.keys():
                result[subject.name]=[]

        for subject in subjects:
            result[subject.name].append({'student_id':subject.rating.id,'stdent_name':subject.rating.name,'rating':subject.rate})
        return JsonResponse(result)
    def post(self,request:HttpRequest):
        data=request.body.decode()
        data=json.loads(data)
        name=data.get('name',None)
        students=data.get('students',[])
        for student in students:
            id=student.get('id',None)
            rate=student.get('rating',None)
            try:
                sdnt=Student.objects.get(id=id)
                subject=Subject.objects.create(name=name,rate=rate,rating=sdnt)
                subject.save()
            except:
                return JsonResponse({'result':'Bad Request'})
        return JsonResponse({'result':'Created'})

class SearchView(View):
    def get(self,request:HttpRequest,id:int):
        try:
            student=Student.objects.get(id=id)
            subjects=Subject.objects.filter(rating=student)
            result=[{'id':student.id, 'name':student.name}]
            for subject in subjects:
                result.append({'subject':subject.name,'rating':subject.rate})
            return JsonResponse({'result':result})
        except:
            return JsonResponse({'result':'Bad Request'})

        
        
    
