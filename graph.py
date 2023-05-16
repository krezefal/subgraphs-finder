from typing import List
from random import random
from prettytable import PrettyTable
import time

from consts import ROUNDING

class Graph:
    def __init__(self, vertices_num, adj_mtx=None):
        self.vertices_num = vertices_num

        if adj_mtx is not None:
            self.graph_prob = adj_mtx
        else: # random generation
            self.graph_prob = [[0 for _ in range(self.vertices_num)] for _ in \
                            range(self.vertices_num)]
            for i in range(self.vertices_num):
                for j in range(self.vertices_num):
                    self.graph_prob[j][i] = self.graph_prob[i][j] = \
                    round(random(), ROUNDING)
                self.graph_prob[i][i] = 0

        self.graph = [[0 for _ in range(self.vertices_num)] for _ in \
                      range(self.vertices_num)]
    
    def bfs(self, start, end):
        visited = [False for _ in range(self.vertices_num)]
        queue = [start]
        visited[start] = True
        while queue:
            node = queue.pop(0)
            for neighbor in range(self.vertices_num):
                if self.graph[node][neighbor] != 0 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    if neighbor == end:
                        return True
        return False
    
    def check_connected_graph(self):
        for i in range(self.vertices_num):
            for j in range(self.vertices_num):
                if i != j and not self.bfs(i, j):
                    return False
        return True
    
    def gen_graph(self):
        for i in range(self.vertices_num):
            for j in range(self.vertices_num):
                if random() < self.graph_prob[i][j]:
                    self.graph[j][i] = self.graph[i][j] = 1
                else:
                    self.graph[j][i] = self.graph[i][j] = 0
    
    def calc_complete_graph_prob(self, tests_amount, 
                                verbose=False, timer=False):
        successful_tests = 0
        quarter = 1

        if timer:
            start_time = time.time()

        for test_num in range(1, tests_amount + 1):
            self.gen_graph()
            if self.check_connected_graph():
                successful_tests += 1

            if verbose:
                if (test_num) % (tests_amount // 4) == 0:
                    print(f"{quarter * 100 / 4}%...")
                    quarter += 1

        if timer:
            last_time = time.time()
            total_time = last_time - start_time
            print(f"Spent time: {round(total_time, ROUNDING)}")

        return successful_tests / tests_amount
    
    # FOR BRUTE FORCE:

    def gen_new_edges_graph(self, edges: List[int]):
        temp = 1
        idx = 0
        for i in range(self.vertices_num):
            for j in range(temp, self.vertices_num):
                if edges[idx] == 1:
                    self.graph[j][i] = self.graph[i][j] = 1
                else:
                    self.graph[j][i] = self.graph[i][j] = 0
                idx += 1
            temp += 1

    def enumeration(self, edges: List[int]) -> None:
        remainder = 1
        i = len(edges) - 1
        while remainder != 0:
            if edges[i] == 1:
                edges[i] = 0
                remainder = 0
            elif edges[i] == 0:
                edges[i] = 1
            i -= 1
    
    def calc_connected_graph_prob(self):
        res = 1
        temp = 1
        for i in range(self.vertices_num):
            for j in range(temp, self.vertices_num):
                if self.graph_prob[i][j] != 0:
                    if self.graph[i][j] == 1:
                        res *= self.graph_prob[i][j]
                    else:
                        res *= 1 - self.graph_prob[i][j]
            temp += 1
        return res

    def brute_force(self, verbose=False, timer=False):
        result = 0
        graph_edges = []
        temp = 1

        for i in range(self.vertices_num):
            for j in range(temp, self.vertices_num):
                if self.graph_prob[i][j] > 0:
                    graph_edges.append(1)
                else:
                    graph_edges.append(0)
            temp += 1

        count = 1

        if timer:
            start_time = time.time()

        while 1 in graph_edges:
            self.gen_new_edges_graph(graph_edges)
            if self.check_connected_graph():
                result += self.calc_connected_graph_prob()
            self.enumeration(graph_edges)

            if verbose:
                print(f"Subgraph #{count}")
                self.print_graph()
                print()
                count += 1

        self.gen_new_edges_graph(graph_edges)
        if self.check_connected_graph():
            result += self.calc_connected_graph_prob()

        if verbose:
            print(f"Subgraph #{count}")
            self.print_graph()
            print()

        if timer:
            last_time = time.time()
            total_time = last_time - start_time
            print(f"Spent time: {round(total_time, ROUNDING)}")
            
        return result

    def print_graph_prob(self):
        table = PrettyTable()
        for row in self.graph_prob:
            table.add_row(row)
        print(table.get_string(header=False))

    def print_graph(self):
        table = PrettyTable()
        for row in self.graph:
            table.add_row(row)
        print(table.get_string(header=False))