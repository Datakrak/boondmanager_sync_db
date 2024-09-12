from dotenv import load_dotenv
import mysql.connector as MC
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Payment, Purchase

load_dotenv()
DB_IP=os.getenv('DB_IP')
DB_USER=os.getenv('DB_USER')
DB_PWD=os.getenv('DB_PWD')
DB_NAME=os.getenv('DB_NAME')

#db_url = f"jdbc:mysql://{DB_IP}:3306/{DB_NAME}?user={DB_USER}&password={DB_PWD}&useSSL=false"
db_url = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_IP}:3306/{DB_NAME}"

engine = create_engine(db_url)



try:
    conn = engine.connect()

    Base.metadata.drop_all(bind=conn)

    Base.metadata.create_all(bind=conn)

    Session = sessionmaker(bind=conn)
    session = Session()
    achat = Purchase(id=2, name="Mon achat", id_societe=3)
    session.add(achat)
    session.commit()
    conn.commit()

    paiement = Payment(id=1, id_purchase=2, name="Ma facture 1", total_ht=3.33)
    session.add(paiement)
    session.commit()
    conn.commit()



except Exception as ex:
    print(ex)
else: 
    print("Connection succesfull")

