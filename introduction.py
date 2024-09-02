def count_words_in_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            # Read the contents of the file
            content = file.read()

        # Split the content into words
        words = content.split()

        # Count the number of words
        word_count = len(words)

        # Prepare the output content
        output_content = f'The file "{input_file}" contains {word_count} words.'

        # Write the word count to the output file
        with open(output_file, 'w') as file:
            file.write(output_content)

        print(f'Word count written to "{output_file}" successfully.')

    except FileNotFoundError:
        print(f'The file "{input_file}" was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage
input_file = 'sample.txt'
output_file = 'word_count.txt'
count_words_in_file(input_file, output_file)
