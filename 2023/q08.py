import re
import os
from itertools import cycle
import math


def part_1(data: str):
    lr_instruction, node_network = data.split("\n\n")
    curr_node = "AAA"
    lr_map = {"L": 0, "R": 1}
    nodes = {}
    for node in re.findall(r"(\w+) = \((\w+), (\w+)", node_network):
        nodes[node[0]] = (node[1], node[2])
    count = 0
    for direction in cycle(lr_instruction):
        curr_node = nodes[curr_node][lr_map[direction]]
        count += 1
        if curr_node == "ZZZ":
            break
    return count


def part_2(data: str):
    lr_instruction, node_network = data.split("\n\n")
    lr_map = {"L": 0, "R": 1}
    graph = {}
    start_nodes = []
    for curr_node, left_node, rnode in re.findall(
        r"(\w+) = \((\w+), (\w+)", node_network
    ):
        if curr_node.endswith("A"):
            start_nodes.append(curr_node)
        graph[curr_node] = (left_node, rnode)
    count = []
    for node in start_nodes:
        for idx, direction in enumerate(cycle(lr_instruction), start=1):
            node = graph[node][lr_map[direction]]
            # Here we are finding the first time **Z appears in the graph for each node.
            if node.endswith("Z"):
                count.append(idx)
                break

    # Why LCM? Looking at sample data it can be deduced that **Z will occur after every nth time for first node,
    # xth time for second node, and so on. So we take LCM(n,x) to find where they will finally meet
    return math.lcm(*count)


data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


with open(os.path.join(os.getcwd(), "2023/inputs/8.txt"), "r") as f:
    data = f.read().strip()
    print(f"Part one output: {part_1(data)}")
    print(f"Part two output: {part_2(data)}")
