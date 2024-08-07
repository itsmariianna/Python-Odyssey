# Store functions for common data analysis operations (e.g., mean, median, mode, standard deviation) in a dictionary. Write a function analyze_data(data, operation) that uses this dictionary to perform the requested analysis on a list of numbers.
from statistics import mean, median, mode, stdev

data_analysis_operations = {'mean' : mean,
                            'median': median,
                            'mode' : mode,
                            'standard deviation' : stdev}


def analyze_data(data, operation):
    if not data:
        return "There is no data here"
    
    elif operation in data_analysis_operations:
        try:
            return data_analysis_operations[operation](data)
        except Exception as e:
            return f'ERROR: {e}'
    else:
        return "There is no such operation"

print(analyze_data([1, 2, 3, 4, 5, 6], 'median'))
print(analyze_data([1, 2, 3, 4, 5, 6], 'sum'))
print(analyze_data([1], 'standard deviation'))
