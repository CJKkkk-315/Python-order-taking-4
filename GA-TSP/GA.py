import numpy as np
import random
import math
best_s = '''1
15
16
2
3
4
17
18
5
19
20
6
7
8
21
9
11
24
36
34
31
26
28
22
25
29
30
33
41
42
43
44
48
50
54
56
60
61
72
71
70
69
68
67
73
76
79
82
84
85
95
94
97
105
104
103
101
100
102
109
118
119
120
121
122
123
124
126
129
131
133
134
135
143
142
146
145
144
149
152
150
153
151
155
161
160
159
157
148
154
158
171
172
163
164
165
166
167
173
174
175
183
190
189
188
187
185
181
182
176
177
178
180
186
196
197
198
199
200
201
202
209
205
208
211
214
221
226
229
239
240
241
242
243
244
250
249
255
257
253
248
247
238
237
246
236
235
234
245
252
254
256
261
260
262
270
278
279
277
276
271
263
264
265
272
266
267
268
273
274
275
280
281
282
292
291
290
289
298
297
296
301
307
302
308
303
312
319
325
341
336
340
343
342
339
338
335
334
332
330
331
333
337
329
321
322
323
326
327
328
324
318
317
316
315
314
311
306
310
305
300
304
309
320
313
299
285
286
287
293
294
295
288
284
283
269
259
258
251
231
232
233
230
223
227
228
225
224
222
220
219
218
217
216
215
212
206
213
210
207
204
195
194
193
192
203
191
184
179
170
169
168
162
156
147
138
139
140
141
137
127
132
136
130
128
125
117
116
115
114
113
112
110
111
108
107
106
98
99
96
86
87
88
89
90
91
92
93
81
78
75
77
83
80
74
63
64
65
66
62
51
49
53
55
57
58
59
52
47
46
40
39
38
37
45
35
32
27
23
10
12
13
14'''
best_s = [int(i)-1 for i in best_s.split('\n')]

def parse_tsp_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()[:-1]


    dimension = None
    for line in lines:
        if line.startswith('DIMENSION'):
            dimension = int(line.split(':')[1])

    coords = []
    for line in lines[-dimension:]:
        parts = line.split(' ')
        coords.append((float(parts[1]), float(parts[2])))

    return coords

class Ga:
    def __init__(self,file,pop_size=200,iteration=1000,pc=0.1,pm=0.08):
        self.pop_size = pop_size
        self.iteration = iteration
        self.pc = pc
        self.pm = pm
        self.coords = parse_tsp_file(file)
        self.chrom_length = len(self.coords)
        self.pop = []
        self.all_best = []
        for i in range(pop_size):
            cities = list(range(len(self.coords)))
            random.shuffle(cities)
            self.pop.append(cities)

    def distance_between(self, city1, city2):
        x_diff = self.coords[city1][0] - self.coords[city2][0]
        y_diff = self.coords[city1][1] - self.coords[city2][1]
        return math.sqrt(x_diff**2 + y_diff**2)

    def get_fitness(self,gene):
        total = 0
        for i in range(len(gene)):
            total += self.distance_between(gene[i - 1], gene[i])
        return 1 / total

    def selection(self,fit_values):
        new_pop = list(random.choices(self.pop, weights=fit_values, k=self.pop_size))
        self.pop = new_pop

    def crossover(self):
        for i in range(len(self.pop)):
            if random.random() < self.pc:
                a = i
                b = random.randint(0, len(self.pop) - 1)
                cpoint = random.randint(0, self.chrom_length-1)
                temp1 = []
                temp2 = []
                temp1.extend(self.pop[a][0:cpoint])
                temp1.extend(self.pop[b][cpoint:len(self.pop[a])])
                temp2.extend(self.pop[b][0:cpoint])
                temp2.extend(self.pop[a][cpoint:len(self.pop[a])])
                self.pop[a] = temp1
                self.pop[b] = temp2

    def mutation(self):
        for i in range(len(self.pop)):
            if random.random() < self.pm:
                mpoint = random.randint(0, self.chrom_length-1)
                if self.pop[i][mpoint] == 1:
                    self.pop[i][mpoint] = 0
                else:
                    self.pop[i][mpoint] = 1

    def get_result(self):
        for iter in range(self.iteration):
            fit_values = np.array([self.get_fitness(x) for x in self.pop])
            iter_best = max(fit_values)
            index = np.argwhere(fit_values == iter_best)[0][0]
            self.all_best.append([iter_best, self.pop[index]])
            self.selection(fit_values)
            self.crossover()
            self.mutation()
            self.pop[0] = self.pop[index]
        self.all_best.sort(key=lambda x:x[0],reverse=True)
        return self.all_best[0]

ga = Ga(file='pma343.tsp')
print(1/ga.get_fitness(best_s))
print(1/ga.get_result()[0])
