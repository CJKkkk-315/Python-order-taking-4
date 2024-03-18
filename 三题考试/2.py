def draw_parallelogram(Mode, height):
    if Mode == 'right':
        for i in range(height):
            print((height-i-1) * ' ' + '*'*18)
    else:
        for i in range(height):
            print(i * ' ' + '*'*18)


def save_draw_graph(Mode, height):
    with open(f'{Mode}_parallelogram.txt','w') as f:
        if Mode == 'right':
            for i in range(height):
                f.write((height-i-1) * ' ' + '*'*18 + '\n')
        else:
            for i in range(height):
                f.write(i * ' ' + '*'*18 + '\n')

save_draw_graph('left',7)
save_draw_graph('right',7)