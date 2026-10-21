class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [0] * numCourses
        numNeeded = [0] * numCourses
        for i in range(len(dependencies)):
            dependencies[i] = set()
        
        valid = set(range(0, numCourses, 1))


        for i in range(len(prerequisites)):
            locked, necessary = prerequisites[i]
            dependencies[necessary].add(locked)
            numNeeded[locked] += 1
            if(locked in valid):
                valid.remove(locked)
        
        stack = []
        for num in valid:
            stack.append(num)

        while(len(stack) > 0):
            curr = stack.pop()
            canUnlock = dependencies[curr]
            for req in canUnlock:
                numNeeded[req] -= 1
                if(numNeeded[req] == 0):
                    stack.append(req)
            dependencies[curr] = set()
        
        if(sum(numNeeded) > 0):
            return False
        return True

        