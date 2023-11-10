import datetime
import locale
import random
from time import sleep

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print("Starting program...")
sleep(3)
print("\nDistribute the Dark Army's funds among all claiming individuals with bank accounts in NYC.")
sleep(2)
print(f"The distribution will be available for the next 15 minutes, starting {formatted_datetime}.")
sleep(2)

name = input("Enter your name: ")
print(f"The name entered by you was {name.title()}.")

valid_ssn = None
while valid_ssn is None:
    ssn = input("Enter your Social Security Number (9 digits, numbers only): ")
    ssn = ssn.replace(" ", "").replace("-", "")
    if len(ssn) == 9 and ssn.isdigit():
        valid_ssn = ssn
    else:
        print("Invalid SSN. SSN should have nine digits. Please try again.")
        
    if valid_ssn is not None:
        print(f"You entered a valid SSN: {valid_ssn}.")

while True:
    bank_account = input("Do you possess a bank account? Please type 'Y' for yes or 'N' for no. ").lower()
    sleep(2)    
    if bank_account == 'y':
        print("\nThe system will conduct a search for a bank account registered under the previously provided name and SSN, with a verified address in the city of New York.")
        sleep(3)
        print("\nPlease note that this process may take several minutes. If you initiated the process within the specified time frame, you will still receive your portion even if the verification is completed after the designated period.\n")
        sleep(3)
        
        count = 0
        while count <= 15:
            print("Locating account...")
            count += 1
            sleep (2)
            
        print("\nAccount located.")            
        sleep(2)
        
        print("\nYou are eligible to claim a portion of the Dark Army's funds.")
        sleep(2)
        print("\nTransfer process will commence shortly.")
        sleep(2)
        print("\nYou will be awarded a random amount ranging from $10.00 to $24,000,000.00.")
        sleep(2)
        print("\nStarting transference...")
        sleep(2)
        
        count = 0
        while count <= 10:
            print("Transferring...")
            count += 1
            sleep(1)
        print("Transference has been successfully completed!")        
        
        random_value = random.uniform(10, 24_000_000)
        formatted_value = locale.format_string('%d', random_value, grouping=True)
        decimal_part = "%.2f" % (random_value % 1)
        total_value = formatted_value + decimal_part[1:]
        sleep(2)
        print(f"\n{name.title()} receives ${total_value}!\n")        
        break
       
    elif bank_account == 'n':
        print("I apologize, but you do not qualify to receive funds from the Dark Army.\n")        
        break
    
    else:
        print("Sorry, that's not an accepted answer. Please try again.")

print("DISCLAIMER:\n")
print("This is a work of fiction. Any names or characters, businesses or places, events or incidents, are fictitious.\nAny resemblance to actual persons, living or dead, or actual events, is purely coincidental.\n")
print("No animals were harmed during the making of this program.\n")
