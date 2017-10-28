##* Importing employee data and converted the format as follows:
##
##  * The `Name` column should be split into separate `First Name` and `Last Name` columns.
##
##  * The `DOB` data should be re-written into `DD/MM/YYYY` format.
##
##  * The `SSN` data should be re-written such that the first five numbers are hidden from view.
##
##  * The `State` data should be re-written as simple two-letter abbreviations.


import os
import pandas as pd
import glob


## create a pandas dataframe to store the employee data
employee_df = pd.DataFrame()

## change directories to raw files
os.chdir('raw_data')


## read all csv files and merge them into on data frame
for csvpath in glob.glob('*.csv'):
    temp_employee_df = pd.read_csv(csvpath)
    employee_df = pd.concat([employee_df, temp_employee_df], ignore_index=True)

## split name into two columns 'First Name' and 'Last Name'
employee_df['First Name'], employee_df['Last Name'] = employee_df['Name'].str.split(' ', 1).str

## reorder column names and drop original name column
new_cols = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
employee_df = employee_df[new_cols]

## reformat DOB in a new list
new_DOB_list = []
for DOB in employee_df['DOB']:
    year = DOB[:4]
    month = DOB [5:7]
    day = DOB[8:10]
    new_DOB_list.append('%s/%s/%s' % (day, month, year))

## switch out the old DOB for the new list
employee_df['DOB'] = new_DOB_list

## hide the first 5 digits of employee SSNs
new_SSN_list = []
for SSN in employee_df['SSN']:
    SSN_last_4 = SSN[7:11]
    new_SSN_list.append('***-**-%s' % (SSN_last_4))

## switch out the old DOB for the new list
employee_df['SSN'] = new_SSN_list

## switch state names into state abbreviations

## state abbreviations dict
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
state_abbr_list = []
for State in employee_df['State']:
    state_abbr = us_state_abbrev[State]
    state_abbr_list.append(state_abbr)

## switch out the old DOB for the new list
employee_df['State'] = state_abbr_list

## save the new data to reformatted_employee_data.csv
savepath = os.path.join('..', 'reformatted_employee_data.csv')
employee_df.to_csv(savepath, index=False)
