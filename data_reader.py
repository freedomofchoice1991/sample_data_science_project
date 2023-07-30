import pandas as pd


class DataReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data_frame = None
        self.max_columns = 14
        self.desired_width = 400
        self.max_rows = 25
        pd.set_option('display.width', self.desired_width)
        pd.set_option('display.max_columns', self.max_columns)
        pd.set_option('display.max_rows', self.max_rows)

    def read_data(self):
        """Load the CSV data into a pandas DataFrame"""
        self.data_frame = pd.read_csv(self.csv_file)
        return self.data_frame

    def display_data(self):
        """Show the output in PyCharm in a comprehensive way"""
        print(self.data_frame)


if __name__ == "__main__":
    print('This file is just a blueprint and works in conjunction with other files. Not for individual use!')
