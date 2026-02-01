import array as arr

A = arr.array('i',[1,2,3,4,5,5,5,5,5,5,5,5])
print('Original array:  ',A)

print('\nNumber of times 5 occurs '+str(A.count(5)))

A.reverse()
print('\nReversed array:  '+str(A))
