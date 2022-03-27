class Account:
    def __init__(self,accntNo,accntName,accntBalance):
        self.accntNo=accntNo
        self.accntName=accntName
        self.accntBalance=accntBalance
        

    
class AccountDemo:
    def __init__(self):
        pass

    def depositAmnt(self,acnt,depamnt):
        self.accntBalance1=acnt.accntBalance+depamnt
        return self.accntBalance1
    
    def withdrawAmnt(self,acnt,withamnt): 
        deduct=self.accntBalance1-withamnt
        if deduct<1000:
            return "No Adequate balance"
        else:
            return deduct
		

#Sample main section. 
#Do not remove the below portion of code. 
if __name__ == '__main__':
    acno=int(input())
    acname=input()
    acntbal=int(input())
    depamnt=int(input())
    withamnt=int(input())
    acnt=Account(acno,acname,acntbal)
    acntdemoobj=AccountDemo()
    print(acntdemoobj.depositAmnt(acnt,depamnt))
    print(acntdemoobj.withdrawAmnt(acnt,withamnt))