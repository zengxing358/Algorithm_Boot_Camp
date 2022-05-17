class Solution:
    def plusOne(self, digits):
        if digits:
            if digits[-1]==9:
                return self.plusOne(digits[:-1])+[0]
            else:
                digits[-1]+=1
                return digits
        return [1]