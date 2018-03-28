f=open('websites.csv','r')
temp=f.readlines()[1002:]

dataset=[]

for x in temp:
    if len(dataset) > 1000:
        break
    t=x.split(',')[1]
    dataset.append( str(t.split("://")[1] + '\n'))
limit=len(dataset)
print (limit)

f=open('top-1m.csv','r')
temp=f.readlines()[1002:]
for x in temp:
    if len(dataset)/2 >= limit:
        break
    t=x.split(',')[1]
    dataset.append( str(t))

f=open('data_set.txt','w')
for x in dataset:
    f.write(x)