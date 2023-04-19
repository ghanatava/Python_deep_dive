import sys
n=len(sys.argv)
args=sys.argv[1:] #exclude the program name 
print('no of commandline args=',n)
print('The args are:',args)

sum=0
for a in range(len(args)):
    sum+=int(args[a])

print(sum)




