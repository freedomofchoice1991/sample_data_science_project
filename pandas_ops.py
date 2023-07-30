from data_reader import DataReader


# child class
class PandasOperations(DataReader):
    def __init__(self, csv_file):
        super().__init__(csv_file)

    def mean_closing_price(self):
        """Calculating Mean of ClosingPrice"""
        return f"\n------\nMean Closing Price: {self.data_frame['ClosingPrice'].mean()}"

    def max_opening_price_company(self):
        """Finding the Company with the Maximum OpeningPrice"""
        idx = self.data_frame['OpeningPrice'].idxmax()
        return f"\n------\nCompany with Maximum Opening Price: {self.data_frame.loc[idx, 'Company']}"

    def closing_price_above_value(self, value):
        """Filtering rows with ClosingPrice above value given"""
        return f"\n------\nClosing Prices above {value} \n{self.data_frame[self.data_frame['ClosingPrice'] > value]}"

    def add_price_diff_column(self):
        """Adding a new column 'PriceDiff' to show the difference between OpeningPrice and ClosingPrice"""
        self.data_frame['PriceDiff'] = self.data_frame['ClosingPrice'] - self.data_frame['OpeningPrice']
        return f"\n------\nDataFrame with Price Difference Column:\n{self.data_frame}"

    def produce_data_frame_above_value(self, value):
        """Creating a new DataFrame with Volume greater than value given"""
        high_volume_data_frame = self.data_frame[self.data_frame['Volume'] > value]
        return f"\n------\nDataFrame with volume > {value}:\n{high_volume_data_frame}"

    def sort_based_on_closing_price(self, ascending: bool):
        """Sort data frames based on Closing price"""
        sorted_data_frame = self.data_frame.sort_values(by='ClosingPrice', ascending=ascending)
        if ascending:
            return f"\n------\nDataFrame sorted based on Closing Price (Ascending) :\n{sorted_data_frame}"
        else:
            return f"\n------\nDataFrame sorted based on Closing Price (Descending) :\n{sorted_data_frame}"

    def group_by_company_and_return_mean(self):
        """Grouping the DataFrame by Company and calculating the mean for each company"""
        grouped_data_frame = self.data_frame.groupby('Company')['ClosingPrice'].mean().reset_index()
        return f"\n------\nMean Closing Price for each Company:\n{grouped_data_frame}"


if __name__ == "__main__":
    print('This file is just a blueprint and works in conjunction with other files. Not for individual use!')
