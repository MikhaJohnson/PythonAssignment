import sys
import re
def extract_names(filename):
  f=open(filename,'r')
  lines=f.read()
  #print lines
  f.close()
  year=re.findall(r'Popularity in (\d{4})',lines)
  print "year is ",year
  list5=re.findall(r'<td>(\w+)</td><td>(\w+)</td><td>(\w+)</td>',lines)
  for val in list5:
    print val
  print "*****************************************************************************************************"
  print "*****************************************************************************************************"
  dict1={}
  for vals in list5:
    (rank,bname,gname)=vals
    dic1={rank,bname,gname}
    print dic1
  print "*****************************************************************************************************"
  print "*****************************************************************************************************"
  #sorted_names = sorted(dic1.keys())
  for vals in list5:
    (rank,bname,gname)=vals
    list6=[year,bname,rank]
    list7=[year,gname,rank]
    print list6
    print list7


  print "*****************************************************************************************************"
  print "*****************************************************************************************************"

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  for filename in args:
    names = extract_names(filename)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
