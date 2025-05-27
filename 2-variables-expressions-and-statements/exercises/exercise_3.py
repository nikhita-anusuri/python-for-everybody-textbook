# prompts user for a celsius temperature and converts
# the temp to fahrenheit
temp_in_c = float(input("Please enter a temperature (celsius): "))
temp_in_f = (temp_in_c * 1.8) + 32
print("The temperature in fahrenheit is: " , temp_in_f)