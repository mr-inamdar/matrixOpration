from numpy import *
def tresA(m,sum=0):
    for i in range(3):
        for e in range(3):
            if i == e :
                sum += m[i][e]
    return sum
def detA(m,sum=0):
    chack = 0
    for i in range(3):
        for k in range(1,2):
            for e in range(0,2):
                if e==i:
                    continue
                if i%2==0:
                    sum+=(m[0][i]*((m[k][e]*m[k+1][e+1])-(m[k][e+1]*m[k+1][e])))
                    break
                else:
                    sum-=(m[0][i]*((m[k][e]*m[k+1][e+2])-(m[k][e+2]*m[k+1][e])))
                    break
            if sum>chack or sum<chack:
                break
        chack = sum
    return sum
def adjA(m):
    r = array([[0,0,8],[9,6,0],[3,11,0]],float,ndmin=2)
    for rx in    range(3):
        for cx in range(3):
            for i in range(3):
                if i == rx:
                    continue
                for e in range(3):
                    if e == cx:
                        continue
                    if rx == 1:
                        if (cx+rx)%2 == 0:
                            v = (((m[i][e]*m[i+2][e+2])-(m[i][e+2]*m[i+2][e]))*((-1)**(cx+rx)))
                            break
                        else:
                            v = (((m[i][e]*m[i+2][e+1])-(m[i][e+1]*m[i+2][e]))*((-1)**(cx+rx)))
                            break   
                    elif (cx+rx)%2 == 0:
                        v = (((m[i][e]*m[i+1][e+1])-(m[i][e+1]*m[i+1][e]))*((-1)**(cx+rx)))
                        break
                    else:
                        v = (((m[i][e]*m[i+1][e+2])-(m[i][e+2]*m[i+1][e]))*((-1)**(cx+rx)))
                        break
                break
            # print(v)
            r[cx][rx]=v
    return r
def invA(m):
    rmx = adjA(m)
    E = detA(m)
    for i in range(3):
        for e in range(3):
            rmx[i][e] /= E
    return rmx       
m = array(input("Enter a element of matrix with a defferece of one blanck space : ").split(),float,ndmin=2)
m = m.reshape(3,3)
c = input("\t\t1.adjA \n\t\t2.detA \n\t\t3.invA \n\t\t4.tresA \nEnter a curasponding no to per this task opretion : ")
match(c):
    case '1':
        print(adjA(m))
    case '2':
        print(detA(m))
    case '3':
        print(invA(m))
    case '4':
        sum = 0
        print(tresA(m,sum))
    case _:
        print("oops!you enter somthing deffrent ,read properly and tray again")    
