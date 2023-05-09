#assert statements makesure that the condition provided is true
#and if it fails then a assertionerror exception should be raised\

def test():
    try:
        x=int(input('Enter a number between 5 and 10:'))
        assert 5<=x and 10>=x
        print('the number entered is:',x)

    except AssertionError:
        print('condition failed please enter a number between 5 and 10 only')
        return test()


test()