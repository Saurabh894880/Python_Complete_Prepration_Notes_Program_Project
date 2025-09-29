# Wap to print following pattern
'''
    *
   ***
  *****
 *******
*********
'''
for i in range(1, 6): 
    print(' ' * (5 - i) + '*' * (2 * i - 1))
