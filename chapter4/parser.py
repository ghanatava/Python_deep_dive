import argparse

parser=argparse.ArgumentParser(
    description='This program displays square of a given number'
)
    

parser.add_argument("num",type=int,help="Please enter a integer number")
args=parser.parse_args()

print(args.num**2)

#to parse multiple args
list_parser=argparse.ArgumentParser()
list_parser.add_argument('nums',nargs='+')
args=list_parser.parse_args()
for x in args.nums:
    print(x)