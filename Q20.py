#valid parenthesis Q20
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:   # if not odd number, then return false
            return False
        cur = None
        a = "({["
        b = ")}]"
        for i in range(len(s)):
            if s[i] in a:
                temp = ListNode(s[i])
                temp.next = cur
                cur = temp
            elif cur and a.index(cur.val) == b.index(s[i]):
                cur = cur.next
            else:
                return False
        return False if cur else True
        
class ListNode(object):
    def __init__(self,val=''):
        self.val = val
        self.next = None
