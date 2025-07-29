# hiring/models.py

from django.db import models
from django.utils import timezone  # To set a default posting date

class JobPosting(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Candidate(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    # You can add more fields later like graduation_year, major, etc.

    def __str__(self):
        return self.full_name
