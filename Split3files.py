def split_file(input_file, train_file, test_file, validation_file, train_percent=0.75, test_percent=0.20):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    train_count = int(total_lines * train_percent)
    test_count = int(total_lines * test_percent)
    
    train_lines = lines[:train_count]
    test_lines = lines[train_count:train_count + test_count]
    validation_lines = lines[train_count + test_count:]
    
    with open(train_file, 'w') as f:
        f.writelines(train_lines)
    with open(test_file, 'w') as f:
        f.writelines(test_lines)
    with open(validation_file, 'w') as f:
        f.writelines(validation_lines)

input_file = 'shuffled195.txt' 

train_file = 'train.txt'
test_file = 'test.txt'
validation_file = 'validation.txt'

split_file(input_file, train_file, test_file, validation_file)

print("File split into train, test, and validation sets successfully.")
