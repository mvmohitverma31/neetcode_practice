class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        temp=[]
        r=len(numbers)-1
        for _ in range(len(numbers)):
            rem=target-numbers[l]
            if rem==numbers[r]:
                temp.append(numbers[l])
                temp.append(numbers[r])
            if rem<target:
                r-=1
        return temp