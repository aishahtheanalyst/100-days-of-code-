# if the bill was £150, split between 5 people, with 12% tip.
# each person should pay (150.00 / 5) * 1.12
# round the result to 2 decimal places = 33.60

print('Welcome to the tip calculator.')

bill = float(input('What was the total bill? £'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = '{:.2f}'.format(bill_per_person)

print(f'Each person should pay: £{final_amount}')
