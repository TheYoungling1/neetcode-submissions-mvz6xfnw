class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first = account[1]
            email_to_name[first] = name
            for email in account[2:]:
                graph[first].add(email)
                graph[email].add(first)
                email_to_name[email] = name

        visited = set()
        result = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))

        return result