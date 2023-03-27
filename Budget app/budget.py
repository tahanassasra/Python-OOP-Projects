import math

class Category:
    def __init__(self, name, ledger=[]):
        self.name = name
        self.ledger = []

    def __str__(self):
        result = ""
        a = int(15 - int(len(self.name)/2))
        if len(self.name)%2:
            result = (a*'*'+str(self.name)+(a-1)*'*')
        else:
            result = (a*'*'+str(self.name)+a*'*')
        tot_amount = 0.0
        for item in self.ledger:
            result += "\n" + str(item['description'])[:23] + (30 - len(str(item['description'])[:23]) - len(str("%7.2f" %(item['amount']))))*" " + str("%7.2f" %(item['amount']))
            tot_amount += item['amount']
        result += "\n" + "Total:" + str("%7.2f" %tot_amount)
        return result


    def get_balance(self):
        amount = 0
        for item in self.ledger:
            amount += item['amount']
        return amount

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})

    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": -self.amount, "description": self.description})

        if self.check_funds(self.amount):
            return True
        return False
  
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
            

###  for debugging purpose ###
food = Category( "Food")
clothing = Category( "Clothing")
entertainment = Category("Entertainment")

food.deposit(20, 'Restaurant in Ramallah')
food.withdraw(17.54, 'supermarket')

clothing.deposit(340, "t-shirt")
clothing.withdraw(20, "holiday clothing")
clothing.transfer(30, entertainment)

entertainment.withdraw(20, 'market')

#################################

def create_spend_chart(categories):
    spent = []
    withdrawals = {}
    for x in categories:
        for y in x.ledger:
            if y['amount'] < 0:
                if x.name in withdrawals:
                    withdrawals[x.name] += y['amount']
                else:
                    withdrawals[x.name] = y['amount']
    category_count = len(withdrawals)
    tot_spent = abs(sum(withdrawals.values()))

    percent = {}
    for key in withdrawals:
        percent[key] = 10*math.floor((10*(abs(withdrawals[key]) / tot_spent)))
        
    key_list = list(withdrawals.keys())  # list of all categories (having withdraw amount)
    len_list =[]
    for i in range(len(key_list)):
        len_list.append(len(key_list[i]))
    max_len = max(len_list) # maximum length for category item
    #make all category with same length (max_len)
    for i in range(len(key_list)):
        if len(key_list[i]) < max_len:
            key_list[i] += (max_len - len(key_list[i]))*(' ')

    final_res="Percentage spent by category\n"
    for x in range(100, -10, -10):
        final_res += (str("%3.f" %x)+'|')
        for key in percent:
            if percent[key] >= x:
                final_res +=(' o ')
            else:
                final_res +=('   ')
        final_res +=('\n')

    final_res += ("    "+ (3 * category_count + 1) * '-' + '\n')
    
    space = ' '
    for i in range(max_len):
        final_res +=(space*4)
        for x in key_list:
            final_res +=(' ' + x[i] + ' ')
        final_res +=('\n')
    final_res = final_res[0:-2]
    final_res +=('  ')
    return final_res
        

    
######   For debugging purpose   #######
        
cati = [food, clothing, entertainment]
print(create_spend_chart(cati))
########################################