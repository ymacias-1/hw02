import csv
import matplotlib.pyplot as plt

#data for plot 1

rows1=[ ]
with open('Carbon Dioxide Emission Estimates.csv', 'r') as f:
    CarbonDioxideData=csv.reader(f)   
    for row in CarbonDioxideData:
      rows1.append(row)
  
#get years 
years1=[ ]
for row in rows1: 
  years1.append(row[2])
data_years=years1[18:26]

#get CO2 emissions data 
emissions=[ ]
for row in rows1: 
  emissions.append(row[4])
UnitedStates_emissions=sorted(emissions[3164:3172])
Canda_emissions=sorted(emissions[556:564])
'''
#plot figure 1 
xs=data_years
ys=Canda_emissions
zs=UnitedStates_emissions

fig, ax=plt.subplots()
ax.plot(xs, ys, label='Canada emissions')
ax.plot(xs, zs, label='UnitedStates emissions')
ax.tick_params(direction='out',length=10, width=2)
plt.xlabel('Year')
plt.ylabel('Emissions (thousand metric tons of carbon dioxide)')
plt.title('Comparision of CO2 emissions')
plt.legend()
plt.show()
'''

#data for plot 2 

rows2=[]
with open('Tourist Arrival and Expenditure.csv') as t: 
  TouristA_E=csv.reader(t)
  for row in TouristA_E: 
    rows2.append(row) 

#getting years 
years2=[]
for row in rows2: 
  years2.append(row[2])
Tourist_years=years2[2179:2185]

#getting number of tourist visits 
num_tourists=[ ]
for row in rows2: 
  num_tourists.append(row[6])
Uzbekistan_num_tourists=num_tourists[2179:2185]
x=Tourist_years
y=Uzbekistan_num_tourists

#plotting second graph
fig,ax=plt.subplots()
ax.scatter(x, y)
ax.set_xticks(Tourist_years)
ax.set_yticks(Uzbekistan_num_tourists)
ax.set_yticklabels(['90', '240', '980', '2030', '2690','5350'])
ax.set_ylabel('Number of Tourists')
ax.set_xlabel('Year')
ax.set_title('Number of Tourists that visit Uzbekistan')

plt.show()

