#EPI Chapter 4 practice

# 4.7 Compute pow(x,y)
# O(n) # of multiplication = at most twice the idnex of y's MSB
# def power(x: float, y: int) -> float:
#   result, power = 1.0, y
#   # check negative power
#   if (y < 0):
#     power *= -1
#     x = 1.0/x
#
#   while power:
#     #check the LSB of power
#     if power & 1: #if LSB is 1
#       result *= x
#     x= x * x
#     power =  power >> 1
#   return result
#
# print(pow(2, -2))
################################
