log_file_path = "./exam.log"

# Reusable function
def get_count_of_errors(log_file_path, search_string):
      try:
            with open(log_file_path, "r") as file:
                  # Read all lines in the log file into a list
                  lines = file.readlines()
                  count = 0

                  # Iterate through the list of lines in the lines array
                  for line in lines:
                        if search_string in line[22:28]:
                              count += 1

                  return count
      except FileNotFoundError:
            # Catch error as a result of the file missing
            return f"The file 'log_file_path' was not found"
      except Exception as e:
            # Catch other errors
            return f"An error occured: {str(e)}"

# Call to the function get_count_of_errors to return the number of "ERROR" in log file
count_of_error = get_count_of_errors(log_file_path, "ERROR")
print(count_of_error)
