print('Welcome to the Global Energy bill calculator!')
input('Enter your account number.\n')
mouth = input('Enter the month number (e.g., for January, enter 1).\n')

e_type = input('Enter your electricity plan (EFIR or EFLR).\n')
e_use = int(input(f'Enter the amount of electricity you used in month {mouth} (in kWh).\n'))
g_type = input('Enter your gas plan (GFIR or GFLR).\n')
g_use = int(input(f'Enter the amount of gas you used in month {mouth} (in GJ).\n'))

p = input('Enter the abbreviation for your province of residence (two letters).\n')
t = [['AB','BC','MB','NT','NU','QC','SK','YT'],['ON'],['NB','PE','NL','NS']]
money = 0

if e_type == 'EFIR':
    if e_use <= 1000:
        money += e_use*8.36
    else:
        money += 1000*8.36 + (e_use-1000)*9.41
elif e_type == 'EFLR':
    money += e_use*9.11


if g_type == 'GFIR':
    if e_use <= 950:
        money += g_use*4.56
    else:
        money += 950*4.56 + (g_use-950)*5.89
elif g_type == 'GFLR':
    money += g_use*3.93
money *= 0.01
money += 1.32
money += 120.62
if p in t[0]:
    money *= 1.05
elif p in t[1]:
    money *= 1.13
elif p in t[2]:
    money *= 1.15

print(f'Thank you! Your total amount due now is: ${round(money,2)}')

