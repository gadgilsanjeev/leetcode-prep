# Problem Title: Add Two Numbers
# LeetCode Link: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium
# Topics: Arrays

"""
Explanation:
    [Briefly explain your logic here in 1-2 sentences]

Complexity:
    Time: O(n) - Explain why
    Space: O(n) - Explain why
"""

from typing import List  # Import common types as needed

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        carry = 0
        choice = 0
        end = 0
        l3 = None
        temp = None
        tail = None
        while 1:
            l3_temp = l1.val + l2.val + carry
            if l3_temp > 9:
                temp = l3_temp % 10
                carry = l3_temp / 10
            else:
                temp = l3_temp
                carry = 0
            if l3 == None:
                l3 = ListNode(temp)
                # print "a"
                # print temp
                tail = l3
            else:
                t = ListNode(temp)
                # print "b"
                tail.next = t
                tail = tail.next

            if l1.next == None:
                choice = 1
            if l2.next == None:
                choice = 2
            if choice == 2 and l1.next == None:
                end = 1
                break
            if choice == 1 or choice == 2:
                break
            l1 = l1.next
            l2 = l2.next
        if choice == 1 and end != 1:
            l2 = l2.next
            while l2.next != None:
                l3_temp = l2.val + carry
                if l3_temp > 9:
                    temp = l3_temp % 10
                    carry = l3_temp / 10
                else:
                    temp = l3_temp
                    carry = 0
                if l3 == None:
                    l3 = ListNode(temp)
                    # print "c"
                    tail = l3
                else:
                    t = ListNode(temp)
                    # print "d"
                    tail.next = t
                    tail = tail.next
                l2 = l2.next
            else:
                l3_temp = l2.val + carry
                if l3_temp > 9:
                    temp = l3_temp % 10
                    carry = l3_temp / 10
                else:
                    temp = l3_temp
                    carry = 0
                if l3 == None:
                    l3 = ListNode(temp)
                    # print "e"
                    tail = l3
                else:
                    t = ListNode(temp)
                    # print "f"
                    tail.next = t
                    tail = tail.next
        if choice == 2 and end != 1:
            l1 = l1.next
            while l1.next != None:
                l3_temp = l1.val + carry
                if l3_temp > 9:
                    temp = l3_temp % 10
                    carry = l3_temp / 10
                else:
                    temp = l3_temp
                    carry = 0
                if l3 == None:
                    l3 = ListNode(temp)
                    # print "g"
                    tail = l3
                else:
                    t = ListNode(temp)
                    # print "h"
                    tail.next = t
                    tail = tail.next
                l1 = l1.next
            else:
                l3_temp = l1.val + carry
                if l3_temp > 9:
                    temp = l3_temp % 10
                    carry = l3_temp / 10
                else:
                    temp = l3_temp
                    carry = 0
                if l3 == None:
                    l3 = ListNode(temp)
                    # print "i"
                    tail = l3
                else:
                    t = ListNode(temp)
                    # print "j"
                    # print temp
                    tail.next = t
                    tail = tail.next
        if carry != 0:
            t = ListNode(carry)
            # print "k"
            # print carry
            tail.next = t
        return l3