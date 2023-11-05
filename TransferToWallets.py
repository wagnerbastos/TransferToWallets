import locale
import random
from time import sleep

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print("Starting program...")
sleep(3)
print("\nDistribute the Dark Army's funds among all individuals with bank accounts in NYC.")
sleep(2)

name = input("Enter your name: ")

while True:
    bank_account = input("Do you possess a bank account? Please type 'Y' for yes or 'N' for no. ").lower()
    sleep(2)    
    if bank_account == 'y':
        print("\nThe system will conduct a search for a bank account registered under the previously provided name, with a verified address in the city of New York.")
        sleep(2)
        print("\nAccount located.")
        sleep(2)
        print("\nYou are eligible to claim a portion of the Dark Army's funds.")
        sleep(2)
        print("\nTransfer process will commence shortly.")
        sleep(2)
        print("\nYou will be awarded a random amount ranging from $0 to $24,000,000.00.")
        sleep(2)
        print("\nStarting transference...")
        sleep(2)
        count = 0
        while count <= 10:
            print("Transferring...")
            count += 1
            sleep(1)
        print("Transference has been successfully completed!")        
        
        random_value = random.uniform(1, 24_000_000)
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
print("This is a work of fiction. Any names or characters, businesses or places, events or incidents, are fictitious.\nAny resemblance to actual persons, living or dead, or actual events, is purely coincidental.")
