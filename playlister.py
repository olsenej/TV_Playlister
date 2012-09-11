import os
import re
from hachoir_metadata import extractMetadata
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_core.i18n import getTerminalCharset
from sys import argv, stderr, exit

os.system('cls')
print ""
print ""
print "Currently in " + os.getcwd() + "\n"
cwd = raw_input("Where are the files?" + "\n" + "(Default G:\TV): ")
if cwd == "":
	os.chdir("G:\TV")
else:
	os.chdir(cwd)
	
print "CWD: " + os.getcwd() + "\n\n"
show_list = os.listdir(os.getcwd())
#show_list.remove("a.xspf")
show_list.sort()

#open the playlist file
f = open("a.xspf", 'w')

print "Shows Added:"
print "====================="

#initialize paths and counter
paths = []
z=0
for item in sorted(set(show_list)):
	paths.append('"'+os.getcwd()+'\\'+item+'"')
	print item
	z+=1
	
f.write(
"<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n" + \
"<playlist xmlns=\"http://xspf.org/ns/0/\" xmlns:vlc=\"http://www.videolan.org/vlc/playlist/ns/0/\" version=\"1\">" + "\n" + \
"\t" + "<title>Playlist</title>" + "\n" + \
"\t" + "<trackList>" + "\n"
)
list_counter = 0

for root, dirs, files in os.walk(os.getcwd()):
	#Do some RegEx to fix spaces and Unix to NT pathing
	p=re.compile('\s')
	slash_fix=re.compile('\\\\')
	
	for episode in files:
		list_counter +=1
		root = p.sub("%20", root)
		root = slash_fix.sub("/", root)
		f.write("\t"+"\t"+"<track>" +"\n" +"\t"+"\t"+"\t"+"<location>file:///" + \
		root +"\\"+p.sub("%20", episode)+ \
		"</location>" + "\n" + \
		"\t"+"\t"+"\t"+"<title>" + episode +"</title>" + "\n" +\
		"\t"+"\t"+"\t"+"<extension application=\"http://www.videolan.org/vlc/playlist/0\">"+ "\n"+ \
		"\t"+"\t"+"\t"+"\t"+"<vlc:id>"+str(list_counter)+"</vlc:id>" + "\n" + \
		"\t"+"\t"+"\t"+"</extension>" + "\n" + \
		"\t"+"\t"+"</track>" +"\n"
		)

f.write("\t" + "</trackList>" + "\n")
f.write("\t" + "<extension application=\"http://www.videolan.org/vlc/playlist/0\">" + "\n")

for x in range(0, list_counter):
		f.write("\t"+"\t"+"\t"+"<vlc:item tid=\""+str(x)+"\"/>" + "\n")
	
f.write("\t" + "</extension>" + "\n" + "</playlist>")
f.close()
print "\n" + "Playlist created. Great job."

print ""
print ""

#Not ready yet
'''print "Parsing metadata"
print ""
argv[1] = root + episode
if len(argv) != 2:
	print >>stderr, "use: %s filename" % argv[0]
	#exit(1)
filename = argv[1]
print "argv: "+argv
filename, realname = unicodeFilename(filename), filename
parser = createParser(filename, realname)
if not parser:
	print stderr, "can't parse"
	exit(1)
try:
	metadata = extractMetadata(parser)
except HacoirError, err:
	print "Error: %s" % unicode(err)
	metadata=None
if not metadata:
	print "no metadata"
	exit(1)
text = metadata.exportPlaintext()
charset = getTerminalCharset()
for line in text:
	print makePrintable(line, charset)'''






