from django.db import models

class Student(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    roll_no = models.CharField(max_length=100)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()

    def __str__(self):
        return self.name
