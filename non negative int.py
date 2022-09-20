def maxArea( A):
 l = 0
 r = len(A) -1
 area = 0
 while l < r:
  area = max(area, min(A[l],
      A[r]) * (r - l))
 
  if A[l] < A[r]:
   l += 1
  else:
   r -= 1
 return area
a = [1,5,4,3]
print(maxArea(a))
