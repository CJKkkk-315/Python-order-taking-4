import csv


def read_exchange_rates_from_file(filename, has_header=True):
    """ Reads a csv file and parses the content field into a time series.

    Parameters:
    -----------

    filename: string
        csv filename
    has_header: bool
        True or False on whether the file contents has a header row

    Return
    ------
    list of tuples with tuple consisting of (currency acronym, currency name, exchange rate)

    """
    currency_rates = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if has_header:
            next(reader, None)
        for row in reader:
            currency_rates.append((row[0], row[1], float(row[2])))
    return currency_rates
