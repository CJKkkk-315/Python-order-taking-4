#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'

#we'll start with an empty list of days (tip: when you're testing,
#you can put some data in here so you don't need to manually add data each
#time, just be sure to set it back to an empty list after you're done)
plastic_removed = []

#loop until the user chooses to end
while(menu_option != 'E'):
    #another fun hack, if you use a triple quoted (""") string, you
    #can add line breaks and it will still print nicely
    menu_string = """
    A = Add data
    T = Get Total kg of Plastic Removed
    O = Get Number of Overload Days
    E = End program
    Choose an option:
    """
    menu_option = input(menu_string)
    if menu_option not in ['A','T','O','E']:
        print('please try again and present the menu again.')
        continue
    if menu_option == 'A':
        plastic = int(input(f'Enter kg of plastic removed on day {len(plastic_removed) + 1}:'))
        plastic_removed.append(plastic)
    if menu_option == 'T':
        sub_option = input('Please enter A (for the total removed in all days entered) or R (for the total removed in a range of days):')
        if sub_option == 'A':
            s = 0
            for i in range(len(plastic_removed)):
                s += plastic_removed[i]
            print(f'Remove total of {s}')
        if sub_option == 'R':
            start = int(input('Please enter the start date:'))
            end = int(input('Please enter the end date:'))
            s = 0
            for i in range(start - 1, end, 1):
                s += plastic_removed[i]
            print(f'Remove total of {s}')
    if menu_option == 'O':
        sub_option = input('Please enter A (for the all overload days) or R (for overload days within a range of days.):')
        threshold = int(input('Please enter the threshold (max kg rigs are meant to collect):'))
        if sub_option == 'A':
            s = 0
            for i in range(len(plastic_removed)):
                if plastic_removed[i] > threshold:
                    s += 1
            print(f'The total number of days is {s}')
        if sub_option == 'R':
            start = int(input('Please enter the start date:'))
            end = int(input('Please enter the end date:'))
            s = 0
            for i in range(start - 1, end, 1):
                if plastic_removed[i] > threshold:
                    s += 1
            print(f'The total number of days is {s}')
    if menu_option == 'E':
        break


#####Here's some totally unrelated code that you might find helpful
unrelated_list = [4, 9, 7, 10, 12, 10, 14, 4, 10, 7]
start_position = 2
end_position = 6

sum_values = 0
count_of_tens = 0

# for no particular reason, let's loop through a section of a list
# and sum all the values in that section, and also count values
# that meet a certain criteria... equal to 10 in this case
for position in range(start_position, end_position, 1):
    current_value = unrelated_list[position]
    print("The value at position " + str(position) + " is: " + str(current_value))
    sum_values = sum_values + current_value
    print("The sum so far is: " + str(sum_values))
    if(current_value == 10):
        count_of_tens = count_of_tens + 1
        print("We have seen " + str(count_of_tens) + " 10s so far")