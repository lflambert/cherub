#Paycheck calculations

#Input Name
name = input("Enter your first and last name: ")

#Input Pay Per Hour
while True:
    try:
        payRate = float(input("Enter Hourly Rate Of Pay: "))
    except ValueError:
        print("Sorry, I didn't understand that. Value must be number.")
        continue
    else:
        break

#Input Hours Worked
while True:
    try:
        hours = float(input("Enter Hours Worked: "))
    except ValueError:
        print("Sorry, I didn't understand that. Value must be a number.")
        continue
    if hours > 168:
        print("You can't work more than 168 hours in a week.")
        continue
    else:
        break

#Taxes and FICA
federaltax = .15
statetax = .10
fica = .02

#Overtime Rate
otrate = 1.5
otpayRate = payRate * otrate  # Calculates overtime pay rate

#Overtime hours
n = hours - 40
if n > 0:
    otHours = n
else:
    otHours = 0

#Nonovertime hours <=40
reghours = hours - otHours

#Compute regular pay
def regpay(reghours, payRate):
    return float((reghours) * payRate)

#Compute overtime pay
def otpay(otHours, otpayRate):
    return float(otHours * otpayRate)

#Deductions and Totals
totalpay = regpay(reghours, payRate) + otpay(otHours, otpayRate)
federaltaxedAmount = round((totalpay * federaltax), 2)
statetaxedAmount = round((totalpay * statetax), 2)
ficataxedAmount = round((totalpay  * fica), 2)
taxedAmount = round((federaltaxedAmount + statetaxedAmount + ficataxedAmount), 2)
afterTaxPay = round((totalpay - taxedAmount),2)

#Print Payroll Information
print("\n Your Name:", name)
print(" Hourly rate:", payRate)
print(" Hours worked:", hours)
print(" Regular Pay:  $", regpay(reghours, payRate))
print(" Overtime Pay:  $", otpay(otHours, otpayRate))
print(" Before Tax Pay:  $", totalpay)
print(" Federal Taxes: $", federaltaxedAmount)
print(" State Taxes: $", statetaxedAmount)
print(" FICA: $", ficataxedAmount)
print(" Total taxes and FICA: $", taxedAmount)
print(" After Tax Pay:  $", afterTaxPay, "\n")
