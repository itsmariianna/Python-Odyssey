# Store functions for converting temperatures between Celsius, Fahrenheit, and Kelvin in a dictionary. Write a function convert_temperature(value, from_unit, to_unit) that uses this dictionary to perform the conversion.

temperature_conversions = {
    ('Celsius', 'Fahrenheit'): lambda c: c * 9/5 + 32,
    ('Celsius', 'Kelvin'): lambda c: c + 273.15,
    ('Fahrenheit', 'Celsius'): lambda f: (f - 32) * 5/9,
    ('Fahrenheit', 'Kelvin'): lambda f: (f - 32) * 5/9 + 273.15,
    ('Kelvin', 'Celsius'): lambda k: k - 273.15,
    ('Kelvin', 'Fahrenheit'): lambda k: (k - 273.15) * 9/5 + 32
}

def convert_temperature(value, from_unit, to_unit):
    try:
        return temperature_conversions[(from_unit, to_unit)](value)
    except KeyError:
        return "Invalid request"

print(convert_temperature(37,'Celsius', 'Fahrenheit'))
print(convert_temperature(67,'Fahrenheit', 'Celsius'))
print(convert_temperature(280,'Kelvin', 'Fahrenheit'))
print(convert_temperature(10,'Fahrenheit', 'Kelvin'))