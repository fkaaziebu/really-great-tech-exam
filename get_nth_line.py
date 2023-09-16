log_file_path = "./exam.log"

# Reusable function to get nth line of log file
def get_nth_line(log_file_path, n):
      try:
            with open(log_file_path, "r") as file:
                  # Read all lines in the log file into a list
                  lines = file.readlines()

                  # Check if n is within a valid range
                  if 1 <= n <= len(lines):
                        return lines[n - 1]
                  else:
                        return f"Line {n} is out of range for file"
      except FileNotFoundError:
            # Catch error as a result of the file missing
            return f"The file 'log_file_path' was not found"
      except Exception as e:
            # Catch other errors
            return f"An error occured: {str(e)}"

# Call to the function get_nth_line to return the first line of the log
# This returns everything in the first line as a string
first_line = get_nth_line(log_file_path, 1)
print(first_line)