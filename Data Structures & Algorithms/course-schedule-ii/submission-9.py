class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()  # Tracks the active path (catches cycles)
        visited = set()   # Tracks fully completed courses (catches redundant work)
        path = []

        def dfs(crs):
            # 1. Have we seen this in our active path?
            if crs in visiting:
                return False
            
            # 2. Have we ALREADY fully completed this course previously?
            if crs in visited:
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            
            # 3. Mark this course as fully completed!
            visited.add(crs)
            path.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return path