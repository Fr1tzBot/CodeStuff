c={"2":10000,"4":15000,"c":20000,"s":1000,"p":3000,"l":5000}
x=c[input("(2)door, (4)door, or(c)onvertible?")]
x+=c[input("Total:"+str(x)+"\n(s)tandard, (p)remium, or (l)luxury?")]
x+=1000*int(input("Total:"+str(x)+"\n0-5 years warranty:"))
print(str(x)+"$Total")