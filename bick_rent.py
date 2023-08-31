class bike:
    def __init__(self,s):
        self.s=s
    def display(self):
        print("available bike stock :",self.s)
    def rent(self,q):
        if q<=0 :
            print("enter the perfect value !!!")
        elif q > self.s:
             print("enter the perfect value !!!")
        else:
            self.s=self.s-q
            print("Total price is ",q*100)
            print("Total bike",self.s)

while True:
    obj=bike(100)
    us=int(input('''
    1.Display the stock
    2.Rent bike
    3.Exit       
    '''))
    if us==1:
        obj.display()
    elif us==2:
        e=int(input("Entert the bike quntity:"))
        obj.rent(e)
    else:
        break

        