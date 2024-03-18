from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    #Your code goes here
    if not m:
        return 0
    s = 0
    l = 0
    for i in m:
        for j in i:
            s += j
            l += 1
    return s/l

def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    #Your code goes here
    point = [0,0]
    t = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > t:
                t = m[i][j]
                point = [i,j]
    return point
def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    #Your code goes here
    h = len(m)
    if c[0] >= h or c[0] < 0 or c[1] >= h or c[1] < 0:
        return False
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if not i and not j:
                continue
            nei = [c[0]+i,c[1]+j]
            if nei[0] >= h or nei[0] < 0 or nei[1] >= h or nei[1] < 0:
                continue
            if m[nei[0]][nei[1]] < m[c[0]][c[1]]:
                return False
    return True

def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    #Your code goes here

    h = len(m)
    c = start
    while True:
        if is_sink(m,c):
            return c
        s = 0
        c1 = [0,0]
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not i and not j:
                    continue
                nei = [c[0] + i, c[1] + j]
                if nei[0] >= h or nei[0] < 0 or nei[1] >= h or nei[1] < 0:
                    continue
                if m[nei[0]][nei[1]] < m[c[0]][c[1]]:
                    if not s:
                        s = m[nei[0]][nei[1]]
                        c1 = [nei[0],nei[1]]
                    else:
                        if m[nei[0]][nei[1]] < s:
                            s = m[nei[0]][nei[1]]
                            c1 = [nei[0], nei[1]]
        c = c1[:]
    
def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    #Your code goes here
    while True:
        if supplies < 0:
            return False
        if s[0] == d[0] and s[1] == d[1]:
            return True
        elif s[0] == d[0] and s[1] != d[1]:
            supplies -= abs(m[s[0]][s[1]] - m[s[0]][s[1] + 1])
            s[1] += 1
        elif s[0] != d[0] and s[1] == d[1]:
            supplies -= abs(m[s[0]][s[1]] - m[s[0] + 1][s[1]])
            s[0] += 1
        else:
            south = abs(m[s[0]][s[1]] - m[s[0] + 1][s[1]])
            east = abs(m[s[0]][s[1]] - m[s[0]][s[1] + 1])
            if south < east:
                supplies -= abs(m[s[0]][s[1]] - m[s[0] + 1][s[1]])
                s[0] += 1
            else:
                supplies -= abs(m[s[0]][s[1]] - m[s[0]][s[1] + 1])
                s[1] += 1

"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m







    
