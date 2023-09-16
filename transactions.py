log_file_path = "./exam.log"

# Reusable function
def num_transactions(log_file_path, search_string):
      try:
            with open(log_file_path, "r") as file:
                  # Read all lines in the log file into a list
                  lines = file.readlines()
                  count = 0

                  # Iterate through the list of lines in the lines array
                  for line in lines:
                        if search_string in line[35:]:
                              count += 1

                  return count
      except FileNotFoundError:
            # Catch error as a result of the file missing
            return f"The file 'log_file_path' was not found"
      except Exception as e:
            # Catch other errors
            return f"An error occured: {str(e)}"

# Call to the function num_transactions to return the number of transactions in log file
num_of_transactions = num_transactions(log_file_path, "transaction done, ")
print(num_of_transactions)
