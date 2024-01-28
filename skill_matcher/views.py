from django.shortcuts import render
from skill_matcher.models import AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job
import re

matched = []

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')


def index(request):
    return render(request,'index.html')


def input(request):
    global matched
    matched = []
    Departments = [AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job]
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        # description = request.POST['Description']
        Skills = request.POST['Skills']
        experience = request.POST['experience']
        if request.POST['options-base'] == 'Male':
            gender = "Male"
        elif request.POST['options-base'] == 'Female':
            gender = "Female"
        dept = request.POST.get('department')
        location = request.POST['location']
        matched = match(firstName, lastName,Skills,experience,gender,dept,location,Departments)
        is_empty = not location == ""
        return render(request,'userinput.html',{"Departments":Departments,"isEmpty":is_empty})
    else:
        return render(request,'userinput.html',{"Departments":Departments})


def output(request):
    global matched
    if matched is not None:
        return render(request,'scriptoutput.html',{"matched" : matched})
    else:
        return render(request,'scriptoutput.html',)
    
def documentation(request):
    return render(request,'documentation.html')


def match(MfirstName, MlastName,MSkills,Mexperience,Mgender,Mdept,Mlocation,MDepartments):
    #For extracting data from database
    Database = []
    for Mclass in MDepartments:
        if Mdept == Mclass.__str__(Mclass):
            queryset = Mclass.objects.all()
            Database.extend(list(queryset.values()))
        if Mdept == "Other":
            queryset = Mclass.objects.all()
            Database.extend(list(queryset.values()))
    
    
    prefered_location = re.split(r',|/|\\', Mlocation)
    user_skills = MSkills.replace(", ",",").split(',')
    matched_companies = []
    matched_skills = []
    if Database is not None:
        for data in Database:
            job_experience = data["company_experience"].replace(' Yrs','').split('-')
            job_experience = [exp for exp in job_experience if exp]
            job_experience = [int(exp) for exp in job_experience]
            if job_experience:
                if job_experience[0] <= int(Mexperience) <= job_experience[1]:
                    job_location = data["job_location"].split(", ")
                    job_skills = punctuate(data["job_skills"]).split(", ")
                    matched_skills = [skill for skill in user_skills if skill.lower() in [job.lower() for job in job_skills]]
                    unmatched_skills = [skill for skill in user_skills if skill.lower() not in [job.lower() for job in job_skills]]
                    lacking_skills = [skill for skill in job_skills if skill.lower() not in [matched.lower() for matched in matched_skills]]
                    filtered_location = [Ulocation for Ulocation in prefered_location if Ulocation.lower() in [Jlocation.lower() for Jlocation in job_location]]
                    match_count = len(matched_skills)
                    unmatch_count = len(unmatched_skills)
                    lacking_skills_count = len(lacking_skills)
                    user_skill_count = len(user_skills)
                    if matched_skills:
                        matched_companies.append({
                            "company_name": data["company_name"],
                            "job_title": data["job_title"],
                            "matched_skills": matched_skills,
                            "unmatched_skills":unmatched_skills,
                            "match_count": match_count,
                            "unmatch_count": unmatch_count,
                            "match_percentage":((user_skill_count/(user_skill_count + lacking_skills_count))*100),
                            "Skills_lacking":lacking_skills,
                            "lacking_count":lacking_skills_count,
                            "lacking_percentage":((lacking_skills_count/(user_skill_count + lacking_skills_count))*100),
                            "user_skills":MSkills,
                            "user_skill_count":user_skill_count,
                            "filtered_location":filtered_location,
                            "Uexperience":Mexperience,
                            "company_experience":data["company_experience"]
                        })
    sorteddata = sorted(matched_companies, key=lambda x: x['match_count'], reverse=True)
    if not Mlocation == "":
        newdata = []
        for i in sorteddata:
            if not i["filtered_location"] == []:
                newdata.append(i)
        return newdata[:50]
    else:
        return sorteddata[:50]


def punctuate(extracted_text):
    punchuation = '''!()-[]{};:'"<>./?#$%&*_\\~'''
    for ele in extracted_text:
        if ele in punchuation:
            extracted_text = extracted_text.replace(ele, "")
    return extracted_text