from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Purchase(Base):
    __tablename__ = 'PURCHASES'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    id_societe = Column(Integer, ForeignKey("COMPANIES.id_company"))


    payment = relationship("Payment", back_populates="purchase")
    company = relationship("Company", back_populates="purchase")


class Payment(Base):
    __tablename__ = "PAYMENTS"

    id = Column(Integer, primary_key=True, index=True)
    id_purchase = Column(Integer, ForeignKey("PURCHASES.id"))
    name = Column(String(100), index=True)
    total_ht = Column(Float)

    
    purchase = relationship("Purchase", back_populates="payment")
    
class Company(Base):
    __tablename__ = "COMPANIES"

    id_company = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    purchase = relationship("Purchase", back_populates="company")