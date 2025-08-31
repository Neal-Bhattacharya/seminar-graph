import random

import pygraphviz as pgv
import networkx as nx

from processor.processor import Processor

G = pgv.AGraph(directed=True)

p = Processor()
p.run()

edges = p.get_edges()
colors = set()
author_colors = {}
print("Generating graph...")
def get_color():
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    while color in colors:
        color = '#%02X%02X%02X' % (r(), r(), r())
    colors.add(color)
    return color

for e in edges:
    if e[0] not in author_colors:
        author_colors[e[0]] = get_color()
    if e[1] not in author_colors:
        author_colors[e[1]] = get_color()

for e in edges:
    G.add_edge(e[0], e[1])
    edge = G.get_edge(e[0], e[1])
    edge.attr['label'] = e[2]
    edge.attr['fontname'] = 'Didot'
    edge.attr['color'] = author_colors[e[0]]
    tooltip = "{} mentioned by {} {} time{}".format(e[0], e[1], e[2], "s" if e[2] > 1 else "")
    edge.attr['tooltip'] = tooltip

for node in G.nodes():
    node.attr['fontname'] = 'Didot'
    node.attr['color'] = author_colors[node]


G.layout(prog='dot')
G.draw('graph.png')
G.draw('graph.svg', args='')
N = nx.DiGraph(G)
max_out = ("", -1)
max_in = ("", -1)
sources = []
sinks = []

for node in G.nodes():
    out_deg = G.out_degree(node)
    in_deg = G.in_degree(node)
    if out_deg > max_out[1]: max_out = (node, out_deg)
    if out_deg == 0: sinks.append(node)
    if in_deg > max_in[1]: max_in = (node, in_deg)
    if in_deg == 0: sources.append(node)

p.print_done()

print("Results:")
print("Max out:" , max_out)
print("Max in: ", max_in)
print("Sources:", ", ".join(sources))
print("Sinks:", ", ".join(sinks))
#lp = nx.dag_longest_path(nx.DiGraph(G))
#print(str(lp))
