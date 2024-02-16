from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=30, null=True)
    usermail = models.EmailField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    bio = models.TextField(blank=True, null=True)  # Allow null values

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'

        

class Candidate(models.Model):
    APPLIED_FOR = (
        ("Front-end developer", "Front-end developer"),
        ("Back-end developer", "Back-end developer"),
        ("Fullstack developer", "Fullstack developer"),
        ("SQL developer", "Fullstack developer"),
        ("HR Trainee", "HR Trainee")
    )

    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    resume = models.FileField(upload_to='pdfs/', null=False)
    position = models.CharField(max_length=50, choices=APPLIED_FOR)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
   
class Interview(models.Model):

    INTERVIEW_STATUS = (
        ('Interviewed', 'Interviewed'),
        ('Not Interviewed', 'Not Interviewed'),
        ('Interview scheduled', 'Interview scheduled'),
        ('Selected', 'Selected'),
        ('Not-selected', 'Not-selected'),
        ('Action-pending', 'Action-pending'),
    )

    POSITION = (
        ("Front-end developer", "Front-end developer"),
        ("Back-end developer", "Back-end developer"),
        ("Fullstack developer", "Fullstack developer"),
        ("SQL developer", "Fullstack developer"),
        ("HR Trainee", "HR Trainee")
    )

    name = models.ForeignKey(Candidate,null=True, on_delete=models.SET_NULL)
    interview_date = models.DateField(null=True)
    position = models.CharField(max_length=30, null=True, choices=POSITION)
    interviewer = models.CharField(max_length=50, null=True)
    interview_status = models.CharField(max_length=30, null=True, choices=INTERVIEW_STATUS)
    feedback = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.position
    

    
class OFFERS_DETAILS(models.Model):

    OFFER= ( 
        ('OFFER ACCEPTED', 'OFFER ACCEPTED'),
        ('OFFER REJECTED', 'OFFER REJECTED') 
        )

    name = models.ForeignKey(Candidate,null=True, on_delete=models.SET_NULL)
    position = models.ForeignKey(Interview,max_length=30, null=True, on_delete=models.SET_NULL)
    offers = models.CharField(max_length=30,null=True,choices=OFFER)

class VACANCIES(models.Model):

    ROLE = (
        ("Front-end developer", "Front-end developer"),
        ("Back-end developer", "Back-end developer"),
        ("Fullstack developer", "Fullstack developer"),
        ("SQL developer", "Fullstack developer"),
        ("HR Trainee", "HR Trainee")
        )
    role = models.CharField(null=True,max_length=30,choices=ROLE)
    Vacancies = models.CharField(max_length=10,null=True)
    Locations = models.CharField(max_length=50,null=True)
    Experience = models.CharField(max_length=30,null=True)
    skills = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.role

