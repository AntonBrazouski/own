#kp_16

def reader():
	myFile = 'text.txt'
	with open(myFile,'r') as reader:
		alist = reader.readlines()
				
def get_data():
	alist = ['\n#one','\n\ttext_one','\n#two','\n#one','\ntext_two']
	return alist
	

def is_hash(i):
	if i == '#':
		return True
	else:
		return False

def is_newline(i):
	if i == '\n':
		return True
	else:
		return False

def is_empty(i):
	if i == '':
		return True
	else:
		return False

def parser(alist):
	headers = []
	data = []
	myStr = ''
	block_header = False
	  
	for item in alist:
		if '#' in item and block_header == False:
			headers.append(item)
			myStr = ''
			block_header = True
		elif '\n' in item and not '#' in item:
			myStr = myStr + item
			data.append(myStr)
			block_header = False
			myStr = ''
	print(headers)
	print(data)

alist = get_data()

print(alist)
parser(alist)


