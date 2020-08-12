file=open(r'inputFile.txt')
fh=file.read()
lines=fh.split('\n')
file.close()
pass_File=open('pass_File.txt','w')
fail_File=open('fail_File.txt','w')
for x in lines:
    if x.split()[2]=='P':
      
      pass_File.write(x+"\n")
  
    else:
      fail_File.write(x+'\n')
pass_File.close()
fail_File.close()
