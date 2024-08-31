
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        res = n*(n+1)//2
        return res
        # s=0
        # for i in range(1, n+1):
        #     s+=i
        # return s




#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)

# } Driver Code Ends