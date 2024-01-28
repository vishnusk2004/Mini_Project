from django.contrib import admin

# Register your models here.
from .models import AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job

classes_list = [AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job]

for i_class in classes_list:
    admin.site.register(i_class)