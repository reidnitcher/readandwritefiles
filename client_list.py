
infile = open('clients.txt', 'r')

counter = 1

for client in infile:
      print(counter,". ", client.rstrip('\n'))
      counter += 1
     

