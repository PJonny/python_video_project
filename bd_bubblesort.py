# this is Bi-Directional Bubble Sort
def bdBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    # the high and low bound of the list that will be bubbled
    low = 0
    high = len(alist)-1
    direction = 'r'
    while passnum > 0 and exchanges:
      exchanges = False
      # bubble from left to right
      if direction == 'r':
        for i in range(low, high):
          if alist[i] > alist[i+1]:
            exchanges = True
            temp = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = temp
        # the high bound of the list must decrease by one
        high -= 1
        # change the direction
        direction = 'l'
      # bubble from right to left
      elif direction == 'l':
        for i in range(high, low, -1):
          if alist[i] < alist[i-1]:
            exchanges = True
            temp = alist[i]
            alist[i] = alist[i-1]
            alist[i-1] = temp
        # the low bound of the list increase by one
        low += 1
        # change the direction
        direction = 'r'
      passnum = passnum-1
      #print list after one pass
      print(alist)


# test the method
if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    # alist = [7,6,5,4,3,2,1]
    bdBubbleSort(alist)
    print(alist) 