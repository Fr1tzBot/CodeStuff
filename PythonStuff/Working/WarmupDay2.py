a = (10, 5, 7)
out2 = 999999999999999999999999999999
out = 0
for i in range(len(a)):
	if a[i] > out:
		out = a[i]
	if a[i] < out2:
		out2 = a[i]
print(out)
print(out2)
