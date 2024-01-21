import csv

# Read data from csv file
jobs = []
with open('it_job_list_naukri.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        jobs.append({
            "job_title": row["Job_Title"],
            "company_name": row["Company_name"],
            "experience": row["Company_Experience"],
            "location": row["Job_location"],
            "skills_needed": row["Job_skills"].strip("['").strip("']").split(",")  # Adjusted skill splitting
        })
# user skill
user_skills = ['python', 'java', 'Computer Networking', 'c', 'Cpp']

#iterate and give the matching job
matched_companies = []
for job in jobs:
    job_skills = job['skills_needed']
    matched_skills = [skill for skill in user_skills if skill.lower() in ' '.join(job_skills).lower()]
    match_count = len(matched_skills)
    if matched_skills:
        matched_companies.append({
            "company_name": job["company_name"],
            "job_title": job["job_title"],
            "matched_skills": matched_skills,
            "match_count": match_count
        })

for company in sorted(matched_companies, key=lambda x: x['match_count'], reverse=True):
    print(f"Company Name: {company['company_name']}")
    print(f"Job Title: {company['job_title']}")
    print(f"Matched Skills: {', '.join(company['matched_skills'])}")
    print(f"match count: {company['match_count']} ")
    print()
