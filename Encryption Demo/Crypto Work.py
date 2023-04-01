#Use  pip install cryptography for install cryptography Library
import random
from cryptography.fernet import Fernet

class Customer:
    def __init__(self, name, card_number, expiry_date, cvv, balance):
        self.name = name
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.balance = balance

class Retailer:
    def __init__(self, name):
        self.name = name

    def process_payment(self, customer, amount):
        encrypted_details = Bank.encrypt_card_details(customer)
        if Bank.verify_transaction(encrypted_details, amount):
            customer.balance -= amount
            return True
        else:
            return False

class Bank:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_card_details(customer):
        key = Bank.generate_key()
        f = Fernet(key)
        card_details = f"{customer.card_number},{customer.expiry_date},{customer.cvv}"
        encrypted_details = f.encrypt(card_details.encode())
        print("Encrypted Details:-", encrypted_details)
        return encrypted_details, key

    @staticmethod
    def decrypt_card_details(encrypted_details, key):
        f = Fernet(key)
        decrypted_details = f.decrypt(encrypted_details).decode()
        print("Decrypted Details:-", decrypted_details)
        card_number, expiry_date, cvv = decrypted_details.split(',')
        return card_number, expiry_date, cvv

    @staticmethod
    def verify_transaction(encrypted_details, amount):
        encrypted_card_details, key = encrypted_details
        card_number, expiry_date, cvv = Bank.decrypt_card_details(encrypted_card_details, key)
        # In a real implementation, the bank would have a database of customer card details
        # Here, we're just checking the card number for simplicity
        if customer.card_number == card_number:
            if customer.balance >= amount:
                return True
        return False

# Create objects for customer, retailer, and bank
customer = Customer("John Doe", "1234 5678 9012 3456", "12/25", "123", 1000)
retailer = Retailer("Best Store")
purchase_amount = random.randint(1, 2000)  # Random purchase amount between 1 and 2000

# Process the payment
if retailer.process_payment(customer, purchase_amount):
    print(f"Payment successful. Remaining balance: ${customer.balance:.2f}")
else:
    print(f"Payment declined. Insufficient balance.")
