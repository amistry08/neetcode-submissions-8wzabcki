class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        route = []

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                if(crs not in route):
                    route.append(crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            if(crs not in route):
                route.append(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        print(route)
        return list(route)
