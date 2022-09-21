
from operator import truediv


age_str = input('what is your age?')
print(f"Your age is {age_str}")

connection_choice_str =  input('Welke verbinding wilt U gebruiken[4G, 5G, Wifi open]')
# Convert answer to upper case
# The user can enter upper, lower or combined casing
connection_choice = connection_choice_str.upper()

if connection_choice == "4G":
    print(f"U bent verbonden via {connection_choice}!")
elif connection_choice =="5G":
    print(f"U bent verbonden met {connection_choice}!")
elif connection_choice =="WIFI OPEN":
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    answer_str = input("Wilt u nog steeds een verbinding maken? [Ja/nee]")
    answer = answer_str.upper()
    if answer =="Ja":
        print(f"U bent verbonden via {connection_choice}!")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")

print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in 'Hello, everyone!':
    print('Yes, Hello is within the Hello, everyone! string')

    print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
    if "hello" in "Hello, everyone!":
        print('Yes, hello is within the Hello, everyone! string')
    else:
        print('No, hello with small letters is not within the string')

# Patient exposed to TB [Tuberculoses]
print("Patient exposed to TB")
question_1_str = input("Is the patient an adult or a child? [Adult/Child]: ")
question_1 = question_1_str.upper()
if question_1 == "Adult":
    # Adult part
    print("Adult")
    question_2_str = input("Has common TB symptoms? [Yes/no]:")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Treat as likely TB patient and perform full TB exam.")
    elif question_2 == "NO":
        print("Have patient report back if unwell; return in 1 month for checkup.")
    else:
        print("Abort, unknown input.")
elif question_1 == "CHILD":
    # Child part
    print("Child")
    question_3_str = input("Can TB test be given? [Yes/No]:")
    question_3 = question_3_str.upper()
    if question_3 == "YES":
     print("Administer TB Test")
     print("Assess TB test results and child's condition")
    elif question_3 == "NO":
        question_4_str = input("Child well[Yes/no]:")
        question_4 = question_4_str.upper()
    if question_4 == "YES":
     print("6 months preventive isoniazid")
     print("Have parent bring in if child shows any symptoms.")
    elif question_4 =="NO":
        print("Take full history.\n Examine for TB.")
        print("If TB likely diagnosis, treat for TB.")
        print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")
    else:
        print ("Abort, unknown input.")
else:
     print("Abort, unknown input")

  
# Shopping Cart
print ("Shopping Cart")
question_1_str = input("Payment Method? [Online/Offline]:")
question_1 = question_1_str.upper()
if question_1 == "ONLINE":
   print("Place Purchase Order.")
   question_2_str = input("Admin User [Yes/No]:")
   question_2 = question_2_str.upper()
   if question_2 == "YES":
       print("Enter Payment Details")
       print("Place Order") 
   elif question_2 == "NO":
        question_3_str = input("Approval Rules [Approved/Rejected]:")
        question_3 = question_3_str.upper()
        if question_3 == "APPROVED":
            print("Approved")
            print("Enter Payment details") 
        elif question_3 == "REJECTED":
            print("Rejected")
            print ("Purchase Order Rejected") 
        else:
            print ("Abort, unknown input")
   else:
        print("Abort, unknown input")
elif question_1 == "OFFLINE":
     print("Offline,Place Purchase Order.")
     question_4_str = input("Admin User? [Yes/No]:")
     question_4 = question_4_str.upper()
     if question_4 == "YES":
        print("Order Created Automatically")
     elif question_4 =="NO":
        question_5_str=input("Approval rules?[Approved/Rejected]:")
        question_5=question_5_str.upper()
        if question_5 =="Approved":
            print("Order Created Automatically.")
        elif question_5 =="Rejected":
            print("Purchase Order Rejected.") 
        else:
            print("Abort, unknown input")
     else:
          print("Abort, unknown input.")       
else:
      print("Abort, unknown input.")

# Ordering at Mac Donald's
eat_in = False
eat_out = False
aborted = False

print("Welkom bij de Mac Donald's")
question_1_str = input("Hier opeten of meenemen[Opeten/Meenemen]?")
question_1 = question_1_str.upper()
if question_1 =="Opeten":
   # Eat in part
   print("Hier opeten.")
   eat_in = True
elif question_1 == "Meenemen":
     print("meenemen.")
     eat_out = True
else:
    aborted = True

if eat_in or eat_out:
 question_2_str= input("Burgers of drankjes[Burgers/Drankjes]:?")
 question_2 = question_2_str.upper()
 if question_2 == "Burgers":
    question_3_str = input("Burgers[Hamburger/Cheeseburger/Big Mac/Quarter Pounder]")
    question_3 = question_3_str.upper()
    if question_3 =="Hamburger":
        print("Hamburger")
    elif question_3 =="Cheeseburger":
        print("Cheeseburger")
    elif question_3 == "Big Mac":
        print("Big Mac")
    elif question_3 == "Quarter Pounder":
         question_4_str = input("Met of zonder kaas[Met/Zonder]:?")
         if question_4 == "Met":
            print("Met")
         elif question_4 == "Zonder":
            print("Zonder")
         else:
            aborted = True
elif question_2 == "Drankjes":
     question_5_str = input ("Warm of koude drank [Warm/Koud]:?")
     question_5 = question_5_str.upper()
     if question_5 == "Warm":
        question_6_str = input("Warme drank [Koffie/Cappucino/Chocolademelk]:")
        question_6 = question_6_str.upper()
        if question_6 == "Koffie":   
          print("Koffie")
        elif question_6 == "Cappucino":
          print("Cappucino")
        elif question_6 == "Chocolademelk":
          print("Chocolademelk")
        else:
            aborted = True
     else:
         aborted = True        
else:
    aborted = True

if aborted:
    print("Abort, unknown input.")
else:
    if eat_in:
        print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
    elif eat_out:
        print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")


