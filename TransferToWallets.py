import datetime
import locale
import random
import time
import sys

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print("Starting program...")
time.sleep(3)
print("\nDistribute the Dark Army's funds among all claiming individuals with bank accounts in NYC.")
time.sleep(2)
print(f"The distribution will be available for the next 15 minutes, starting {formatted_datetime}.")
time.sleep(2)

def get_user_info():
    """Gather and confirm basic user information."""
    while True:
        name = input("Enter your name: ")
        print(f"The name entered by you was {name.title()}.")
        review_name = input(f"Is {name.title()} your name? (Please type 'Y' for yes or 'N' for no.) ").lower()
        if review_name == 'y':
            break
        else:
            print("Let's try again.")
            
    while True:        
        valid_ssn = None
        while valid_ssn is None:
            ssn = input("Enter your Social Security Number (9 digits, numbers only): ")
            ssn = ssn.replace(" ", "").replace("-", "")
            if len(ssn) == 9 and ssn.isdigit():
                valid_ssn = ssn
            else:
                print("Invalid SSN. SSN should have nine digits. Please try again.")
                
        print(f"You entered a valid SSN: {valid_ssn}.")
        review_ssn = input(f"Is {valid_ssn} your Social Security Number? (Please type 'Y' for yes or 'N' for no). ").lower()
        if review_ssn == 'y':
            break
        else:
            print("Let's try again.")
    
    return name, valid_ssn

def claim_funds(user_info):
    """Claim funds based on user eligibility."""
    name, valid_ssn = user_info
    while True:
        bank_account = input("Do you possess a bank account? (Please type 'Y' for yes or 'N' for no.) ").lower()
        time.sleep(2)
        
        if bank_account == 'y':
            print("\nThe system will conduct a search for a bank account registered under the previously provided name and SSN, with a verified address in the city of New York.")
            time.sleep(3)
            print("\nPlease note that this process may take several minutes. If you initiated the process within the specified time frame, you will still receive your portion even if the verification is completed after the designated period.\n")
            time.sleep(3)
            
            count = 0
            while count <= 15:
                print("Locating account...")
                count += 1
                time.sleep(2)
                
            print("\nAccount located.")            
            time.sleep(2)
            
            print("\nYou are eligible to claim a portion of the Dark Army's funds.")
            time.sleep(2)
            print("\nTransfer process will commence shortly.")
            time.sleep(2)
            print("\nYou will be awarded a random amount ranging from $10.00 to $24,000,000.00.")
            time.sleep(2)
            print("\nStarting transference...")
            time.sleep(2)
            
            count = 0
            while count <= 10:
                print("Transferring...")
                count += 1
                time.sleep(1)
            
            print("Transference has been successfully completed!")        
            random_value = random.uniform(10, 24_000_000)
            formatted_value = locale.currency(random_value, grouping=True)
            time.sleep(2)
            print(f"\n{name.title()} receives {formatted_value}!\n")        
            break
        
        elif bank_account == 'n':
            print("I apologize, but you do not qualify to receive funds from the Dark Army.\n")        
            break
        
        else:
            print("Sorry, that's not an accepted answer. Please try again.")

# Gather and confirm user information
user_info = get_user_info()

# Claim funds based on user eligibility
claim_funds(user_info)

def typewriter_effect(sentence, delay=0.1):
    for char in sentence:
        sys.stdout.write(char)  # Write the character to the console
        sys.stdout.flush()      # Ensure it gets printed immediately
        time.sleep(delay)       # Pause for the specified delay
    print()  # Move to the next line after the sentence is done

typewriter_effect("DISCLAIMER:\nThis is a work of fiction. Any names or characters, businesses or places, events or incidents, are fictitious.\nAny resemblance to actual persons, living or dead, or actual events, is purely coincidental.\nNo animals were harmed during the making of this program.\n")
