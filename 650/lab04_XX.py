# siyu yin
# csce 101-002
# 2023.02.09
# ysiyu@email.sc.edu
# Lab1

def calc_area(width,height):
    area = width * height
    return area

def calc_perimeter(width,height):
    perimeter = width * 2 + height * 2
    return perimeter

width = int(input('Input the width:'))
height = int(input('Input the height:'))
area = calc_area(width,height)
perimeter = calc_perimeter(width,height)
print(f'The area is {area} and perimeter is {perimeter}')