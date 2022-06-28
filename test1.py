# Syed Aftaabuddin
# Lab 2
# April 27, 2020


from clock import Clock

# Test clock for initial time 04:07:03
c1 = Clock (4, 7, 3)
print(c1)
print(c1.hr, c1.min, c1.sec)
c1.tick( )
print(c1)
# Output
# 04:07:04
print(  )

# Test clock for initial time 04:07:59
c2 = Clock(4, 7, 59)
print(c2)
c2.tick( )
print(c2)
# Output
# 04:08:00
print(  )


#Third case test for initial time 04:59:59 
c3 = Clock(4, 59, 59)
print(c3)
c3.tick( )
print(c3)
# Output
# 05:00:00
print(  )

#Fourth case test for initial time 23:59:59
c4 = Clock (23, 59, 59)
print(c4)
c4.tick( )
print(c4)
# Ouput
# 00:00:00
