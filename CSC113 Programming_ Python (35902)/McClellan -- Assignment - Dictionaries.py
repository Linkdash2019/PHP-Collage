bday = {
  "cameron": {"BdayM": "April", "BdayD": 3, "BdayY": 2008},
  "kayden": {"BdayM": "March", "BdayD": 11, "BdayY": 2010},
  "travis": {"BdayM": "December", "BdayD": 30, "BdayY": 1998},
  #to add new default names use the following format:
  #"<name>": {"BdayM": "<Month>", BdayD: <BDay>, BdayY: <BYear>,
}

def add():
  name = input("Enter the name of the person:\n>>> ")
  month = input("Enter the birthday month NAME\nExample: December\n>>> ")
  day = int(input("Enter the Birth Day\nDays 1-31\n>>> "))
  year = int(input("Enter the full birthday year\nExample: 2008\n>>> "))
  
  bday[name.lower()] = {"BdayM": month.title(), "BdayD": day, "BdayY": year}

def delete():
  name = input("Enter the name to delete\n>>> ")
  
  try:
    del bday[name.lower()]
  except:
    print("Error person not found\nReturning to main menu\n")

def update():
  name = input("Enter the name to change\n>>> ")
  question = input("What would you like to change?\nMonth, Day, or Year\n>>> ")
  
  if question.lower() == "month":
    month = input("Enter the month\n>>> ")
    bday[name.lower()]["BdayM"] = month
    
  elif question.lower() == "day":
    day = int(input("Enter the new day\n>>> "))
    bday[name.lower()]["BdayD"] = day
    
  elif question.lower() == "year":
    year = int(input("Enter the new year\n>>> "))
    bday[name.lower()]["BdayY"] = year
  
  else:
    print("Error: Returning to main menu!")
    
def see():
  try:
    print(bday[text.lower()]["BdayM"], bday[text.lower()]["BdayD"], bday[text.lower()]["BdayY"], "\n")
  except:
    print("Error: Name not foud in database.\nTry adding a name by entering add\n")

def people():
  print("People in database are:")
  for name in bday:
    print("", name.title())
  print()
    
def helpme():
  print("help - View this message\nadd - Add a new person and birthday to the database\nchange - Edit the database\nremove - Delete someone from the database\nlist - View all people in the database\nexit - End the program\n")
  
#Start main program
text = "Nothing"

while text.lower() != "exit":
  text = input("Who's birthday do you want to view?\nEnter help for help!\n>>> ")
  
  if text.lower() == "help":
    helpme()
    
  elif text.lower() == "add":
    try:
      add()
    except:
      print("An unknown error has ococcurred\nReturning to main menu\n")
    
  elif text.lower() == "change":
    try:
        update()
    except:
        print("An unknown error has occured\nReturning to main menu\n")
    
  elif text.lower() == "remove":
    delete()
    
  elif text.lower() == "exit":
    pass
    
  elif text.lower() == "list":
    people()
    
  else:
    see()
