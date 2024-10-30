d1 = {"adao smith":"a","judie silva": "b+"}
d2 = {"maria santos":"a","Paulo jose":"c"}
d3 = {}

for item in (d1,d2):
    d3.update(item)

print(d3)