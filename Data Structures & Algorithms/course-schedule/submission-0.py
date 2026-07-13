class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        #visitSet = all courses along the current DFS path
        visitSet = set()
        
        def dfs(crs):
            if crs in visitSet: #if we already visited it => loop
                return False
            if preMap[crs]==[]: #if it has no prereqs
                return True
            visitSet.add(crs) #=> we are visiting it for the first time
            for pre in preMap[crs]:
                if not dfs(pre): return False #if a certain prereq returns False, immediately return False
            visitSet.remove(crs) #we are done visiting it
            preMap[crs]=[] #we have verified all its prereqs so it has none anymore
            return True
        
        for crs in range(numCourses): #we need to iterate through every single course because all of them may not be connected
            if not dfs(crs): return False

        return True