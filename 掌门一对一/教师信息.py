import requests
import json
tid_drop = {}
def get_student_ids(start, end):
    sids = []
    for i in range(start, end+1):
        print(f'正在抓取第{i}页学生信息')
        url = "https://partner.zmlearn.com/api/student-tag/student/queryForPage"

        payload = '{' + f'"stuMobile":"","sortField":"responseTime","sortType":"desc","pageNo":{i},"pageSize":50,"state":"","tmkRemoveList":false,"isImport":false,"isTodayTodo":false,"districtId":"2917","teamId":"9626","sellerId":"177665","studentName":"","is7DaysUnContacted":false,"is14DaysUnTranslated":false,"is14DaysUnTranslatedFinished":false,"isPlanTodayFinished":false,"isTrialType":false,"todoNameList":[],"accountNumber":"","tagIds":[],"buId":102,"positionCode":"CC"'+ '}'
        headers = {
            'Connection': 'close',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'PARTNER_TOKEN=ca6359cf7b79307317896466dcc39a33a5c184b6a952ccf8456461efa8161fac; acw_tc=2f624a5717002086398944264e5f2e9aa5bb595db2351f3096cdc1605feb43; acw_tc=2f624a3a17002087556463938e24a23d0dd97f9a61a18c62e8673687f31a7d'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        for row in data['data']['list']:
            sids.append(row['studentId'])
    return sids
def get_teacher_ids(sids):
    print(f'共{len(sids)}条学生信息，抓取教师信息')
    tids = []
    for sid in sids:

        url = "https://partner.zmlearn.com/api/zmbiz-csc-frontend-sale/studentLesson/queryStuTestLessonPage"

        payload = '{' + f'"studentId":{sid},"pageNo":1,"pageSize":10' + '}'
        headers = {
            'Connection': 'close',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'PARTNER_TOKEN=ca6359cf7b79307317896466dcc39a33a5c184b6a952ccf8456461efa8161fac; acw_tc=2f624a5717002086398944264e5f2e9aa5bb595db2351f3096cdc1605feb43; getTeaNameShowLine=1700217283891; acw_tc=2f624a3a17002087556463938e24a23d0dd97f9a61a18c62e8673687f31a7d'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = json.loads(response.text)
        for row in data['data']['list']:
            if row['teacherId'] not in tid_drop:
                tid_drop[row['teacherId']] = 1
                tids.append([row['teacherId'],row['teacherEncryptId'], row['grade'] + row['subject'] + row['pkgTypeName']])
    return tids

def get_teacher_info(tids):
    print(f'共{len(tids)}条教师信息，抓取具体信息')
    final_ans = []
    for tid in tids:

        url = f"https://partner.zmlearn.com/api/zmbiz-csc-frontend-sale/teacher/getTeacherInfo?teacherId={tid[0]}&teacherEncryptId={tid[1]}"

        payload = {}
        headers = {
            'Connection': 'close',
            'Cookie': 'PARTNER_TOKEN=ca6359cf7b79307317896466dcc39a33a5c184b6a952ccf8456461efa8161fac; acw_tc=2f624a5717002086398944264e5f2e9aa5bb595db2351f3096cdc1605feb43; acw_tc=2f624a3a17002087556463938e24a23d0dd97f9a61a18c62e8673687f31a7d'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        phone, wechat = get_phone_wechat(tid)
        name = data['data']['name']
        gender = data['data']['gender']
        school = data['data']['school']
        if data['data']['teacherStatus'] == 0:
            online = '在职'
        elif data['data']['teacherStatus'] == 2:
            online = '离职'
        else:
            online = ''
        final_ans.append([name, phone, wechat, gender, school, online, tid[2]])
    return final_ans

def get_phone_wechat(tid):

    url = "https://partner.zmlearn.com/api/zmbiz-csc-frontend-sale/teacher/getTeacherSecretInfoNew"
    payload = '{' + f'"teacherEncryptId":"{tid[1]}","queryType":0' + '}'
    headers = {
        'Connection': 'close',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'PARTNER_TOKEN=ca6359cf7b79307317896466dcc39a33a5c184b6a952ccf8456461efa8161fac; acw_tc=2f624a3e17002104403404427e532ff34c09b7b1619d389a7561b91d3073b5'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    wechat = json.loads(response.text)['data']

    payload = '{' + f'"teacherEncryptId":"{tid[1]}","queryType":1' + '}'
    response = requests.request("POST", url, headers=headers, data=payload)
    phone = json.loads(response.text)['data']
    return phone, wechat

sids = get_student_ids(1,10)
tids = get_teacher_ids(sids)
final_ans = get_teacher_info(tids)
print(*final_ans,sep='\n')