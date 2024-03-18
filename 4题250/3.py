data = open('cds_from_genomic.txt').read().split('>lc')
data = [i for i in data if i]
d = {}
for i in data:
    idd = i.split('\n')[0].split('|')[1].split()[0]
    d[idd] = ''.join(i.split('\n')[1:])
r = open('gene_id.txt').read().split('\n')
r = [i for i in r if i]
with open('cds_seq.txt','w') as f:
    for i in r:
        f.write(i+'\n')
        f.write(d[i]+'\n')
