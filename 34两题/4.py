import threading
import math


def calc_areaOfRectangle(name,length,width):
    print(f'{name}:[{length*width}]')


def calc_areaOfCircle(name,radius):
    print(f'{name}:[{math.pi*radius**2}]')


if __name__ == '__main__':
    length1 = float(input('Please enter length of rectangle1:'))
    width1 = float(input('Please enter width of rectangle1:'))
    length2 = float(input('Please enter length of rectangle2:'))
    width2 = float(input('Please enter width of rectangle2:'))
    radius1 = float(input('Please enter the radius of circle 1:'))
    radius2 = float(input('Please enter the radius of circle 2:'))
    thread_1 = threading.Thread(target=calc_areaOfRectangle,args=('Rectangle 1',length1,width1))
    thread_2 = threading.Thread(target=calc_areaOfRectangle, args=('Rectangle 2', length2, width2))
    thread_3 = threading.Thread(target=calc_areaOfCircle, args=('Circle 1',radius1,))
    thread_4 = threading.Thread(target=calc_areaOfCircle, args=('Circle 2',radius2,))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
