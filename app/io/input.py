import pandas as pd


def input_text():
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    input_t = input("Enter your text here: ")
    return input_t


def read_from_file(file_path):
    """
    Function to read text from a file.

    Args:
        file_path (str): The path to the file from which to read the text.

    Returns:
        str: The content read from the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def pandas_read(file_path):
    """
    Function to read text from a CSV file using pandas.

    Args:
        file_path (str): The path to the CSV file from which to read the text.

    Returns:
        str: The content read from the CSV file.
    """

    data = pd.read_csv(file_path)
    text = data.iloc[0, 0]
    return text


