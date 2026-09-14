# Q.Print x and N times using head

def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)

func(15,4)


# Q.Print 1 to N using head

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)

func(1,5)


# Q.Print(1 to N) using Tail

def func(n):
    if n == 0:
        return 
    func(n-1)
    print(n)

func(10)


# Q.print(N to 1) using Head 
def func(n):
    if n == 0:
        return
    print(n)
    func(n-1)

func(20)

# Q.print(N to 1) using Tail
def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)

func(1,12)