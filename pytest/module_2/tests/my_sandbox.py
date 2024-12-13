def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read().upper()
    with open(output_file, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    input_test = "this is test text to deal with fixtures."
    with open('input.txt', 'w') as f:
        f.write(input_test)

    process_data('input.txt', 'output.txt')