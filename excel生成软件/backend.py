all_cl = []
#东外墙
time_0_23 = "0:00	1:00	2:00	3:00	4:00	5:00	6:00	7:00	8:00	9:00	10:00	11:00	12:00	13:00	14:00	15:00	16:00	17:00	18:00	19:00	20:00	21:00	22:00	23:00".split()
dqtw1 = "38.5 	38.4 	38.2 	38.0 	37.6 	37.3 	36.9 	36.4 	36.0 	35.5 	35.2 	35.0 	35.0 	35.2 	35.6 	36.1 	36.6 	37.1 	37.5 	37.9 	38.2 	38.4 	38.5 	38.6".split()
td = [0.7 for i in range(len(time_0_23))] #ia
qka = "1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03	1.03".split()
qkb = "0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94	0.94".split()
dtwl = [(float(i1)+float(i2))*float(i3)*float(i4) for i1,i2,i3,i4 in zip(dqtw1, td, qka, qkb)]
tmp_in = [25 for _ in range(len(time_0_23))] #ie
crk = [1.5 for _ in range(len(time_0_23))] #if
dqarea = [29.59 for _ in range(len(time_0_23))] #ii
dcl = [float(i3)*float(i4)*(float(i1)-float(i2)) for i1,i2,i3,i4 in zip(dtwl, tmp_in, crk, dqarea)]
dtwl = [round(i,3) for i in dtwl]
dcl = [round(i,3) for i in dcl]
all_cl.append(dcl)
# 南外墙
nqtw1 = "36.1 	36.2 	36.2 	36.1 	35.9 	35.6 	35.3 	35.0 	34.6 	34.2 	33.9 	33.5 	33.2 	32.9 	32.8 	32.9 	33.1 	33.4 	33.9 	34.4 	34.9 	35.3 	35.7 	36.0 ".split()
ntwl = [(float(i1)+float(i2))*float(i3)*float(i4) for i1,i2,i3,i4 in zip(nqtw1, td, qka, qkb)]
nqarea = [29.59 for _ in range(len(time_0_23))] #ij
ncl = [float(i3)*float(i4)*(float(i1)-float(i2)) for i1,i2,i3,i4 in zip(ntwl, tmp_in, crk, nqarea)]
ntwl = [round(i,3) for i in ntwl]
ncl = [round(i,3) for i in ncl]
all_cl.append(ncl)
# 西外墙
xqtw1 = "38.5 	38.9 	39.1 	39.2 	39.1 	38.9 	38.6 	38.2 	37.8 	37.3 	36.8 	36.3 	35.9 	35.5 	35.2 	34.9 	34.8 	34.8 	34.9 	35.3 	35.8 	36.5 	37.3 	38.0 ".split()
xtwl = [(float(i1)+float(i2))*float(i3)*float(i4) for i1,i2,i3,i4 in zip(xqtw1, td, qka, qkb)]
xqarea = [30.94 for _ in range(len(time_0_23))] #ik
xcl = [float(i3)*float(i4)*(float(i1)-float(i2)) for i1,i2,i3,i4 in zip(xtwl, tmp_in, crk, xqarea)]
xtwl = [round(i,3) for i in xtwl]
xcl = [round(i,3) for i in xcl]
all_cl.append(xcl)
# 北外墙
bqtw1 = "33.1 	33.2 	33.2 	33.2 	33.1 	33.0 	32.8 	32.6 	32.3 	32.1 	31.8 	31.6 	31.4 	31.3 	31.2 	31.2 	31.3 	31.4 	31.6 	31.8 	32.1 	32.4 	32.6 	32.9 ".split()
btwl = [(float(i1)+float(i2))*float(i3)*float(i4) for i1,i2,i3,i4 in zip(bqtw1, td, qka, qkb)]
bqarea = [30.94 for _ in range(len(time_0_23))] #il
bcl = [float(i3)*float(i4)*(float(i1)-float(i2)) for i1,i2,i3,i4 in zip(btwl, tmp_in, crk, bqarea)]
btwl = [round(i,3) for i in btwl]
bcl = [round(i,3) for i in bcl]
all_cl.append(bcl)
# 东内墙
nqcrk = [1.97 for _ in range(len(time_0_23))] #ig
dnqarea = [30.94 for _ in range(len(time_0_23))] #im
twp = [28.3 for _ in range(len(time_0_23))] # ic
c3 = [3 for _ in range(len(time_0_23))]
tls = [i1+i2 for i1,i2 in zip(twp,c3)]
tmp_in = tmp_in
dnqcl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(nqcrk, dnqarea, tls, tmp_in)]
tls = [round(i,3) for i in tls]
dnqcl = [round(i,3) for i in dnqcl]
all_cl.append(dnqcl)

# 南内墙
nnqarea = [30.94 for _ in range(len(time_0_23))] #in
nnqcl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(nqcrk, nnqarea, tls, tmp_in)]
nnqcl = [round(i,3) for i in nnqcl]
all_cl.append(nnqcl)

# 西内墙
xnqarea = [30.94 for _ in range(len(time_0_23))] #io
xnqcl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(nqcrk, xnqarea, tls, tmp_in)]
xnqcl = [round(i,3) for i in xnqcl]
all_cl.append(xnqcl)
# 北内墙
bnqarea = [30.94 for _ in range(len(time_0_23))] #ip
bnqcl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(nqcrk, bnqarea, tls, tmp_in)]
bnqcl = [round(i,3) for i in bnqcl]
all_cl.append(bnqcl)
# 东外窗瞬时
tw1 = "27.20 	26.70 	26.2	25.80 	25.50 	25.3	25.4	26	26.9	27.9	29	29.9	30.80 	31.50 	31.90 	32.20 	32.20 	32.00 	31.60 	30.80 	29.90 	29.10 	28.40 	27.80 ".split()
td = [1 for _ in range(len(time_0_23))] #ib
tw1td = [float(i1)+i2 for i1,i2 in zip(tw1, td)]
tmp_in = tmp_in
cw = [1 for _ in range(len(time_0_23))] #iu
kcw = [3.6825 for _ in range(len(time_0_23))] #ih
dcarea = [6.48 for _ in range(len(time_0_23))] #iq
dccl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(dcarea, kcw, tw1td, tmp_in)]
dccl = [round(i,3) for i in dccl]
all_cl.append(dccl)
# 南外窗瞬时
ncarea = [6.48 for _ in range(len(time_0_23))] #ir
nccl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(ncarea, kcw, tw1td, tmp_in)]
nccl = [round(i,3) for i in nccl]
all_cl.append(nccl)
# 西外窗瞬时
xcarea = [6.48 for _ in range(len(time_0_23))] #if
xccl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(xcarea, kcw, tw1td, tmp_in)]
xccl = [round(i,3) for i in xccl]
all_cl.append(xccl)
# 北外窗瞬时
bcarea = [6.48 for _ in range(len(time_0_23))] #it
bccl = [float(i1)*float(i2)*(float(i3)-float(i4)) for i1,i2,i3,i4 in zip(bcarea, kcw, tw1td, tmp_in)]
bccl = [round(i,3) for i in bccl]
all_cl.append(bccl)
# 东窗日射
cql = [0.26 for _ in range(len(time_0_23))] #imore
ca = [0.85 for _ in range(len(time_0_23))] #iv
djamx = [368 for _ in range(len(time_0_23))] #ib
cs = [1 for _ in range(len(time_0_23))] #iw
ci = [0.6 for _ in range(len(time_0_23))] #ix
dcarea = dcarea
dcrcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)*float(i6) for i1,i2,i3,i4,i5,i6 in zip(cql,ca,djamx,cs,ci,dcarea)]
all_cl.append(dcrcl)
# 南窗日射
cql = [0.26 for _ in range(len(time_0_23))] #imore
ca = [0.85 for _ in range(len(time_0_23))] #iv
djamx = [368 for _ in range(len(time_0_23))] #ib
cs = [1 for _ in range(len(time_0_23))] #iw
ci = [0.6 for _ in range(len(time_0_23))] #ix
ncarea = ncarea
ncrcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)*float(i6) for i1,i2,i3,i4,i5,i6 in zip(cql,ca,djamx,cs,ci,ncarea)]
all_cl.append(ncrcl)
# 西窗日射
cql = [0.26 for _ in range(len(time_0_23))] #imore
ca = [0.85 for _ in range(len(time_0_23))] #iv
djamx = [368 for _ in range(len(time_0_23))] #ib
cs = [1 for _ in range(len(time_0_23))] #iw
ci = [0.6 for _ in range(len(time_0_23))] #ix
xcarea = xcarea
xcrcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)*float(i6) for i1,i2,i3,i4,i5,i6 in zip(cql,ca,djamx,cs,ci,xcarea)]
all_cl.append(xcrcl)
# 北窗日射
cql = [0.26 for _ in range(len(time_0_23))] #imore
ca = [0.85 for _ in range(len(time_0_23))] #iv
djamx = [368 for _ in range(len(time_0_23))] #ib
cs = [1 for _ in range(len(time_0_23))] #iw
ci = [0.6 for _ in range(len(time_0_23))] #ix
bcarea = xcarea
bcrcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)*float(i6) for i1,i2,i3,i4,i5,i6 in zip(cql,ca,djamx,cs,ci,bcarea)]
bcrcl = [round(i,3) for i in bcrcl]
all_cl.append(bcrcl)
# 照明散热
clq = "0.34	0.55	0.61	0.65	0.68	0.71	0.74	0.74	0.79	0.81	0.83	0.39	0.35	0.31	0.28	0.25	0.23	0.2	0.18	0.16	0.15	0.14	0.12	0.11".split()
n1 = [1 for _ in range(len(time_0_23))]
n2 = [0.6 for _ in range(len(time_0_23))]
n = [30 for _ in range(len(time_0_23))] #iy
m = [30 for _ in range(len(time_0_23))] #id
zmcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)for i1,i2,i3,i4,i5 in zip(clq,n1,n2,n,m)]
zmcl = [round(i,3) for i in zmcl]
all_cl.append(zmcl)

# 设备散热
clq = "0.62 	0.69 	0.75 	0.79 	0.82 	0.84 	0.86 	0.88 	0.89 	0.91 	0.92 	0.93 	0.38 	0.31 	0.25 	0.21 	0.18 	0.16 	0.14 	0.12 	0.11 	0.09 	0.08 	0.07 ".split()
n1 = [1 for _ in range(len(time_0_23))]
n2 = [0.8 for _ in range(len(time_0_23))]
n3 = [0.5 for _ in range(len(time_0_23))]
sbcl = [float(i1)*float(i2)*float(i3)*float(i4)*float(i5)*float(i6) for i1,i2,i3,i4,i5,i6 in zip(clq,n1,n2,n3,n,m)]
sbcl = [round(i,3) for i in sbcl]
all_cl.append(sbcl)
# 人体散热
clq = [0.55, 0.64, 0.7, 0.75, 0.79, 0.81, 0.84, 0.86, 0.88, 0.89, 0.91, 0.92, 0.45, 0.36, 0.3, 0.25, 0.21, 0.19, 0.16, 0.14, 0.12, 0.11, 0.09, 0.08]
q_s = [65 for _ in range(len(time_0_23))] #ib1
n = [12 for _ in range(len(time_0_23))] #ic1
o = [0.93 for _ in range(len(time_0_23))] #id1
cls = [float(i1)*float(i2)*float(i3)*float(i4) for i1,i2,i3,i4 in zip(clq, q_s, n, o)]
q_2 = [69 for _ in range(len(time_0_23))] #ie
q_t = [float(i1)*float(i2)*float(i3) for i1,i2,i3 in zip(n, o, q_2)]
rtcl = [float(i1)+float(i2) for i1,i2 in zip(q_t, cls)]
all_cl.append(rtcl)
# 新风冷负荷计算
hn = 50.5 #ig1
hw = 92.7 #if1
m0 = 207 #ie1
q = m0*1.2/3600*(hw-hn)*1000
all_cl.append([q for _ in range(len(time_0_23))])

