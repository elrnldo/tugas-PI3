def calculate_sum_from_file(filename):
  """
  Reads integer numbers from a text file, calculates the sum, and formats it with comma separators and two digits.

  Args:
      filename: The name of the text file containing the numbers.
  """

  total_sum = 0
  try:
    with open(filename, 'r') as file:
      for line in file:
        # Read each line, convert to integer, and add to the sum
        total_sum += int(line.strip())
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  else:
    # Format the sum with comma separators and two decimal places
    formatted_sum = "{:,.2f}".format(total_sum)
    print(formatted_sum)

# Specify the filename
filename = "indata.txt"

# Call the function to calculate and print the sum
calculate_sum_from_file(filename)