import pygraphviz as pgv
import networkx as nx

from processor.processor import Processor

G = pgv.AGraph(directed=True)

p = Processor()
p.run()
print(p.get_edges())
print("Generating graph...")
for e in p.get_edges():
    G.add_edge(e[0], e[1])
    edge = G.get_edge(e[0], e[1])
    edge.attr['label'] = e[2]
    edge.attr['fontname'] = 'Didot'
    edge.attr['tooltip'] = "{} mentioned by {} {} time{}".format(e[0], e[1], e[2], "s" if e[2] > 1 else "")
for node in G.nodes(): node.attr['fontname'] = 'Didot'

G.layout(prog='dot')
G.draw('graph.png')
G.draw('graph.svg')
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
