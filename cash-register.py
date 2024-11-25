import math

def change(amount_due,amount_paid):
  
  denominations = {"20000":20000,"10000" :10000,"5000" :5000,"2000" :2000,"1000" : 1000,"500" :500,"200" :200,"100" :100,"50" :50,"20" :20,"10" :10,"5" :5}
  change_distribution = {}
  change = (amount_paid - amount_due)
  for money in denominations:
    count=0
    while change>=int(money) and change>0:
      count+=1
      change-=int(money)
    if count>0:
      change_distribution[int(money)]=count
  return change_distribution

  
print(change(20000,50000))
