import json

    # 1. Open your saved file
with open("all_jobs.json", "r") as file:
        jobs = json.load(file)

    # 2. Set up our counters
total_jobs = len(jobs)  # This counts how many total jobs are in the list
unlocked_links = 0      # We will start our count at zero

    # 3. Look at every single job, one by one
for job in jobs:
        # If the link is NOT 'None', it means we got a real link!
        if job['posts_link'] != None:
            unlocked_links = unlocked_links + 1

    # 4. Print the final results
print("Total jobs grabbed:", total_jobs)
print("Unlocked jobs with real links:", unlocked_links)