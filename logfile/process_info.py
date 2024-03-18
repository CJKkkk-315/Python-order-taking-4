import sys
commands = sys.argv[1:]
if not commands:
    print('Missing option')
    exit(0)
if commands[0] not in ['-a','-s','-m','-t','-v']:
    print('Wrong option')
    exit(0)
if len(commands) == 1:
    print('Missing the filename argument')
    exit(0)
with open('log_file') as f:
    data = f.read()
lines = [i for i in data.split('\n') if i]
lines = [i.split() for i in lines]

if commands[0] == '-a':
    if not lines:
        print('No processes found')
        exit(0)
    lines.sort(key=lambda x:x[3])
    for line in lines:
        print(' '.join(line))
    exit(0)

if commands[0] == '-m':
    if not lines:
        print('No processes found')
        exit(0)
    total_memory = 0
    for line in lines:
        total_memory += int(line[1])
    print(f'Total memory size: {total_memory} KB')
    exit(0)

if commands[0] == '-t':
    if not lines:
        print('No processes found')
        exit(0)
    total_time = 0
    for line in lines:
        total_time += int(line[2])
    print(f'Total CPU time: {total_time} seconds')
    exit(0)

if commands[0] == '-s':
    try:
        res = []
        threshold = int(commands[1])
        for line in lines:
            if int(line[1]) >= threshold:
                res.append(line)
        if not res:
            print('No processes found with the specified memory size')
            exit(0)
        else:
            for line in res:
                print(' '.join(line))
    except:
        print('Missing the memory threshold argument')

if commands[0] == '-v':
    print('name:aa,surname:bb,student ID:123456,completion date:2022-10-27')
