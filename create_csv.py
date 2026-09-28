import json
import csv

    # 1. Open the JSON file you already saved
with open("all_jobs.json", "r") as json_file:
        jobs = json.load(json_file)

    # 2. Create a brand new CSV file
with open("jobs_report.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row (The column names at the top of the Excel sheet)
        columns = ["Company", "Location", "Category", "Salary", "Link Available", "Application Link"]
        writer.writerow(columns)

        # 3. Loop through the 100 jobs and write each one into the Excel sheet
        for job in jobs:
            # Check your rule: Is the link available? True or False
            if job['posts_link'] != None:
                link_available = True
            else:
                link_available = False

            # Prepare the row of data for this specific job
            row = [
                job.get('Company', 'No Name'),
                job.get('Location', 'No Location'),
                job.get('Category', ''),
                job.get('Salary', ''),
                link_available,              # Your custom True/False column!
                job.get('posts_link', '')    # The actual link (or blank if None)
            ]

            # Write the row to the file
            writer.writerow(row)
print("Success! Open your folder and double-click jobs_report.csv to see it in Excel.")