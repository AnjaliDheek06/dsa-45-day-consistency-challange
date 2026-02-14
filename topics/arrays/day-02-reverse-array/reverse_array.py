class Solution:
    def rev_Arr(self,arr):
        p1 = 0 
        p2 = len(arr) -1
        while p1<p2:
            arr[p1],arr[p2] = arr[p2],arr[p1]
            p1  +=  1
            p2  -=  1
if   __name__ ==   "__main__":
    sol = Solution()
    arr = [4,3,2,8,7]
    sol.rev_Arr(arr)
    print(" ".join(map(str,arr)))