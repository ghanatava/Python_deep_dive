def towers(n,a,b,c):
    if n==1:
        print(f'move disk {n} from pole {a} to pole{c}')
    else:
        #move n-1 disks from a to b using c as intermediate pole
        towers(n-1,a,b,c)
        #move remainig one disk from A to C
        print('Move disk {n} from pole {a} to {c}')

        #move n-1 disks from b to c using a as intermediate pole
        towers(n-1,b,c,a)
