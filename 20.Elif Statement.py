# elif-statement-Library-Fine-Amount-Management-
"""
days      Fine Amount
  0         No Fine
  1-5       0.5
  6-10      1
  11-30     5
  30<days   Membership Canceled
"""
days = int(input("Enter the days:"))
if days == 0:
  print("Good No Fine")
elif days >= 1 and days <= 5:
  print("Fine Amount:",days*0.5)
elif days >= 6 and days <=10:
  print("Fine Amount:",days*1)
elif days >=11 and days <=30:
  print("Fine Amount:",days*5)
else:
  print("Membership Canceled")
