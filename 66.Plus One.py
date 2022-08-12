class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        #case:[9]->[1,0]
        elif len(digits)==1 and digits[-1]==9:
            return [1,0]
        
        #special case [9,9]->[1,0,0]重複代入function
        else:
            digits[-1]=0
            digits[0:-1]=self.plusOne(digits[0:-1])
            return digits
    