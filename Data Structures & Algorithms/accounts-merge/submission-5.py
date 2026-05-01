class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    
        email_to_name = {}
        graph = {}

        for account in accounts:
            name = account[0]
            first = account[1]
            if first not in graph:
                graph[first] = []
    
            email_to_name[first] = name
            for email in  account[2:]:
                if email not in graph:
                    graph[email] = []
                
                graph[email].append(first)
                graph[first].append(email)
                email_to_name[email] = name


        visited = set()
        result = []

        # add to curr component if needed
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    # add neighbour to the same compoenent
                    dfs(neighbour, component)

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))

        return result



