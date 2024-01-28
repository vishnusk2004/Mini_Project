from django.db import models

# Create your models here.
class AI_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "AI"
    
class Cloud_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Cloud"

class Cognitive_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Cognitive"

class Data_Science_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Data Science"

class Education_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Education"

class Engineering_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Engineering"
    
class IOT_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "IOT"
    
class IT_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "IT"
    
class ML_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "ML"
    
class Pharma_Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    company_experience = models.CharField(max_length=255)
    job_skills = models.JSONField()
    def __str__(self):
        return "Pharma"