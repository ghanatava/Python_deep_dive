#tuples as records

lax_coordinates=(33.94251,-118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66,
8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

#ways to unpack tuples


for passport in sorted(traveler_ids):
    print('%s%s' %passport)


for country,_ in traveler_ids:  #like go lang comma ok syntax
    print(country)

#tupples as immutable list
#tuples are immutable but if they contain a mutable item there values can be changed

a=('a','b',[1,2])
a[-1].append(3)
print(a)