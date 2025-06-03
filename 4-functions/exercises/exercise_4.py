def compute_pay():
    hours = int(input("Please enter the number of hours you've worked: "))
    rate = int(input("Please enter the rate: "))
    if hours > 40:
        overtime_hours = hours - 40
        pay = ((pay-overtime_hours)*rate)+(overtime_hours*(rate*1.5))
    else:
        pay = hours*rate

    print("Pay: ", pay)

compute_pay()