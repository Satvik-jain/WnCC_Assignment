import sys
import subprocess
# implement pip as a subprocess:
# installing xlsxwriter package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xlsxwriter'])
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

URL = "https://itc.gymkhana.iitb.ac.in/wncc/soc/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

project = {}  # A dictionary with key as name of project and value is a list of [Mentor, no. of mentee, topic]

# Created a list of project URL named as project_url
project_url = soup.find_all("div", class_="rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white")
for i in range(71):
    project_url[i] = "https://itc.gymkhana.iitb.ac.in" + project_url[i]["href"]


# Now I have to surf through every url to get the name of the mentors and the number of mentees allowed.

def get_mentor_name(i):  # Here 'i' is the index project URL in the list project_url
    URL = project_url[i]
    page = requests.get(URL)
    indivisual_soup = BeautifulSoup(page.content, "html.parser")
    mentor = indivisual_soup.find("div", class_="col-sm-10 col-md-8").find_all("p", {"class": "lead"})
    mentee = mentor.pop(len(mentor) - 1).text
    index = 0
    for name in mentor:
        mentor[index] = name.text
        index += 1

    return mentor, mentee  # It returns the mentors as list and number of mentee as string


project_mentors = []
project_mentees = []
for i in range(71):
    mentor, mentee = get_mentor_name(i)
    project_mentors.append(mentor)
    project_mentees.append(mentee)


# Now project_mentors and project_mentees are the list of mentors and no. of mentees in a project


# Getting names of all the Projects
projects = soup.find_all("div", {"class": "col-lg-4 col-6 mb-4 shuffle-item"})
for i in range(71):
    projects[i] = projects[i].find("p").text

# Taking data frame as ProjectName, Mentors, number of mentees and Link.
# Creating a new data frame

df = pd.DataFrame()
for i in range(71):
    mentors = ", ".join(project_mentors[i])
    no_of_mentee = project_mentees[i]
    url = project_url[i]
    name = projects[i]

    df = df._append(
        pd.DataFrame({"Projects": name, "Mentors": mentors, "Number of mentees": no_of_mentee, "Link to project": url},
                     index=[0]), ignore_index=True)
df.index += 1
df.index.name = "S.No."
print(df)


# Creating xlsx (Excel) file
writer = pd.ExcelWriter('SOC_WEB_SCRAPING.xlsx', engine="xlsxwriter")

# Adding dataframe to the writer
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book
worksheet = writer.sheets['Sheet1']

new_format = workbook.add_format()
new_format.set_align('left')

# Applying new format to columns
worksheet.set_column('C:B', 40, new_format)
worksheet.set_column('C:D', 20, new_format)
worksheet.set_column('C:C', 40, new_format)
worksheet.set_column('C:E', 40, new_format)
writer._save()
