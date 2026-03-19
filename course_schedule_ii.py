from collections import defaultdict, deque


def find_order(num_courses: int, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(find_order(num_courses, prerequisites))
