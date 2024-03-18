import os
import pandas as pd
import matplotlib.pyplot as plt


def read_csv_file(file_path):
    """
    Read a CSV file and return a DataFrame.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        DataFrame: The data read from the file.
    """
    # Read CSV file using pandas
    data = pd.read_csv(file_path)
    return data


def clean_data(data):
    """
    Clean the data by removing rows with null values.

    Parameters:
        data (DataFrame): The original data.

    Returns:
        DataFrame: The cleaned data.
    """
    # Drop rows with null values
    return data.dropna()


def create_line_chart(data):
    """
    Create a line chart for all variables in the data.

    Parameters:
        data (DataFrame): The data.
    """
    # Plot line chart using matplotlib
    data.plot.line()
    plt.title('Line Chart for All Variables')
    plt.show()


def create_scatter_chart(data, x, y, title):
    """
    Create a scatter chart to visualize the relationship between two variables.

    Parameters:
        data (DataFrame): The data.
        x (str): The variable to plot on the x-axis.
        y (str): The variable to plot on the y-axis.
        title (str): The title of the chart.
    """
    # Plot scatter chart using matplotlib
    plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()


def main():
    """
    The main function of the program.
    """
    while True:
        # Ask user for file name
        file_name = input("Please enter a data file name to be analyzed or 'Q' to quit: ")

        # Break the loop if user wants to quit
        if file_name.lower() == 'q':
            break

        # Check if the file exists
        if os.path.isfile(file_name):
            # Read and clean the data
            data = read_csv_file(file_name)
            data = clean_data(data)

            # Create charts
            create_line_chart(data)

            create_scatter_chart(data, 'Glucose', 'Insulin', 'Glucose vs Insulin')
            create_scatter_chart(data, 'Glucose', 'BloodPressure', 'Glucose vs BloodPressure')
            create_scatter_chart(data, 'BMI', 'Age', 'BMI vs Age')
            create_scatter_chart(data, 'Outcome', 'BloodPressure', 'Outcome vs BloodPressure')
            create_scatter_chart(data, 'Outcome', 'SkinThickness', 'Outcome vs SkinThickness')

            pd.set_option('display.max_rows', 500)
            pd.set_option('display.max_columns', 500)
            pd.set_option('display.width', 1000)
            print('Result of data analysis')
            print('-'*50)
            print(data.corr())
            print('-'*50)

            print('''
------------------------------------------------------------------------------------
•The number varies from -1 to 1.
•Positive relationships go in the same direction.
•1 means that there is a perfect correlation.
•0.8-0.9 is a very strong relationship.
•0.5-0.8 means strong relationship.
•0.3-0.5 means relatively strong relationship. 
•<=0.3 means a weak relationship
------------------------------------------------------------------------------------
            ''')

        else:
            print("The file does not exist, please enter a valid file name.")


if __name__ == "__main__":
    main()
