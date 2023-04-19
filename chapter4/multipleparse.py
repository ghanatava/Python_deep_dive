import argparse

#to parse multiple args
list_parser=argparse.ArgumentParser()
list_parser.add_argument('nums',nargs='+')
args=list_parser.parse_args()
for x in args.nums:
    print(x)