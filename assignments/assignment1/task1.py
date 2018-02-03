
def re_text(t):
    newtxt=''
    vowels=("a","e","i","o","u")
    for x in t:
        if x not in vowels:
            newtxt+= ''.join(x)
    return newtxt

    
if __name__ == '__main__':   
    print(re_text("mobile"))



def getIndex(m,n):
    ind=list();
    offset=0;
    for x in m:
        if x is n:
            
            ind.append (m.index(x,offset))
            offset=ind[-1]+1;
    return (ind)
 

    
if __name__ == '__main__':    
    print(getIndex("i love iti","i"))


def multi(m):
    ind=[]
    for i in range(1,m+1):
        in_index=[]
        for j in range(1,i+1):
            
            in_index.append(i*j)

        ind.append(in_index)   
    return ind 
            
         
if __name__ == '__main__':
    print(multi(3))

def calc_area(str,w,h=1):
    if str is "t":
       
       return  (0.5*w*h)
    if str is "r":
       
       return  (w*h)
    
    if str is "s":
       
       return  (w*w)
    if str is "c":
       
       return  (3.14*w^2)
if __name__ == '__main__':    
    print(calc_area("s",5))



def diction(str):
    dictionary={}
    
    for i in str:
        try:
            name=dictionary[i[0]]  
        except :
            name=[]
        name.sort()    
        name.append(i)
        dictionary[i[0]]=name
    return(dictionary)

name=['marwa','lamiaa','Mohamed']
if __name__ == '__main__':
    print(diction(name))    

if __name__ == '__main__':
    k = 6
    for i in range(0, 4):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print()

        
      