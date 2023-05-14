I have done Question 1 B Part.

Question 1 A part is incomplete.

# Web Scraping Project

This program scraps useful data from (https://itc.gymkhana.iitb.ac.in/wncc/soc/) which includes SoC Project Database.

To use this program, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

The following libraries are required to run this program:

beautifulsoup4
requests
pandas
xlsxwriter

You can install these libraries using pip. Open a terminal and enter the following command:

'''
pip install beautifulsoup4 requests pandas xlsxwriter
'''

This program will create a DataFrame using the Pandas library, It includes useful data such as:
1) Name of project
2) Mentors 
3) Number of mentees allowed
4) Link to each project

The program saves the extracted and cleaned data in a xlsx file format. You can share this file with others or use it for further analysis.
