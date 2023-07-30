# Sample task for data analysis and manipulation of famous companies
# Notice: The numbers are not real and I made them up just for the sake of this task
# Copyright © Reza Karami  2023

from pandas_ops import PandasOperations
from numpy_ops import NumPyOperations
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import Base
from database import CompanyStockPrices
import csv
import logging
import os
import multiprocessing
import random


class Main:
    def __init__(self, numpy_obj, pandas_obj):
        self.np_obj = numpy_obj
        self.pd_obj = pandas_obj

    def numpy_operations(self, top_number_of_closing_prices: int):
        lock = multiprocessing.Lock()
        with lock:
            print('NumPy operations are about to begin:\n\n')
            time.sleep(random.randint(3, 5))

            for func in [self.np_obj.max_high(),
                         self.np_obj.volume_75th_percentile(),
                         self.np_obj.min_low(),
                         self.np_obj.top_number_of_closing_prices(top_number_of_closing_prices),
                         self.np_obj.index_of_highest_closing_price()]:
                print(func)
                time.sleep(1)

            print('NumPy operations are finished\n=====================\n')

    def pandas_operations(self, closing_price_above_value: int, produce_data_frame_above_value: int, ascending: bool):
        lock = multiprocessing.Lock()
        with lock:
            print('Pandas operations are about to begin:\n')
            time.sleep(random.randint(3, 5))

            for func in [self.pd_obj.mean_closing_price(),
                         self.pd_obj.max_opening_price_company(),
                         self.pd_obj.closing_price_above_value(closing_price_above_value),
                         self.pd_obj.add_price_diff_column(),
                         self.pd_obj.produce_data_frame_above_value(produce_data_frame_above_value),
                         self.pd_obj.sort_based_on_closing_price(ascending),
                         self.pd_obj.group_by_company_and_return_mean()]:
                print(func)
                time.sleep(1)

            print('Pandas operations are finished\n=====================\n')


if __name__ == "__main__":
    CSV_FILE = 'stock_prices.csv'
    DATABASE_NAME = 'data_store.db'
    # Set the start method to 'spawn'
    multiprocessing.set_start_method('spawn')
    # ---------------------Delete Old database everytime code runs-------------------------
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
    # -------------------------------Logging the program-----------------------------------
    # log into terminal
    multiprocessing.log_to_stderr()
    # create a logger object
    logger = multiprocessing.get_logger()
    # set logging level
    logger.setLevel(logging.INFO)
    # --------------------------------database setting-------------------------------------
    engine = create_engine('sqlite:///' + DATABASE_NAME, echo=False)
    Base.metadata.create_all(bind=engine)
    # --------------------------------Creating objects ------------------------------------
    numpy_ops_obj = NumPyOperations(CSV_FILE)
    numpy_ops_obj.read_data()

    pandas_ops_obj = PandasOperations(CSV_FILE)
    pandas_ops_obj.read_data()

    main_obj = Main(numpy_ops_obj, pandas_ops_obj)
    # -----------------------------Save data into the database ----------------------------
    data = pandas_ops_obj.read_data()
    with Session(engine) as session:
        # read CSV file and create Company objects and add them to database
        with open(CSV_FILE, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)    # Skip the header row

            for row in reader:
                Date, Company, Symbol, OpeningPrice, ClosingPrice, High, Low, Volume = row
                company = CompanyStockPrices(Date, Company, Symbol, OpeningPrice, ClosingPrice, High, Low, Volume)
                session.add(company)
            session.commit()
            session.close()
    # -----------------------------Running methods using multiprocessing-----------------------------------------
    p1 = multiprocessing.Process(target=main_obj.numpy_operations, args=(3,))
    p2 = multiprocessing.Process(target=main_obj.pandas_operations, args=(800, 90000, True))
    p1.start()
    p2.start()
