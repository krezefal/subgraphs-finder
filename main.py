from colorama import Fore, Style

from graph import Graph
from consts import *

if __name__ == "__main__":
    graph = Graph(3)
    print("\nGraph:")
    graph.print_graph_prob()
    graph.gen_graph()

    print("\nProbability of occurrence of a complete graph")
    print("Start simulation")
    print(f"{Fore.GREEN}Decision: {graph.calc_complete_graph_prob(tests_amount, verbose=True, timer=True)} \
          {Style.RESET_ALL}")
    print("\nStart brute force")
    print(f"{Fore.GREEN}Decision: {graph.brute_force(verbose=True, timer=True)} {Style.RESET_ALL}")
