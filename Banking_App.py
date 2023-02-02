# Banking app
# class based
# withdrawal and deposit
# write the transaction to a python 
# ==========================
# while true
# input
# classes
# method
# properties
# open()
# deposit money, withdraw money, see transaction history in another file,   
# client class
class Client():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
   
    def AccNo(self):
        import random
        accno = "".join(str(random.randint(0, 9)) for i in range(10))
        
        return accno 
    def transaction(self):
        depo_inq = input("Would you like to deposit? ")
        
        depo_inq = depo_inq.lower()
        
        if depo_inq == "yes":
            depo_amt = input("How much would you like to deposit in your account? ")
            int(depo_amt)
            acct_bal = depo_amt
            print(f"Your account balence is {acct_bal}. ")
            
        elif depo_inq == "no":
            withdraw_inq = input("Would you like to withdraw? ")
            withdraw_inq = withdraw_inq.lower()
            
            if withdraw_inq == "yes":
                withdraw_amt = input("How much would you like to withdraw? ")
                int(withdraw_amt)
                acct_bal = acct_bal - withdraw_amt
                print(f"Your account balance is {acct_bal}")
                
            elif withdraw_inq == "no":
                  print(f"You have come to the end of your transaction. We hope to see you again {self.name}")
            else:
                pass
        else:
            pass
                
                
                
                
       
        
                     
        
client = Client(input("What is your first name? "), input("What is your last name? "))
acc_no = client.AccNo()
print(f"Your account number is {acc_no}")

# Accessing the name property
print(f"Your name is {client.name}")   

with open(f"{client.name}.txt", "w") as file:
	        file.write(f"""Welcome {client.name} this is your new account.\n Here you'll find all your data including your transaction history (i.e. your withdrawals and your deposits) and your account balance.\n Your account number is {acc_no}. \n Your transaction history will appear once you start using your account.""")             
client.transaction()   