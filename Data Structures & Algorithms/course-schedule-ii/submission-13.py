class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()
        path = []

        # Add 'depth' to track indentation
        def dfs(crs, depth=0):
            indent = "  " * depth  # Creates visual indentation
            
            if crs in visiting:
                return False

            if crs in visited:
                # # if crs not in path:
                # #     path.append(crs)
                # if crs not in visited:
                #     path.append(crs)
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre, depth + 1): # Pass depth + 1 to children
                    return False

            visiting.remove(crs)
            
            visited.add(crs)
            path.append(crs)
                
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return path