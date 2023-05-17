from colorama import Fore, Style

from graph import Graph
from parser_ import parse_args

if __name__ == "__main__":
    mtx_size, tests_number, manual_input, verbose, timer = parse_args()

    if manual_input:
        adj_mtx = []
        print("Enter adjacency matrix")
        for i in range(1, mtx_size + 1):
            row = list(map(float, input(f"Row #{i}: ").strip().split()))
            if len(row) != mtx_size:
                raise ValueError('Incorrect matrix row length')
            adj_mtx.append(row)
        graph = Graph(mtx_size, adj_mtx)
    else:
        graph = Graph(mtx_size)

    print("\nGraph:")
    graph.print_graph_prob()
    graph.gen_graph()

    print("\nProbability of occurrence of a complete graph")
    print("Start simulation")
    print(f"{Fore.GREEN}Decision: " \
          f"{graph.calc_complete_graph_prob(tests_number, verbose, timer)}" \
          f"{Style.RESET_ALL}")
    
    print("\nStart brute force")
    print(f"{Fore.GREEN}Decision: {graph.brute_force(verbose, timer)}" \
          f"{Style.RESET_ALL}")
