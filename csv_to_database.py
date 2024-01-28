import os
import sys
import csv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_manager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def import_csv_into_database(file_path,Mclass):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Mclass.objects.create(
                job_title=row['Job_Title'],
                company_name=row['Company_name'],
                job_location=row['Job_location'],
                company_experience=row['Company_Experience'],
                job_skills=row['Job_skills']
            )

if __name__ == '__main__':
    main()
    
    from_path = "C:\\projects\\mini_project\\project_manager\\skill_matcher\\data\\csv"
    relative_path = "C:\\projects\\mini_project\\project_manager\\"

    csv_file_path = []

    # Get all files ending with .csv in from_path
    for root, dirs, files in os.walk(from_path):
        for file in files:
            if file.endswith(".csv"):
                # Build the relative path
                relative_file_path = os.path.relpath(os.path.join(root, file), relative_path)
                csv_file_path.append(relative_file_path)

    # Sort the list of CSV file paths
    csv_file_path.sort()

    # Print or use the list as needed
    print("List of CSV file paths:")
    for path in csv_file_path:
        print(path)
    
    from skill_matcher.models import AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job
    class_list = [AI_Job,Cloud_Job,Cognitive_Job,Data_Science_Job,Education_Job,Engineering_Job,IOT_Job,IT_Job,ML_Job,Pharma_Job]
    
    for s_class in class_list:
        print(s_class)
    
    if not input("Want To Continue? Press Yes To Continue. Any other Response will terinate execution. :: ").lower() == "yes".lower():
        sys.exit()
    print("Will Continue Execution...")
    
    if len(csv_file_path) == len(class_list):
    # Iterate through both lists simultaneously
        for csv_path, i_class in zip(csv_file_path, class_list):
            import_csv_into_database(csv_path, i_class)
    else:
        print("Number of items in csv_file_path and class_list is not the same. Skipping the iteration.")
    
    print("Done")
    # from skill_matcher.models import 
    # class_list = []
    # for i_class in class_list :
    #     import_csv_into_database(csv_file_path[12],i_class)