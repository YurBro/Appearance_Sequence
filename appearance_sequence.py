# 定义好出口
class appearance_sequence:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        # 假设我们上一层的结果为“112213”
        s1 = self.countAndSay(n-1)  # 递归
        res = ''    # 设置新串
        slow = 0       #
        fast = 1
        s1 += '0'      # 末尾标志，因为不会出现0
        while fast < len(s1):
            if s1[slow] != s1[fast]:                    # 判断是否数字相同
                res += str(fast-slow) + str(s1[slow])   # 前半部分表示后半部分的个数
                slow = fast
            fast += 1

        return res


