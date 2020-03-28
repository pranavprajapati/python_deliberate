# Write your code here
st = input("Enter here: ")
n =  int(input("Enter nos: "))
cap_n = st[-n:].capitalize()
#print(st[:-n] + cap_n)
print(f" {st[:-n]}{cap_n}")
