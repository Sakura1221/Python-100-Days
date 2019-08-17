"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

# for i in range(1,6):
#     print('*'*i)
#
# for i in range(1,6):
#     print(' '*(5-i) + '*'*i)
#
# for i in range(1,10,2):
#     print(' '*int(5-(i+1)/2) + '*'*i)

for i in range(1,6):
    for _ in range(5 - i):
        print(' ', end='')
    for _ in range(2 * i - 1):
        print('*',end='')
    print()