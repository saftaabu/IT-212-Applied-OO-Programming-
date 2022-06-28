a = 57     
b = 123    

print("{0:02x} {1} {2:08b}".format(a, a, a))
print("{0:02x} {1} {2:08b}".format(b, b, b))

c = a & b
print("{0:02x} {1} {2:08b}".format(c, c, c))

c = a ^ b
print("{0:02x} {1} {2:08b}".format(c, c, c))

c = a | b
print("{0:02x} {1} {2:08b}".format(c, c, c))
