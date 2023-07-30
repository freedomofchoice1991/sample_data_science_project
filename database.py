# ----------SQLAlchemy ORM-----------
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CompanyStockPrices(Base):
    __tablename__ = 'companies_data'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    date = Column(String())
    name = Column(String())
    symbol = Column(String())
    opening_price = Column(Integer())
    closing_price = Column(Integer())
    high = Column(Integer())
    low = Column(Integer())
    volume = Column(Integer())

    def __init__(self, date, name, symbol, opening_price, closing_price, high, low, volume):
        self.date = date
        self.name = name
        self.symbol = symbol
        self.opening_price = opening_price
        self.closing_price = closing_price
        self.high = high
        self.low = low
        self.volume = volume


if __name__ == "__main__":
    print('This file is just a blueprint and works in conjunction with other files. Not for individual use!')
