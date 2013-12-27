#12.5.3 Examples

#How to extract an entire tar archive to the current working directory:

import tarfile
import sys

def tar_open(filename):
	tar = tarfile.open(filename)
	tar.extractall()
	tar.close()

#How to create an uncompressed tar archive from a list of filenames:

def tar_add(targetfilename, *arglist):
	tar = tarfile.open(targetfilename, "a")
	for name in arglist:
	    tar.add(name)
	tar.close()

#How to read a gzip compressed tar archive and display some member information:

def tar_info(filename):
	if tarfile.is_tarfile(filename):
		tar=tarfile.open(filename)
	else:
		tar = tarfile.open(filename, "r:gz")
	for tarinfo in tar:
	    msg=tarinfo.name + "is" + str(tarinfo.size) + "bytes in size and is "
	    if tarinfo.isreg():
	        msg+="a regular file."
	    elif tarinfo.isdir():
	        msg+="a directory." 
	    else:
	        msg+="something else."
	    print(msg)
	tar.close()

#How to create a tar archive with faked information:

def tar_fake(filename):
	tar = tarfile.open(filename, "w:gz")
	for name in namelist:
	    tarinfo = tar.gettarinfo(name, "fakeproj-1.0/" + name)
	    tarinfo.uid = 123
	    tarinfo.gid = 456
	    tarinfo.uname = "johndoe"
	    tarinfo.gname = "fake"
	    tar.addfile(tarinfo, file(name))
	tar.close()

#The only way to extract an uncompressed tar stream from sys.stdin:

def tar_open_stdin():
	tar = tarfile.open(mode="r|", fileobj=sys.stdin)
	for tarinfo in tar:
	    tar.extract(tarinfo)
	tar.close()

def sample(*args):
	for name in args:
		with open(name) as f:
			print(f.read())

# python 3.3
if __name__=="__main__":
	usage="""
Usage:
1.tar_open(ex.test.tar)
2.tar_add(ex. tar_add(test.tar,a.txt,b.txt,c.txt))
3.tar_info(tar or gzip only)(ex.test.tar.gz)
q.quit
		"""
	user_select=""
	while user_select != "q":
		print(usage)
		user_select=input("Select:")
		if user_select=="1":
			filename=input("tar_open:")
			tar_open(filename)
		elif user_select=="2":
			filename=input("tar_add:")
			filelist=input("filelist(sep=',')")
			files=filelist.split(sep=',')
			for f in files:
				tar_add(filename,f)
		elif user_select=="3":
			filename=input("tar_info:")
			tar_info(filename)
