from SimpleDataAnalyser import SimpleDataAnalyser
from DataVisualiser import DataVisualiser


class Menu:
    def __init__(self):
        self.dataframe = None
        self.analyser = SimpleDataAnalyser()
        self.visualiser = DataVisualiser()

    def read_file(self):
        while self.dataframe is None:
            file_path = input('Please enter the file path:')
            self.dataframe = self.analyser.extract_property_info(file_path)

        print('File read successful!')

    def choose_function(self):
        print('Welcome to the Investor app, please select the following functions:')
        print('A. Suburb Property Summary')
        print('B. Average Land Size')
        print('C. Property Value Distribution')
        print('D. Sales Trend')
        print('E. Identifying a Property of a Specific Price in a Suburb')
        print('Q. Quit')
        choose = input('Please enter your selection:')

        if choose not in ['A','B','C','D','E','Q']:
            print('Incorrect selection, please reselect.')
            return 1

        if choose == 'A':
            suburb = input('Please enter the suburbs you want to query:')
            self.analyser.suburb_summary(self.dataframe, suburb)
            return 1

        if choose == 'B':
            suburb = input('Please enter the suburbs you want to query:')
            result = self.analyser.avg_land_size(self.dataframe, suburb)
            if result is None:
                print('Suburb does not exist')
            else:
                print('Average Land Size:', result)
            return 1

        if choose == 'C':
            suburb = input('Please enter the suburbs you want to query:')
            target_currency = input('Please enter the currency you want to query:')
            self.visualiser.prop_val_distribution(self.dataframe, suburb, target_currency)
            print('Image generation successful! The file name is:Histogram.png')
            return 1

        if choose == 'D':
            self.visualiser.sales_trend(self.dataframe)
            print('Image generation successful! The file name is:SalesTrend.png')
            return 1

        if choose == 'E':
            suburb = input('Please enter the suburbs you want to query:')
            price = input('Please enter the price you want to query:')
            try:
                price = float(price)
            except:
                print('Price needs to be a numerical value')
                return 1
            self.visualiser.locate_price(price, self.dataframe, suburb)
            return 1

        if choose == 'Q':
            print('Goodbye')
            return 0
