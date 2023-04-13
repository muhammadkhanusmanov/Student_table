from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    rate=models.IntegerField(default=0, blank=True)
    rating=models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.rating.name} {self.name}'
    

