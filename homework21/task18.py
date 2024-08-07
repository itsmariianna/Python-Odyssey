# Create a dictionary with functions for various financial calculations (e.g., compound interest, loan payment, investment return). Write a function financial_calculator(operation, **kwargs) that uses this dictionary to perform the requested calculation.
financial_calculations = {
    'compound interest': lambda principal, rate, time, times_per_year: principal * (1 + rate / times_per_year) ** (times_per_year * time),
    'loan payment': lambda principal, annual_rate, num_payments: (principal * annual_rate / 12) / (1 - (1 + annual_rate / 12) ** (-num_payments)),
    'investment return': lambda initial_amount, annual_rate, years: initial_amount * (1 + annual_rate) ** years
}

def financial_calculator(operation, **kwargs):
    if operation in financial_calculations:
        try:
            return financial_calculations[operation](**kwargs)
        except TypeError:
            return 'Missing argument'
    else:
        return "There is no such financlial calculation"
    
print(financial_calculator('compound interest', principal=1000, rate=0.05, time=10, times_per_year=4))
print(financial_calculator('loan payment', principal=30000, annual_rate=0.07, num_payments=60))
print(financial_calculator('investment return', initial_amount=5000, annual_rate=0.08, years=5))
print(financial_calculator('loan payment', principal=30000, annual_rate=0.07))
print(financial_calculator('payment', principal=30000, annual_rate=0.07))
