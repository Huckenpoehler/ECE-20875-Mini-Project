import pandas
import csv
import matplotlib.pyplot as plt

''' 
The following is the starting code for path2 for data reading to make your first step easier.
'dataset_2' is the clean data for path1.
'''
dataset_2 = pandas.read_csv('NYC_Bicycle_Counts_2016.csv')
dataset_2['Brooklyn Bridge']      = pandas.to_numeric(dataset_2['Brooklyn Bridge'].replace(',','', regex=True))
dataset_2['Manhattan Bridge']     = pandas.to_numeric(dataset_2['Manhattan Bridge'].replace(',','', regex=True))
dataset_2['Williamsburg Bridge']  = pandas.to_numeric(dataset_2['Williamsburg Bridge'].replace(',','', regex=True))
dataset_2['Queensboro Bridge']    = pandas.to_numeric(dataset_2['Queensboro Bridge'].replace(',','', regex=True))
#print(dataset_2.to_string()) #This line will print out your data

# question 1
print("Sample Sizes:")
print('     Brooklyn Bridge: %10d' % sum(dataset_2['Brooklyn Bridge']))
print('     Manhattan Bridge: %10d' % sum(dataset_2['Manhattan Bridge']))
print('     Williamsburg Bridge: %d' % sum(dataset_2['Williamsburg Bridge']))
print('     Queensboro Bridge: %8d' % sum(dataset_2['Queensboro Bridge']))

# question 2
precip, precipTotal, clear, clearTotal, cool, coolTotal, warm, warmTotal = 0, 0, 0, 0, 0, 0, 0, 0

with open('NYC_Bicycle_Counts_2016.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if float(row['Precipitation']) > 0:
            precip += 1
            precipTotal += int(row['Total'].replace(',',''))
        else:
            clear += 1
            clearTotal += int(row['Total'].replace(',',''))
        if float(row['High Temp']) < 60:
            cool += 1
            coolTotal += int(row['Total'].replace(',',''))
        else:
            warm += 1
            warmTotal += int(row['Total'].replace(',',''))

print("\nAverage Cyclists:")
print("     Clear Day: %.2f" % float(clearTotal/clear))
print("     Rainy Day: %.2f" % float(precipTotal/precip))
print("     Warm Day: %9.2f" % float(warmTotal/warm))
print("     Cool Day: %9.2f" % float(coolTotal/cool))

# question 3
monB, monM, monW, monQ = 0,0,0,0
tueB, tueM, tueW, tueQ = 0,0,0,0
wedB, wedM, wedW, wedQ = 0,0,0,0
thuB, thuM, thuW, thuQ = 0,0,0,0
friB, friM, friW, friQ = 0,0,0,0
satB, satM, satW, satQ = 0,0,0,0
sunB, sunM, sunW, sunQ = 0,0,0,0

with open('NYC_Bicycle_Counts_2016.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row['Day'] == 'Monday':
            monB += int(row['Brooklyn Bridge'].replace(',',''))
            monM += int(row['Manhattan Bridge'].replace(',',''))
            monW += int(row['Williamsburg Bridge'].replace(',',''))
            monQ += int(row['Queensboro Bridge'].replace(',',''))
        elif row['Day'] == 'Tuesday':
            tueB += int(row['Brooklyn Bridge'].replace(',',''))
            tueM += int(row['Manhattan Bridge'].replace(',',''))
            tueW += int(row['Williamsburg Bridge'].replace(',',''))
            tueQ += int(row['Queensboro Bridge'].replace(',',''))
        elif row['Day'] == 'Wednesday':
            wedB += int(row['Brooklyn Bridge'].replace(',',''))
            wedM += int(row['Manhattan Bridge'].replace(',',''))
            wedW += int(row['Williamsburg Bridge'].replace(',',''))
            wedQ += int(row['Queensboro Bridge'].replace(',',''))
        elif row['Day'] == 'Thursday':
            thuB += int(row['Brooklyn Bridge'].replace(',',''))
            thuM += int(row['Manhattan Bridge'].replace(',',''))
            thuW += int(row['Williamsburg Bridge'].replace(',',''))
            thuQ += int(row['Queensboro Bridge'].replace(',',''))
        elif row['Day'] == 'Friday':
            friB += int(row['Brooklyn Bridge'].replace(',',''))
            friM += int(row['Manhattan Bridge'].replace(',',''))
            friW += int(row['Williamsburg Bridge'].replace(',',''))
            friQ += int(row['Queensboro Bridge'].replace(',',''))
        elif row['Day'] == 'Saturday':
            satB += int(row['Brooklyn Bridge'].replace(',',''))
            satM += int(row['Manhattan Bridge'].replace(',',''))
            satW += int(row['Williamsburg Bridge'].replace(',',''))
            satQ += int(row['Queensboro Bridge'].replace(',',''))
        else:
            sunB += int(row['Brooklyn Bridge'].replace(',',''))
            sunM += int(row['Manhattan Bridge'].replace(',',''))
            sunW += int(row['Williamsburg Bridge'].replace(',',''))
            sunQ += int(row['Queensboro Bridge'].replace(',',''))

plt.plot(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [monB/1000, tueB/1000, wedB/1000, thuB/1000, friB/1000, satB/1000, sunB/1000])
plt.plot(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [monM/1000, tueM/1000, wedM/1000, thuM/1000, friM/1000, satM/1000, sunM/1000])
plt.plot(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [monW/1000, tueW/1000, wedW/1000, thuW/1000, friW/1000, satW/1000, sunW/1000])
plt.plot(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [monQ/1000, tueQ/1000, wedQ/1000, thuQ/1000, friQ/1000, satQ/1000, sunQ/1000])
plt.xlabel('Day of Week')
plt.ylabel('Quantity of Bicyclists in Thousands')
plt.legend('BMWQ')
plt.title('Total Bicyclists Recorded between 1 April and 31 October\norganized by Day of Week')
plt.show()