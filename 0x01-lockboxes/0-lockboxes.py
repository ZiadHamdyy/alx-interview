#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    visited = [False] * len(boxes)
    visited[0] = True
    stack = boxes[0]
    while stack:
        key = stack.pop()
        if not visited[key]:
            visited[key] = True
            stack.extend(boxes[key])
    return all(visited)
