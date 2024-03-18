
AFL_TEAMS = [['Adelaide', 'the Adelaide Oval'], ['Brisbane', 'the Gabba'],
             ['Carlton', 'the MCG'], ['Collingwood', 'the MCG'],
             ['Essendon', 'the MCG'], ['Fremantle', 'Optus Stadium'],
             ['Geelong', 'the MCG'], ['Gold Coast', 'the Gabba'],
             ['Greater Western Sydney', 'Giants Stadium'],
             ['Hawthorn', 'the MCG'], ['Melbourne', 'the MCG'],
             ['North Melbourne', 'the MCG'],
             ['Port Adelaide', 'the Adelaide Oval'],
             ['Richmond', 'the MCG'], ['St Kilda', 'the MCG'],
             ['Sydney', 'the SCG'], ['West Coast', 'Optus Stadium'],
             ['Western Bulldogs', 'the MCG']]


import random

def vs(team_A,team_B,place,level):
    drew_flag = 0
    team_A_g = random.randint(12,22)
    team_A_b = random.randint(12,22)
    team_B_g = random.randint(10,22)
    team_B_b = random.randint(10,22)
    score_A = team_A_g*8+team_A_b*1
    score_B = team_B_g*8+team_B_b*1
    while score_A == score_B:
        drew_flag = 1
        print(f'{team_A} {team_A_g}.{team_A_b} ({score_A}) drew with {team_B} {team_B_g}.{team_B_b} ({score_B}) in the {level} at {place}.')
        team_A_g = random.randint(12, 22)
        team_A_b = random.randint(12, 22)
        team_B_g = random.randint(10, 22)
        team_B_b = random.randint(10, 22)
        score_A = team_A_g * 8 + team_A_b * 1
        score_B = team_B_g * 8 + team_B_b * 1
    if score_A > score_B:
        win_team = team_A
        win_team_g = team_A_g
        win_team_b = team_A_b
        win_team_score = score_A
        lose_team = team_B
        lose_team_g = team_B_g
        lose_team_b = team_B_b
        lose_team_score = score_B
    else:
        win_team = team_B
        win_team_g = team_B_g
        win_team_b = team_B_b
        win_team_score = score_B
        lose_team = team_A
        lose_team_g = team_A_g
        lose_team_b = team_A_b
        lose_team_score = score_A
    if drew_flag:
        print(f'In the replay, {win_team} {win_team_g}.{win_team_b} ({win_team_score}) defeated {lose_team} {lose_team_g}.{lose_team_b} ({lose_team_score}).')
    else:
        print(f'{win_team} {win_team_g}.{win_team_b} ({win_team_score}) defeated {lose_team} {lose_team_g}.{lose_team_b} ({lose_team_score}) in the {level} at {place}.')
    return win_team,lose_team
ALL_TEAMS = []
for team in AFL_TEAMS:
    ALL_TEAMS.append(team[0])
four_team = input('Which teams are playing in the AFL finals this year? ').split(',') # Melbourne,Sydney,Brisbane,Adelaide
flag = 1
if len(four_team) == 4:
    for team in four_team:
        if team not in ALL_TEAMS:
            print('Error input!')
            flag = 0
else:
    print('Error input!')
    flag = 0


if flag:
    place = ''
    for i in AFL_TEAMS:
        if four_team[2] == i[0]:
            place = i[1]
    F_win_team,F_lose_team = vs(four_team[2],four_team[3],place,'the First Semi-Final')
    for i in AFL_TEAMS:
        if four_team[0] == i[0]:
            place = i[1]
    S_win_team,S_lose_team = vs(four_team[0],four_team[1],place,'the Second Semi-Final')
    for i in AFL_TEAMS:
        if S_lose_team == i[0]:
            place = i[1]
    P_win_team,P_lose_team = vs(S_lose_team,F_win_team,place,'the Preliminary Final')

    G_win_team,G_lose_team = vs(S_win_team,P_win_team,'the MCG','the Grand Final')


#
# Which teams are playing in the AFL finals this year? Melbourne,Sydney,Brisbane,Adelaide
#
# Brisbane 16.12 (108) defeated Adelaide 11.10 (76) in the First Semi-Final at the Gabba.
#
# Melbourne 18.12 (120) defeated Sydney 10.12 (72) in the Second Semi-Final at the MCG.
#
# Sydney 14.13 (97) drew with Brisbane 13.19 (97) in the Preliminary Final at the SCG.
# In the replay, Sydney 16.14 (110) defeated Brisbane 11.11 (77).
#
# Melbourne 22.12 (144) defeated Sydney 15.18 (108) in the Grand Final at the MCG.