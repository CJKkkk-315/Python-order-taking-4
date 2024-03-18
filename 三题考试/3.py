books_info = []
with open('books.txt') as f:
    rows = f.read().split('\n')
    for row in rows:
        sm,zz,bh,kc = row.split('\t')
        books_info.append({'书名': sm, '作者': zz, 'ISBN 编号': bh, '库存数量': int(kc)})
print(books_info)

def add_book_info(books_info,title,author,ISBN,stock):
    for i in books_info:
        if title == i['书名']:
            print('系统中已存在此书')
            return
    books_info.append({'书名': title, '作者': author, 'ISBN 编号': ISBN, '库存数量': stock})

add_book_info(books_info,'snow country','Yasunari Kawabata','008X',3)

def search_books(books_info,author):
    res = []
    for i in books_info:
        if i['作者'] == author:
            res.append(i)
    res.sort(key=lambda x:len(x['书名']))
    for i in res:
        print(i)
search_books(books_info,'Haruki Murakami')

def borrow_book(books_info,ISBN):
    for i in books_info:
        if i['ISBN 编号'] == ISBN:
            if i['库存数量'] == 0:
                print('库存不足')
            else:
                i['库存数量'] -= 1
    with open('books_update.txt','w') as f:
        for i in books_info:
            f.write(i['书名'] + '\t' + i['作者'] + '\t' + i['ISBN 编号'] + '\t' + str(i['库存数量']) + '\n')

borrow_book(books_info,'402X')