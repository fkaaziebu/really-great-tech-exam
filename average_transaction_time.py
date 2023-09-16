import datetime
log_file_path = "./exam.log"

def convert_time_to_millis(time_str):
      time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S.%f")
      return ((time_obj.hour*3600 + time_obj.minute*60 + time_obj.second)*1000 + \
              time_obj.microsecond / 1000)

# Reusable function
def average_trans_time(log_file_path, search_string):
      try:
            with open(log_file_path, "r") as file:
                  # Read all lines in the log file into a list
                  lines = file.readlines()
                  count = 0
                  sum_of_time = 0

                  # Iterate through the list of lines in the lines array
                  for i, line in enumerate(lines):
                        if search_string in line[35:]:
                              transaction_time = convert_time_to_millis(lines[i + 1][10:22]) - convert_time_to_millis(line[10:22])
                              sum_of_time += transaction_time
                              count += 1
                  return sum_of_time // count
      except FileNotFoundError:
            # Catch error as a result of the file missing
            return f"The file 'log_file_path' was not found"
      except Exception as e:
            # Catch other errors
            return f"An error occured: {str(e)}"

# Call to the function average_trans_time to return the number of transactions in log file
average_time = average_trans_time(log_file_path, "transaction done, ")
print(average_time)
