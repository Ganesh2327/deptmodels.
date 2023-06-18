from django.db import models

# Create your models here.
class DEPT(models.Model):
    Dname=models.CharField(max_length=100,primary_key=True)
    deptno=models.IntegerField()
    loc=models.CharField(max_length=100)

class EMP(models.Model):
    ename=models.CharField(max_length=100)
    deptno=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    empno=models.IntegerField()
