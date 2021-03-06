#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Completing a Tree
URL: http://rosalind.info/problems/tree/

Given: A positive integer n (n <= 1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

def countEdges(n, adj_list):
    return(n - len(adj_list) - 1)
    
def main(): 
    with open('problem_datasets/rosalind_tree.txt', 'r') as infile:
        n = int(infile.readline())
        adj_list = infile.readlines()
            
    print(countEdges(n, adj_list))

if __name__ == '__main__':
    main()
