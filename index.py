from lib import pre_processor,assembler
import os
import shutil
inp = raw_input("enter file name containing .x files\n")
#addr= (raw_input('enter address'))
sw=open('userinput.txt','w')
sw.write(inp)
sw.close()
'''
fw=open('address.txt','w')
fw.write(addr)
fw.close()
'''
fp=open(inp,'r')
#f1=open('sampleCode1.txt','w')
c=[]
asm=[]
ffff=[]
for line in fp:
	c.append(line)

	lis=line.split('.')[0]
	ffff.append(lis)
	if  os.path.isdir(lis):
		shutil.rmtree(lis)
	os.mkdir(lis)

fp.close()
os.system('gcc demo.c -o demo')
os.system('./demo')
os.system('python3 gui.py')


fileNames = []
fx=open(inp,'r')
for line in fx:
	l=line.split('\n')[0]
	fileNames.append(l)

pre_processor.replace_macros ( fileNames )
pre_processor.replace_opcodes ( fileNames )
assembler.createSymbolTable( fileNames )
assembler.replaceTable( fileNames )


fileext=['.pre','.pre.s']
for file11 in os.listdir("/home/vsl/Desktop/cs241/"):
	for ext in fileext:
		if file11.endswith(ext):
			os.remove(file11)
			
	
fileext=[]
fileext=['.8085','.l','.li','.loaded','.ls','.txt','.table','.s']
for file11 in os.listdir("/home/vsl/Desktop/cs241/"):
	for ext in fileext:
		if file11.endswith(ext):
			for xxx in ffff:
				if xxx in file11:
					#print file11
					src='/home/vsl/Desktop/cs241/'+file11
					dst='/home/vsl/Desktop/cs241/'+xxx+'/'
					if shutil.move(src, dst):
						break
				else:
					continue
				#except ValueError:
		
