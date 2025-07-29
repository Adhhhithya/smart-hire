# hiring/admin.py
from django.contrib import admin
from .models import JobPosting, Candidate

admin.site.register(JobPosting)
admin.site.register(Candidate)
