from django.db import models
from users.models import User

# Create your models here.

class EmployerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='empprofile')

    company_name=models.CharField(max_length=120,unique=True)
    logo=models.ImageField(upload_to='images')
    bio=models.CharField(max_length=120)
    services=models.CharField(max_length=120)
    location=models.CharField(max_length=120)


class Jobs(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='company')
    job_title=models.CharField(max_length=120)
    job_description=models.TextField()
    role=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(default=0)
    salary=models.PositiveIntegerField()
    location=models.CharField(max_length=120)
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True)
    qualification=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.job_title


class Application(models.Model):
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name='aapplicants')
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name='ajobs')
    options=(
        ('applied','applied'),
        ('rejected','rejected'),
        ('pending','pending'),
        ('cancelled','cancelled'),
        ('accepted','accepted')
    )
    status=models.CharField(max_length=20,choices=options,default='applied')
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=(
            'applicant','job'
        )

