
input_file = 'ENCFF789TLJ_Neg_output.txt'
output_file = 'Combine195.txt'

with open(input_file, 'r') as f_input, open(output_file, 'a') as f_output:
    for line in f_input:
        strip_line = line.strip()
        chopped_line = strip_line[:195]
        modified_line = "0 " + chopped_line + "\n"
        f_output.write(modified_line)

print(f"{input_file} complete")

