
import csv


customers = open('customers.csv', 'r')
country = open('customer_country.csv', 'w',)
counter = 0

customer_file = csv.reader(customers, delimiter= ',')
#country_file = csv.writer(country, delimiter = ',')
# unnecessary

for record in customer_file:
    country.write(record[1] +', '+ record[2] + ', ' + record[4]+ '\n')
    counter += 1

print(counter)







