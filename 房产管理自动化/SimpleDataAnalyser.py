import pandas as pd
import numpy as np


class SimpleDataAnalyser:

    @staticmethod
    def extract_property_info(file_path):
        try:
            dataframe = pd.read_csv(file_path)
            return dataframe
        except:
            print('File Path error')
            return None

    @staticmethod
    def currency_exchange(dataframe, exchange_rate):
        prices = dataframe['price'].values
        for i in range(len(prices)):
            try:
                prices[i] = prices[i] * exchange_rate
            except:
                prices[i] = np.nan
        return prices

    @staticmethod
    def suburb_summary(dataframe, suburb):
        suburbs = dataframe['suburb']
        if suburb == 'all':
            sub_df = dataframe
        elif not suburbs.isin([suburb]).any():
            print('Suburb does not exist')
            return
        else:
            sub_df = dataframe[dataframe['suburb'] == suburb]
        sub_df = sub_df.dropna(subset=['bedrooms', 'bathrooms', 'parking_spaces'])
        bedrooms = sub_df['bedrooms'].values
        bathrooms = sub_df['bathrooms'].values
        parking_spaces = sub_df['parking_spaces'].values

        print('Bedrooms summary:')
        print("Mean:    ", np.mean(bedrooms))
        print("Std Dev: ", np.std(bedrooms))
        print("Median:  ", np.median(bedrooms))
        print("Min:     ", np.min(bedrooms))
        print("Max:     ", np.max(bedrooms))

        print('Bathrooms summary:')
        print("Mean:    ", np.mean(bathrooms))
        print("Std Dev: ", np.std(bathrooms))
        print("Median:  ", np.median(bathrooms))
        print("Min:     ", np.min(bathrooms))
        print("Max:     ", np.max(bathrooms))

        print('Parking spaces summary:')
        print("Mean:    ", np.mean(parking_spaces))
        print("Std Dev: ", np.std(parking_spaces))
        print("Median:  ", np.median(parking_spaces))
        print("Min:     ", np.min(parking_spaces))
        print("Max:     ", np.max(parking_spaces))

        return

    @staticmethod
    def avg_land_size(dataframe, suburb):
        suburbs = dataframe['suburb']
        if suburb == 'all':
            sub_df = dataframe
        elif not suburbs.isin([suburb]).any():
            return None
        else:
            sub_df = dataframe[dataframe['suburb'] == suburb]
        sub_df = sub_df[sub_df['land_size'] > 0]
        sub_df = sub_df.dropna(subset=['land_size_unit'])
        sub_df.loc[sub_df['land_size_unit'] == 'ha', 'land_size'] = sub_df['land_size'] * 100
        return np.mean(sub_df['land_size'].values)
