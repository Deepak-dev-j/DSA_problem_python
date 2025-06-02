# a=("i","j",[1,2,3,4,])
# print(a) # type: ignore

# arr=["list","like",1,2,23]
# arr.insert(0,20)
# arr.insert(1,30)
# arr.pop(1)
# print(arr)

from array import *

arr=array('i',[4,5,7,8])
a=2
for i in range(0,len(arr)):
    if arr[i]==5:
         print(i)
         break