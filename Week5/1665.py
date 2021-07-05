class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        temp=sum([task[0] for task in tasks])
        tasks.sort(key=lambda x:-(x[1]-x[0]))
        init=temp
        for actual,minimum in tasks:
            if init<minimum:
                add=minimum-init
                init+=add
                temp+=add
            init-=actual
        return temp