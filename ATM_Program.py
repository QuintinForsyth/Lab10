# ATM program

import os
import sys

def menu(id): 
  '''
  provides the user with actions
  '''
  print("Press 1 to view account balance\nPress 2 to withdraw\nPress 3 to deposit\nPress 4 to exit\n")
  try:
    choice = int(input())
    if (choice == 1):
      with open(id+".txt") as f:
        account = f.readlines()
        if account:
          print("Your balance is $"+account[0])
        else:
          print("Your balance is $0")
    elif (choice == 2):
      withdraw(id)
    elif (choice == 3):
      deposit(id)
    else:
      print("Thank You! Goodbye.")
      return
    menu(id)
  except:
    menu(id)
      
def create_account(id):
  '''
  creates account if none existed
  '''
  fwrite = open(id + ".txt","w")
  fwrite.write(str(0))
  fwrite.close()
  menu(id)

def deposit(id):
  '''
  deposits money
  '''
  new_balance = 0
  with open(id +".txt") as f:
    balance = f.readlines()
  try:
    amount = int(input("Please enter amount to deposit, you currently $"+balance[0]+": $"))
  except:
    deposit(id)

  else:
    # infinite money generator
    new_balance = int(balance[0]) + amount
  fwrite = open(id + ".txt","w")
  fwrite.write(str(new_balance))
  fwrite.close
  
def withdraw(id):
  '''
  takes out our fictitious money an dputs it in the void
  '''
  new_balance = 0
  with open(id +".txt") as f:
    balance = f.readlines()
  try:
    amount = int(input("Please enter amount to withdraw, you currently $"+balance[0]+": $"))
  except:
    withdraw(id)

  if amount > int(balance[0]):
    print("You cannot withdraw more than your total of $"+balance[0])
    withdraw(id)

  new_balance = int(balance[0]) - amount
  fwrite = open(id + ".txt","w")
  fwrite.write(str(new_balance))
  fwrite.close
  
def start():
  '''
  starts
  '''
  try:
    id = int(input("Please enter your bank ID: "))
    sid = str(id)
    if os.path.isfile(str(id)+ ".txt"):
      menu(sid)
    else:
      create_account(sid)
  except:
    start()

    
start()
  