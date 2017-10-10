import sys

def text_into_file(filename):
	with open('/Users/lawerencelee/Desktop/'+filename+'.txt', 'a') as file:
		content = input('Paste text to be added to file: ')
		file.write(content + '\n')

def show():
	with open('/Users/lawerencelee/Desktop/'+filename+'.txt') as file:
		print(20*'***')
		for line in file:
			print(line)

if __name__ == "__main__":
	filename = input('Specify File Name: ')
	if sys.argv[1].lower() == '--list':    # --list is literally typed in to the commmand line
		show()
	else:

		text_into_file(filename)

