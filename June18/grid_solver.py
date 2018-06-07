h_opts = []
counter = 1
for i in range(0,7):
    for j in range(0,7):
        for k in range(0,7):
            for l in range(0,7):
                for m in range(0,7):
                    for n in range(0,7):
                        for o in range(0,7):
                            res = [i,j,k,l,m,n,o]
                            zero_count = len([z for z in res if not z])
                            if i + j + k + l + m + n + o == 20 and zero_count == 3:
                                counter = counter + 1
#                                 print(str(counter)+": "+str(i)+" + "+str(j)+" + "+str(k)+" + "+str(l)+" + "+str(m)+" + "+str(n)+" + "+str(o)+" = "+str(i+j+k+l+m+n+o))
                                h_opts.append(res)
# print((h_opts))
print("finished "+str(len(h_opts))+" finding rows...")
df = pd.DataFrame(h_opts)
# print(df)
valid = []

for r in df.iterrows():
    for s in df.iterrows():
        for t in df.iterrows():
            for u in df.iterrows():
                for v in df.iterrows():
                    for w in df.iterrows():
                        for x in df.iterrows():
                            if (r[1][0]+s[1][0]+t[1][0]+u[1][0]+v[1][0]+w[1][0]+x[1][0] == 20 and 
                                r[1][1]+s[1][1]+t[1][1]+u[1][1]+v[1][1]+w[1][1]+x[1][1] == 20 and
                                r[1][2]+s[1][2]+t[1][2]+u[1][2]+v[1][2]+w[1][2]+x[1][2] == 20 and
                                r[1][3]+s[1][3]+t[1][3]+u[1][3]+v[1][3]+w[1][3]+x[1][3] == 20 and
                                r[1][4]+s[1][4]+t[1][4]+u[1][4]+v[1][4]+w[1][4]+x[1][4] == 20 and
                                r[1][5]+s[1][5]+t[1][5]+u[1][5]+v[1][5]+w[1][5]+x[1][5] == 20 and
                                r[1][6]+s[1][6]+t[1][6]+u[1][6]+v[1][6]+w[1][6]+x[1][6] == 20):
                                valid.append([[r[1][0],s[1][0],t[1][0],u[1][0],v[1][0],w[1][0],x[1][0]],
                                    [r[1][1],s[1][1],t[1][1],u[1][1],v[1][1],w[1][1],x[1][1]],
                                    [r[1][2],s[1][2],t[1][2],u[1][2],v[1][2],w[1][2],x[1][2]],
                                    [r[1][3],s[1][3],t[1][3],u[1][3],v[1][3],w[1][3],x[1][3]],
                                    [r[1][4],s[1][4],t[1][4],u[1][4],v[1][4],w[1][4],x[1][4]],
                                    [r[1][5],s[1][5],t[1][5],u[1][5],v[1][5],w[1][5],x[1][5]],
                                    [r[1][6],s[1][6],t[1][6],u[1][6],v[1][6],w[1][6],x[1][6]]])

print(valid)