from django.shortcuts import render
map = {'busca binária': "Algorithms/Tecniques/binary_search.html",
       'busca ternária': "Algorithms/Tecniques/ternary_search.html",
       'dfs': "Algorithms/Graph/DFS.html",
       'bfs': "Algorithms/Graph/BFS.html",
       'mochila': "Algorithms/Dynamic_programming/Knapsack.html",
       'lca': "Algorithms/Graph/LCA.html"}
def algorithms(request): 
    return render(request,"Algorithms.html",{'header': "Algoritmos"})

def algorithm(request, algorithm):
    if algorithm == "busca binaria":
        algorithm = "busca binária"
    if algorithm == "busca ternaria":
        algorithm = "busca ternária"
    #remove ternary to publish
    return render(request,(map[algorithm] if (algorithm in map) else "Algorithm.html"),{'algorithm': algorithm.capitalize(), 'header': algorithm.capitalize()})