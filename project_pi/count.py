with open('pi-1million.txt', 'r') as file:
    pi = file.read()


digit_counts = {str(digit): 0 for digit in range(10)}

for digit in pi:
    if digit.isdigit():
        digit_counts[digit] += 1


with open('counts_of_pi', 'w') as output_file:
    output_file.write('Using Pi with million digits\nthese are the counts of 0-9 digits used in Pi number\n\n\n')
    for digit, count in digit_counts.items():
        output_file.write(f'A digit {digit} has been used: {count} times\n')

print('Done!')