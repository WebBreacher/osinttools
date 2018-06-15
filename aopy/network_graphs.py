'''import networkx as nx
import matplotlib.pyplot as plotter

G = nx.Graph()

G.add_edge("Justin Seitz","automatingosint.com")
G.add_edge("jms_dot_py","Justin Seitz")
G.add_edge("justin@automatingosint.com","automatingosint.com")
G.add_edge("justin@automatingosint.com","Justin Seitz")

nx.draw(G,with_labels=True)
plotter.show()'''

import networkx as nx
import matplotlib.pyplot as plotter

G = nx.Graph()

G.add_edge("Justin Seitz","Scary Hacker 1")
G.add_edge("Justin Seitz","Scary Hacker 2")
G.add_edge("micah", "Scary Hacker 5")
G.add_edge("Justin Seitz","micah")
G.add_edge("Scary Hacker 4", "Scary Hacker 2")
G.add_edge("Justin Seitz","Scary Hacker 6")
G.add_edge("Scary Hacker 5","Scary Hacker 6")
G.add_edge("Scary Hacker 3", "Scary Hacker 2")
G.add_edge("Scary Hacker 4", "Scary Hacker 3")


connections = nx.shortest_path(G,"Justin Seitz","Scary Hacker 4")
print(" => ".join(connections))



nx.draw(G,with_labels=True)
plotter.show()