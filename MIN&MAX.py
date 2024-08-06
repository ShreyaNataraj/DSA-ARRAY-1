#MAXIMUM AND MINIMUM ELEMENT IN THE ARRAY USING COMPARISIONS
def min_num(A):
  mini = float('inf')
  for num in A:
    if num<mini:
      mini = num
  return mini

def max_num(A):
  maxi = float('-inf')
  for num in A:
    if num>maxi:
      maxi =num
  return maxi

A = [1,2,3,4,5,6]
print("maximum element in the list is:" + str(max_num(A)))
print("manimum element in the list is:" + str(min_num(A)))
    