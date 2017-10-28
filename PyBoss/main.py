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

## reformat DOB in a new list
new_DOB_list = []
for DOB in employee_df['DOB']:
    year = DOB[0:4]
    month = DOB [5:7]
    day = DOB[8:10]
    new_DOB_list.append('%s/%s/%s' % (day, month, year))

## switch out the old DOB for the new list
employee_df['DOB'] = new_DOB_list

print(employee_df)
