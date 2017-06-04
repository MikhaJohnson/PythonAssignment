import sys
import re
import os
import shutil
import commands
def getAbsolutePath(directory):
  list1=[]
  filename=os.listdir(directory)
  #print filename
  for files in filename:
    #print files
    
    match=re.search(r'__(\w+)__',files)
    if match:
      path1=os.path.join(directory,files)
      path2=os.path.abspath(path1)
      list1.append(path2)
  return list1
def copy_to(paths, dirpath):
  if not os.path.exists(dirpath):
    os.mkdir(dirpath)
  for path in paths:
    fname=os.path.basename(path)
    path11=os.path.join(dirpath,fname)
    shutil.copy(path,path11)

def main():
 
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

 
  # The args array is left just containing the dirs.
  a=args[1]
  #print a
  todir = ''
  if args[0] == '--todir':
    todir = args[2]
    del args[0:2]
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  # +++your code here+++

  paths = []
  paths.extend(getAbsolutePath(a))
  #getAbsolutePath(a)
  print paths
  
  if todir:
    copy_to(paths,todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)
 
  # +++your code here+++
  
if __name__ == "__main__":
  main()

