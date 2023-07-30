from data_reader import DataReader
import numpy as np


# child class
class NumPyOperations(DataReader):
    def __init__(self, csv_file):
        super().__init__(csv_file)

    def max_high(self):
        """Using numpy to find the maximum value of High column"""
        return f"\nMax High Price: {np.max(self.data_frame['High'])}\n"

    def volume_75th_percentile(self):
        """Calculating the 75th percentile of Volume using numpy"""
        return f"\n75th Percentile of Volume: {np.percentile(self.data_frame['Volume'], 75)}\n"

    def min_low(self):
        """Using numpy to find the minimum value of Low column"""
        return f"\nMinimum Low Price: {np.min(self.data_frame['Low'])}\n"

    def top_number_of_closing_prices(self, num):
        """Using numpy to find the top number of maximum ClosingPrice values"""
        top_closing_prices = np.sort(self.data_frame['ClosingPrice'])[-num:]
        return f"\nTop {num} Maximum Closing Prices: {top_closing_prices}\n"

    def index_of_highest_closing_price(self):
        """Using numpy to find the index of the highest ClosingPrice"""
        index = np.argmax(self.data_frame['ClosingPrice'])
        return f"\nIndex of Highest Closing Price: {index}\n"


if __name__ == "__main__":
    print('This file is just a blueprint and works in conjunction with other files. Not for individual use!')
