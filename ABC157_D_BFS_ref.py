"""
D-Friend Suggestions
BFS
"""

import sys
input = sys.stdin.readline
from collections import deque, Counter


def main():
    N, M, K = map(int, input().split())
    friend = [[] for _ in range(N)]
    block = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        friend[a - 1].append(b - 1)
        friend[b - 1].append(a - 1)

    for _ in range(K):
        c, d = map(int, input().split())
        block[c - 1].append(d - 1)
        block[d - 1].append(c - 1)

    label_list = [-1] * N
    label = 0
    for start_vertex in range(N):
        q = deque()

        def push(vertex, label):
            if label_list[vertex] != -1:
                return
            q.append(vertex)
            label_list[vertex] = label

        push(start_vertex, label)

        while len(q) != 0:
            vertex = q.popleft()
            friend_vertexes = friend[vertex]
            for f_vertex in friend_vertexes:
                push(f_vertex, label)
        label += 1

    connected_component_id = Counter(label_list)

    ans = []
    for i in range(N):
        vertex_label = label_list[i]
        connected_qty = connected_component_id[vertex_label]

        for j in block[i]:
            if label_list[i] == label_list[j]:
                connected_qty -= 1

        ans.append(connected_qty - len(friend[i]) - 1)

    print(*ans)


if __name__ == '__main__':
    main()