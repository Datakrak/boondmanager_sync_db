import requests
import base64
import pandas as pd
import io
from dotenv import load_dotenv
import os

load_dotenv()

mail = os.getenv("mail")
pwd = os.getenv("pwd")
auth_str = f"{mail}:{pwd}"

def main():
    token = base64.b64encode(auth_str.encode('ascii')).decode()
    headers = {
        "Authorization":f"Basic {token}"
    }

    res = requests.get('https://ui.boondmanager.com/api/payments.csv', headers=headers).content


    rawData = io.StringIO(res.decode())
    print(rawData)
    df = pd.read_csv(rawData, delimiter=';')

    print(df.dtypes)
    return 0

def sync_payements():
    url = 'https://ui.boondmanager.com/api/payments.csv'
    return 0


def sync_purchases():
    url = 'https://ui.boondmanager.com/api/purchases.csv'
    return 0


def sync_companies():
    url = 'https://ui.boondmanager.com/api/companies.csv'
    return 0


def sync_contacts():
    url = 'https://ui.boondmanager.com/api/contacts.csv'
    return 0

if __name__ == "__main__":
    main()