
#Dictionary
# Creating dictionaries
a={} #empty dictionary
b={'one':1, 'two':2,'three':3}
c={}
c['one']=1
c['two']=2
c['third']=3
print(c)

#access elements in the dictionary
b={'one':1, 'two':2,'three':3}
print(b['two'])

#Dictionary operations

del (b['two'])#del
print(b)

b['one']=7#update
print(b)

b['four']=9# add
print(b)

print(len(b))


#Dictionary methods

print(b.keys())
print(b.values())
print(b.items())

# Aliasing and copying in dictionary?

c={'one':1, 'two':2,'three':3}
d=c
d['three']=4
print(d)
print(c)
copy1=c.copy()
copy1['three']=7
print(copy1)
print(c)
