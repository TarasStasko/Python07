from app.io.input import input_text, read_from_file, pandas_read


def main():

    input_text_result = input_text()
    print("Input text:", input_text_result)

    with open("test.txt", "w") as file:
        file.write(input_text_result)
    print("Input text has been written to 'test.txt'.")

    read_from_file_result = read_from_file("test.csv")

    print("Text read from file:", read_from_file_result)

    with open("test.txt", "a") as file:
        file.write("\n" + read_from_file_result)
    print("Text read from file has been appended to 'test.txt'.")

    pandas_read_result = pandas_read("test.csv")

    print("Text read from file using Pandas:", pandas_read_result)

    with open("test.txt", "a") as file:
        file.write("\n" + str(pandas_read_result))
    print("Text read from file using Pandas has been appended to 'test.txt'.")


if __name__ == '__main__':
    main()
