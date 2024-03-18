from SimpleDataAnalyser import SimpleDataAnalyser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class DataVisualiser:

    @staticmethod
    def reverse_insertion_sort(data):
        for i in range(1, len(data)):
            item = data[i]
            j = i - 1
            while j >= 0 and item > data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = item
        return data

    def recursive_binary_search(self, data, target, low, high):
        if low > high:
            return False
        mid = low + (high - low) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            return self.recursive_binary_search(data, target, low, mid - 1)
        else:
            return self.recursive_binary_search(data, target, mid + 1, high)

    @staticmethod
    def prop_val_distribution(dataframe, suburb, target_currency='AUD'):
        analyser = SimpleDataAnalyser()

        currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12, "KRW": 860.92,
                         "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}
        if target_currency in currency_dict:
            rate = currency_dict[target_currency]
        else:
            print('The target currency exchange rate has not been recorded, and the result will be generated in AUD')
            rate = currency_dict['AUD']

        suburbs = dataframe['suburb']
        if suburb == 'all':
            sub_df = dataframe
        elif not suburbs.isin([suburb]).any():
            print('The target suburbs have not been recorded, all data will be used to generate results')
            sub_df = dataframe
        else:
            sub_df = dataframe[dataframe['suburb'] == suburb]
        prices = analyser.currency_exchange(sub_df, rate)
        prices = prices[~np.isnan(prices)]
        plt.hist(prices, bins=20)
        plt.title("Histogram of Price")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.savefig('Histogram.png')

    def sales_trend(self, dataframe):
        dataframe = dataframe.copy()
        dataframe = dataframe.dropna(subset=['sold_date'])
        dataframe['sold_date'] = pd.to_datetime(dataframe['sold_date'], format='%d/%m/%Y')
        dataframe['year'] = dataframe['sold_date'].dt.year
        all_year = dataframe['year'].value_counts()
        plot_data = [[i, j] for i, j in zip(all_year.index, all_year.values)]
        plot_data = self.reverse_insertion_sort(plot_data)
        plot_data = plot_data[::-1]
        x = [i[0] for i in plot_data]
        y = [i[1] for i in plot_data]
        plt.plot(x, y)
        plt.xlabel('Year')
        plt.ylabel('Number')
        plt.title('Sales Trend')
        plt.savefig('SalesTrend.png')

    def locate_price(self, target_price, data, target_suburb):
        analyser = SimpleDataAnalyser()
        suburbs = data['suburb']
        if not suburbs.isin([target_suburb]).any():
            print('Suburb does not exist')
            return False
        else:
            sub_df = data[data['suburb'] == target_suburb]
        prices = analyser.currency_exchange(sub_df, 1.0)
        prices = prices[~np.isnan(prices)]
        prices = self.reverse_insertion_sort(prices)
        return self.recursive_binary_search(prices, target_price, 0, len(prices)-1)

