# By: HAKUNA MATATA
# Usage: keep shellcode2exe.py in the same folder as this file
#		convertShellcode2exe.py <file name>

from binascii import a2b_hex
from os import system
import sys

try:
	filename = sys.argv[1]
except:
	try:
		check = filename
	except:
		filename = raw_input("Enter file that contains shellcode: ")

fr = open(filename,'rb').read()

fr = fr.replace("\\x","")
fr = fr.replace("\"","")
fr = fr.replace("\r\n","")
fr = fr.replace(" ","")

temp = ""
for i in range(0,len(fr),2):
	temp += a2b_hex(fr[i]+fr[i+1])
	
fn = filename[:filename.rfind(".")]+".bin"
fo = open(fn,'wb')
fo.write(temp)
fo.close()

fne = filename[:filename.rfind(".")]+".exe"
system("shellcode2exe.py "+fn+" "+fne)