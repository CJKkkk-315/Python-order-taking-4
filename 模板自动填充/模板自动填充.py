idx = int(input()) - 1
try:
    all_keywords = open('input.txt',encoding='utf8').read()
except:
    all_keywords = open('input.txt').read()
result = ""
for keywords in all_keywords.split('\n'):
    z = []
    q = []
    for keyword in keywords.split():
        if keyword[0] == '轴':
            z.append([keyword[1],keyword.split('=')[1]])
        else:
            q.append([keyword[1],keyword.split('=')[1]])
    for i in range(len(q)):
        if q[i][1] == '前进':
            q[i].append('正限')
        else:
            q[i].append('负限')
    if not z and not q:
        tem = f"""
            {idx+1}:
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
        """
        idx += 1
    elif not z:
        item1 = ""
        for i in q:
            item1 += f'            "气{i[0]}".{i[1]} := 1;\n'
        item1 += '\n'
        item2 = "            IF "
        item2 += ' AND '.join([f'"气{i[0]}".{i[2]}' for i in q])
        item2 += ' THEN'
        item3 = ""
        for i in q:
            item3 += f'            "气{i[0]}".{i[1]} := 0;\n'
        tem = f"""
            {idx+1}:
{item1[:-1]}
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
            {idx+2}:
{item2}
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+3}:
{item3[:-1]}
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
                """
        idx += 3
    elif not q:
        item1 = ""
        for i in z:
            item1 += f'            "轴{i[0]}".位置 := "位{i[0]}".{i[1]};\n'
            item1 += f'            "轴{i[0]}".速度 := "位{i[0]}".自动速度;\n'
            item1 += f'            "轴{i[0]}".绝对 := 1;\n\n'
        item1 += "            IF "
        item1 += ' AND '.join([f'"轴{i[0]}".done' for i in z])
        item1 += ' THEN'
        item2 = ""
        for i in z:
            item2 += f'            "轴{i[0]}".绝对 := 0;\n'
        item3 = "            IF "
        item3 += ' AND '.join([f'NOT"轴{i[0]}".done' for i in z])
        item3 += ' THEN'
        tem = f"""
            {idx+1}:
{item1}
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+2}:
{item2[:-1]}
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
            {idx+3}:
{item3}
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+4}:
                IF "m8012p" THEN
                    "流程".泡.等待 := "流程".泡.等待 + 1;
                END_IF;
                IF "流程".泡.等待 >= 1 THEN
                    "流程".泡.等待 := 0;
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+5}:
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
                    """
        idx += 5
    else:
        item1 = ""
        for i in z:
            item1 += f'            "轴{i[0]}".位置 := "位{i[0]}".{i[1]};\n'
            item1 += f'            "轴{i[0]}".速度 := "位{i[0]}".自动速度;\n'
            item1 += f'            "轴{i[0]}".绝对 := 1;\n\n'
        for i in q:
            item1 += f'            "气{i[0]}".{i[1]} := 1;\n\n'
        item1 += "            IF "
        item1 += ' AND '.join([f'"轴{i[0]}".done' for i in z])
        item1 += ' AND '
        item1 += ' AND '.join([f'"气{i[0]}".{i[2]}' for i in q])
        item1 += ' THEN'
        item2 = ""
        item3 = "            IF "
        item3 += ' AND '.join([f'NOT"轴{i[0]}".done' for i in z])
        item3 += ' THEN'
        for i in z:
            item2 += f'            "轴{i[0]}".绝对 := 0;\n'
        for i in q:
            item2 += f'            "气{i[0]}".{i[1]} := 0;\n'
        tem = f"""
            {idx+1}:
{item1}
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+2}:
{item2}
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
            {idx+3}:
{item3}
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;          
            {idx+4}:
                IF "m8012p" THEN
                    "流程".泡.等待 := "流程".泡.等待 + 1;
                END_IF;
                IF "流程".泡.等待 >= 1 THEN
                    "流程".泡.等待 := 0;
                    "流程".泡.顺序 := "流程".泡.顺序 + 1;
                END_IF;
            {idx+5}:
                "流程".泡.顺序 := "流程".泡.顺序 + 1;
    
        """
        idx += 5
    result += tem
with open('result.txt','w') as f:
    f.write(result)