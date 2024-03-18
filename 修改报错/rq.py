import requests
def file2json(filename):
    txt_data = open(filename,encoding='UTF8').read().split('\n')
    start_idx = 1
    now_idx = 0
    need_idx = 1
    content = ""
    flag = 0
    print(len(txt_data))
    for i in txt_data:
        if i.split(')')[0] == str(start_idx):
            flag = 1
        if flag:
            if i.split(')')[0] == str(need_idx):
                if now_idx:
                    print(content)
                    res = requests.get(f'https://services.bioportal.lirmm.fr/annotator?text={content}&apikey=1de0a270-29c5-4dda-b043-7c3580628cd5').text
                    with open('res_json/' + filename + str(now_idx) + '.json','w',encoding='UTF8') as f:
                        f.write(res)
                    content = ""
                now_idx += 1
                need_idx += 1
            content += i
    res = requests.get(f'https://services.bioportal.lirmm.fr/annotator?text={content}&apikey=1de0a270-29c5-4dda-b043-7c3580628cd5').text
    with open('res_json/' + filename + str(now_idx) + '.json','w',encoding='UTF8') as f:
        f.write(res)
file2json('train1.txt')