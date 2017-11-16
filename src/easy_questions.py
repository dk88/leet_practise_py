# encoding:utf-8
import sys

__author__ = 'zhaoxiaojun'

reload(sys)
sys.setdefaultencoding('utf-8')


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        count = 0
        while num > 0:
            flag = num & 1
            if flag == 0:
                res += pow(2, count)
            count += 1
            num >>= 1
        return res

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        str_list = list(s)
        for ind in range(len(s)):
            if not str(s[ind]).strip() or ind == len(s) - 1:
                end = ind - 1
                if ind == len(s) - 1:
                    end = ind
                while start < end:
                    tmp = s[start]
                    str_list[start] = s[end]
                    str_list[end] = tmp
                    start += 1
                    end -= 1
                start = ind + 1
        return ''.join(str_list)

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        res_list = []
        for word in words:
            ws = set(str(word).lower())
            if ws.issubset(s1) or ws.issubset(s2) or ws.issubset(s3):
                res_list.append(word)
        return res_list

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        total = 0
        for ind in range(len(ops)):
            if str(ops[ind]).upper() == 'D':
                last_valid_score = stack.pop()
                current_score = last_valid_score * 2
                stack.append(last_valid_score)
                stack.append(current_score)
                total += current_score
            elif str(ops[ind]).upper() == 'C':
                invalid_score = stack.pop()
                total -= invalid_score
            elif str(ops[ind]).upper() == '+':
                last_valid_score1 = stack.pop()
                last_valid_score2 = stack.pop()
                current_score = last_valid_score1 + last_valid_score2
                stack.append(last_valid_score2)
                stack.append(last_valid_score1)
                stack.append(current_score)
                total += current_score
            else:
                total += int(ops[ind])
                stack.append(int(ops[ind]))
        return total

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sis_set = set()
        max_len = len(candies) / 2
        for num in candies:
            if num not in sis_set and len(sis_set) < max_len:
                sis_set.update([num])
        return len(sis_set)

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_list = []
        for ind in range(1, n + 1):
            cur_val = ''
            if ind % 3 == 0:
                cur_val = 'Fizz'
            if ind % 5 == 0:
                cur_val = '%s%s' % (cur_val, 'Buzz')
            if cur_val == '':
                cur_val = ind
            res_list.append(cur_val)
        return res_list

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_list = []
        for nu_list in nums:
            flat_list += nu_list
        if r * c > len(flat_list):
            return nums
        else:
            res_list = []
            for count in range(r):
                res_list.append(flat_list[c * count:(count + 1) * c])
            return res_list


if __name__ == '__main__':
    so = Solution()
    print so.findComplement(5)
    print so.reverseWords("Let's take")
    print so.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print so.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print so.distributeCandies([1, 1, 2, 2, 3, 3])
    print so.fizzBuzz(15)
    print so.matrixReshape([[1, 2], [3, 4]], 1, 4)
