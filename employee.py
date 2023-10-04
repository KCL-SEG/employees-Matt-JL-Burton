"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission,hours, hourlyPay, montlhySalary, fixedBonus, bonusPerContract, contractLanded):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.hours = hours
        self.hourlyPay = hourlyPay
        self.montlhySalary = montlhySalary
        self.fixedBonus = fixedBonus
        self.bonusPerContract = bonusPerContract
        self.contractLanded = contractLanded

    def get_pay(self):
        pay = 0
        if self.contract == "hourly":
            pay =  pay + self.hours * self.hourlyPay
        else:
            pay = pay + self.montlhySalary
        if self.commission == "fixed":
            pay = pay + self.fixedBonus
        elif self.commission == "contract":
            pay = pay + (self.contractLanded * self.bonusPerContract)
        else:
            pay = pay
        return pay


    def __str__(self):
        returnStr = self.name + " works on a "
        if self.contract == "hourly":
            returnStr = returnStr + "contract of " + str(self.hours) + " hours at " + str(self.hourlyPay) + "/hour"
        else:
            returnStr = returnStr + "monthly salary of " + str(self.montlhySalary)
        
        if self.commission=="fixed":
            returnStr = returnStr + " and receives a bonus commission of " + str(self.fixedBonus)
        elif self.commission=="contract":
            returnStr = returnStr + " and receives a commission for " + str(self.contractLanded) + " contract(s) at " + str(self.bonusPerContract) + "/contract"
        else:
            returnStr = returnStr
        returnStr = returnStr + ". Their total pay is " + str(self.get_pay()) + "." 
        return returnStr


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"Monthly","None",0,0,4000,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"hourly","None",100,25,0,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"Monthly","contract",0,0,3000,0,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"hourly","contract",150,25,0,0,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"Monthly","fixed",0,0,2000,1500,0,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"hourly","fixed",120,30,0,600,0,0)

# print(billie)
print(charlie)
# print(renee)
print(jan)
print(robbie)
print(ariel)