#kp_16

def reader():
	myFile = 'keep09start.txt'
	with open(myFile,'r') as reader:
		alist = reader.readlines()
	
	return alist

def write(headers, data):
	for i in range(len(headers)):
		with open('_' + headers[i] + '.txt', 'w') as myFile:
			myFile.write(headers[i])
			myFile.wrtite(data[i])

def write_files(headers, data):	
	for i in range(len(headers)):
		with open(headers[i]+'.txt','w') as my_file:
			my_file.write(headers[i] +'\n')
			my_file.writelines(data[i])

	
def get_data():
	alist = ['\n#one','\n\ttext_one','\n#two','\n#one','\ntext_two,#one,#two #three, five', '\n seven,!']
	
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
			headers.append(item[0:-1])
			myStr = ''
			block_header = True
		elif '\n' in item and not '#' in item:
			myStr = myStr + item
			data.append(myStr)
			block_header = False
			myStr = ''
	
	#write(headers, data)
	write_files(headers, data)
	print(headers)	

alist = reader()

parser(alist)


