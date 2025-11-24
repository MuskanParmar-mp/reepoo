#even number
def even_no(n):
    if n == 0:
        return
    even_no(n-1)
    if n % 2 == 0:
        print(n)

n = int(input("enter a no: "))
even_no(n)