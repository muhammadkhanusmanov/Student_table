from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=50)
    rate=models.IntegerField(default=0, blank=True)
    rating=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.rating.name}'

