"""# Find leader in the given array ( where leader means the element whose value is grester than or equal to the elements in the right hand side of the array)


def findLeader(arr):
	arr.reverse()
	ans=[arr[0]]
	cur_leader=ans[-1]
	for i in range(1,len(arr)):
		if arr[i]>=cur_leader:
			ans.append(arr[i])
			cur_leader=ans[-1]
	return ans
	

arr=list(map(int,input().split(" ")))

resultArr=findLeader(arr)


def printArr(arr):
	arr.reverse()
	for i in arr:
		yield i
		
		
result=printArr(resultArr)

for i in result:
	print(i)


# Sort the gibven array without using a built in function which contains values 0,1 and 2  (SORT COLORS PROBLEM)

def sortColors(arr):
	n=len(arr)
	left=0
	right=n-1
	
	i=0
	while i<=right:
		if arr[i]==0:
			arr[left],arr[i]=arr[i],arr[left]
			left+=1
			i+=1
		elif arr[i]==2:
			arr[right],arr[i]=arr[i],arr[right]
			right-=1

		else:
			i+=1
		
			
arr=list(map(int,input().split()))

sortColors(arr)

print(arr)



#Subarray sum equals K 

def subArraySumK(arr,k):
	
	cur_sum=0
	count=0
	left=0
	i=0
	while i<len(arr):
		cur_sum+=arr[i]
		
		if cur_sum>k:
			while cur_sum>k:
				cur_sum-=arr[left]
				left+=1
			
		if cur_sum==k:
			count+=1	
			
				
		i+=1
				
	return count
				




arr=list(map(int,input().split()))
k=int(input())
count=subArraySumK(arr,k)
print(count)





# 3Sum Closest Problem(Given an integer array and we need to find the closest sum that formed by the sum of any three values where the index of the the three values is not same)


def threeSumClosest(arr,target):
	arr.sort()
	i=0
	dif=float('inf')
	closest=float('inf')
	while i<len(arr)-2:

		left=i+1
		right=len(arr)-1
		while left<right:		
			cur_sum=arr[i]+arr[left]+arr[right]
			#print('i=',arr[i],'left=',arr[left],'right=',right,'cur_sum=',cur_sum)
			cur_dif=abs(target-cur_sum)
			if cur_dif<dif:
				dif=cur_dif
				closest=cur_sum
				
			if cur_sum<=target:
				left+=1
				
			else:
				right-=1
				
		i+=1
	
	
	return closest
	
	
	
arr=list(map(int,input().split()))
target=int(input())

closest=threeSumClosest(arr,target)

print("3SumClosest Values =",closest)


# Product Except self in an array(Return an array that contains all the products except self of an index)

def productExceptSelf(arr):
	prod=1
	for i in arr:
		prod=prod*i
	
	ans=[]
	for i in range(0,len(arr)):
		ans.append(prod//arr[i])
		
	return ans
	
arr=list(map(int,input().split(" ")))

ans=productExceptSelf(arr)

print(ans)
		

	



# Longest Polindromic Substring


def longestPolindromicCenter(s):
	def expandCenter(left,right):
		while left>=0 and right<len(s) and s[left]==s[right]:
			left-=1
			right+=1
			
		return s[left+1:right]
		
		
	length=''
	for i in range(len(s)):
		oddLengthPoly=expandCenter(i,i)
		evenLengthPoly=expandCenter(i,i+1)
	
		if len(oddLengthPoly)>len(length):
			length=oddLengthPoly
		if len(evenLengthPoly)>len(length):
			length=evenLengthPoly
		
		

	return length
			

string=input()
ans=longestPolindromicCenter(string)
print(ans)




# Group Anagrams

from collections import defaultdict

n=int(input())

arr=list(input().split(' '))
print(arr)
d=defaultdict(list)
for i in arr:
	sor=''.join(sorted(i))
	d[sor].append(i)
	
	
print(d.values())

"""
