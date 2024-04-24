import random


def shuffle_file_lines(input_file, output_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    random.shuffle(lines)
    
    with open(output_file, 'w') as f:
        f.writelines(lines)

input_file = 'Combine195.txt'
shuffled_output_file = 'shuffled195.txt'

shuffle_file_lines(input_file, shuffled_output_file)

print("Lines shuffled successfully.")
