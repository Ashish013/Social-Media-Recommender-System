from queue import Queue
from collections import defaultdict

class SocialMediaNetwork:

    num_recommend = 2

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.person_list = []
        self.interest_list = ["music","reading","pets","nature","art","dancing","movies","sports","age"]
        self.interest_dict = defaultdict(list)
        self.edge_list = []
        self.final_recomm_people = []

    # method to add a Person to the network
    def CreatePerson(self,name,age,interests):
      if name not in self.person_list:
        self.graph[name] = []
        self.person_list.append(name)
        self.interest_dict[name] = [0] * len(self.interest_list)
        self.interest_dict[name][-1] = age
        for hobby in interests:
          self.interest_dict[name][self.interest_list.index(hobby.lower())] = 1

    # For example Interest list of Ashish is [1,0,1,1,0,0,0,1]
      else:
        print("Username " + name + " is already registered !")

    # method to add an edge to graph
    def addFriend(self,person1,person2):
      num = 0
      if person1 not in self.person_list:
        print("Username " + person1 + " not Registered !")
        num+=1
      if person2 not in self.person_list:
        print("Username " + person2 + " not Registered !")
        num+=1
      if (num != 0):
        pass
      else:
        self.graph[person1].append(person2)
        self.graph[person2].append(person1)
        self.edge_list.append((person1,person2))

    # method to recommend Connections to init_person
    def RecommendConnections(self,init_person,threshold):

      visit={}
      parent={}
      level={}
      path=[]
      queue=Queue()

      for node in self.graph.keys():
        visit[node]=False
        parent[node]=None
        level[node]=-1

      s = init_person
      queue.put(s)
      visit[s]=True
      level[s]=0

      while not queue.empty():
          v = queue.get()
          path.append(v)
          for u in self.graph[v]:
              if(not visit[u]):
                  queue.put(u)
                  visit[u]=True
                  parent[u]=v
                  level[u]=level[v]+1

      recommended_persons = [u for u in level.keys() if level[u]>1 and level[u]<= threshold]

      print("Top " + str(SocialMediaNetwork.num_recommend) + " Recommended connections suggested for " + init_person + " based on Interests and age are :")

      if (recommended_persons == []):
        print("None")
      else:
        priority_num = 1
        scores = []
        for person in recommended_persons:
          scores.append(sum([abs(self.interest_dict[init_person][x] - self.interest_dict[person][x]) for x in range(len(self.interest_list))]))

        sorted_scores = sorted(scores)
        for score in sorted_scores:
          print(str(priority_num) + ") " + recommended_persons[scores.index(score)])
          self.final_recomm_people.append(recommended_persons[scores.index(score)])
          priority_num+=1
          if (priority_num > SocialMediaNetwork.num_recommend):
            break

    def Visualize(self,init_person):
      import networkx as nx
      G = nx.Graph()
      G.add_nodes_from(self.person_list)
      G.add_edges_from(self.edge_list)

      node_colors = ["red" if (i == self.person_list.index(init_person)) else "yellow" for i in range(len(self.person_list))]
      for i in self.final_recomm_people:
        node_colors[self.person_list.index(i)] = "blue"

      node_sizes = [800 if (i == self.person_list.index(init_person)) else 400 for i in range(len(self.person_list))]
      nx.draw_networkx(G,node_color = node_colors,node_size = node_sizes)

network = SocialMediaNetwork()
network.CreatePerson("Ashish",age = 18,interests = ["pets","music","sports","nature"])
network.CreatePerson("Anish",age = 25,interests = ["Music","Dancing","Sports"])
network.CreatePerson("Vijay",age = 23,interests=["sports","reading","nature"])
network.CreatePerson("Nishanth",age = 26,interests=["sports","Nature"])
network.CreatePerson("Subash",age = 34,interests=["Movies","Pets"])
network.CreatePerson("Naman",age = 37,interests=["Music","art"])

network.addFriend("Ashish","Anish")
network.addFriend("Anish","Naman")
network.addFriend("Anish","Nishanth")
network.addFriend("Ashish", "Vijay")
network.addFriend("Subash","Vijay")
network.addFriend("Subash","Naman")

#print(network.graph)

network.RecommendConnections("Ashish",threshold = 2)
network.Visualize("Ashish")