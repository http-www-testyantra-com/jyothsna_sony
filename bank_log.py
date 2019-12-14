class Bank:
 Bank_name="Sbi"
 ROI=14
 Mb="mumbai"
 def __init__(self,Name,age,phno,email,bal=0):
    self.Name=Name
    self.age=age
    self.phno=phno
    self.email=email
    self.bal=bal
 def deposit(self,amt):
    self.bal+=amt
    self.success()
 @staticmethod
 def success():
    print("trasaction is succesfull")
 def withdraw(self,amt=0):
    if amt==0:
        amt=self.get_amount()
    if amt>self.bal:
        self.failure()
        print("insufficient balance")
        return self.bal==amt
    # self.bal=self.sub(self.bal,amt)
    # self.success()

 def Display(self):
    print(self.Name,self.age,self.phno,self.email,self.bal)
 def modify(self,Name="",age=0,phno=0,email=""):
    if Name!="":
        self.Name=Name
    if age!=0:
        self.age=age
    if phno!=0:
        self.phno=phno
    if email!="":
        self.email=email
        self.success()
 @classmethod
 def change_Bname(cls,new=""):
    if new=="":
        cls.Bank_Name=new
    cls.success()
 @classmethod
 def modify_ROI(cls,new=0):
     if new == 0:
         new=cls.get_ROI()
     cls.ROI=new
     cls.success()
 @staticmethod
 def get_ROI():
     new=float(input("enter new roi"))
     return new
 @staticmethod
 def sub(a,b):
    return a-b
 @staticmethod
 def failure():
    print("transaction failure")
 @staticmethod
 def get_amount():
    amount=int(input("eter the amount"))
    return amount
 @staticmethod
 def success():
    print("Tranction successfull")
class Bank2(Bank):
 def __init__(self,Name,age,phno,email,pan,adhar,bal=0):
     self.pan=pan
     self.adhar=adhar
 def add_adhar_pan(self,pan,adhar):
     self.pan=pan
     self.adhar=adhar
ram=Bank("reeta",25,974867984,"reeta.com",10000)
sam=Bank("seetha",28,958785,"seetha")
Bank.modify_ROI()
ram.Display()
sam.withdraw()
Bank.Display(ram)
Bank.withdraw(sam,10000)
Bank2.add_adhar_pan(ram,173568735,"dhgjh")
print(ram.adhar)
print(ram.pan)









