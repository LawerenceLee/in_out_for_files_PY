def reading_lines(filename):
    '''Reads each line of a file
    and prints it out.'''
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            print(line)

if __name__ == "__main__":
    user_file = input('Specify a filename: ')
    print('***'*15)
    reading_lines(user_file)
