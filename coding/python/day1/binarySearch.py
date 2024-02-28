

class BSearch():
	def __init__(self, list):
		self.list = list

	def makeBinarySearch(self, element):
		n=len(self.list)
		leftIndex=0
		rightIndex=n

		while leftIndex<rightIndex:
			mid=(leftIndex+rightIndex)//2
			if self.list[mid] == element:
				return mid

			if self.list[mid] < element:
				leftIndex=mid+1
			else:
				rightIndex= mid-1


list=[10,12,13,14,15,16]
bsearch=BSearch(list)
print(bsearch.makeBinarySearch(19))

