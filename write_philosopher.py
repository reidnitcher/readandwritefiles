from matplotlib.cbook import open_file_cm


def main():
    outfile = open('philosophers.txt', 'w')
    outfile.write('John Locke' + '\n')
    outfile.write('David Humme' +'\n')
    outfile.write('Edmund Burke' + '\n')

    outfile.close

def add_my_name():
    outfile = open("philosophers.txt", "a")
    
    outfile.write("Reid Nitcher\n")

    outfile.close()

main()
add_my_name()





