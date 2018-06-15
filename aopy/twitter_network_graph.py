import networkx as nx

followers_file = "webbreacher-1529088541.363703-followers.txt"
friends_file   = "webbreacher-1529088541.363703-friends.txt"

# load the friends list
target    = "webbreacher"

with open(followers_file,"rb") as fd:
    followers = fd.read().splitlines()

with open(friends_file,"rb") as fd:
    friends   = fd.read().splitlines()

# create the graph object
graph = nx.DiGraph()


# iterate over the friends list and add them to the graph
for friend in friends:
    
    graph.add_edge(target,friend)
    
# iterate over the followers list and add them to the graph
for follower in followers:
    
    graph.add_edge(follower,target)
    

nx.write_gexf(graph,"%s.gexf" % target)

print("[*] Wrote out graph for %s mapping %d friends and %d followers." % (target,len(friends),len(followers)))