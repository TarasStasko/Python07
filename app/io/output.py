def console_write(text):
    """
    Function to write text to the console.

    Args:
        text (str): The text to be written to the console.
    """
    print(text)


def file_write(file_path, text):
    """
    Function to write text to a file.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(text)


