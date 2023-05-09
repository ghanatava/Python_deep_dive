class Exception1(Exception):

    def __init__(self,args):
        self.message=args

def check(dict):
    for k,v in dict.items():
        print('Name={:15s} Balance={:10.2f}'.format(k,v))
        if v<2000.00:
            raise Exception1('Balance ammount is less than the min. balance in account of '+k)
        
bank={'Rahul':5000.00,'Vani':10000,'Ajay':100}

try:
    check(bank)

except Exception1 as me:
    print(me)




    