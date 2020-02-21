import os
import csv
#importing datetime for date format conversion
import datetime

# Set variable for input file, which is in Resources folder, 2 directories up from where the code is running
employee_data_csv = os.path.join("..","..","Resources", "employee_data.csv")

# Lists to store data
Employee_ID = []
FirstName = []
LastName = []
dob = []
Replaced_DOB = []
ReplacedSSN = []
state = []
state_code = []

with open(employee_data_csv, "r", encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #next row to skip reading the Header
    next(csvreader)
    for row in csvreader:
        # Add EmpID
        Employee_ID.append(row[0])
        # Add Name
        NewName = row[1].split(" ")
        FirstName.append(NewName[0])
        LastName.append(NewName[1])
        # Add dob
        dob.append(row[2])
        
        # Add ssn
        splitSSN = row[3].split("-")
        splitSSN[0] = '***-'
        splitSSN[1] = '**-'
        ReplacedSSN.append(splitSSN[0]+splitSSN[1]+splitSSN[2])
        
        # Add State
        state.append(row[4])
    us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
            }
    #looping through state and looking up in dictionary to get the 2 letter code
    for i in state:
        state_two_letter = us_state_abbrev[i]
        state_code.append(state_two_letter)  
    
    #looping through dob and converting the format to mm/dd/yy
    for j in dob:
        NewDOB = datetime.datetime.strptime(j, '%Y-%m-%d').strftime('%m/%d/%Y')  
        Replaced_DOB.append(NewDOB)    

# Zip lists together
cleaned_csv = zip(Employee_ID, FirstName, LastName, Replaced_DOB, ReplacedSSN, state_code)
# Set variable for output file
output_file = "Employee_data_cleanedup.csv"

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["EmpID", "First Name", "Last Name", "DOB","SSN", "State"])
    # Write in zipped rows
    writer.writerows(cleaned_csv)