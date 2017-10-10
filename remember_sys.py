import sys

def show():
    with open('database.txt') as file:
        for line in file:
            print(line)

def rememberer(thing):
    with open('database.txt', 'a') as file:
        file.write(thing+'\n')

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))