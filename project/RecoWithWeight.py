from .grapher import Graph
import heapq

class RecoWithWeight:

    def __init__(self):
        self.network = Graph()

    def add_connection(self, user1, user2):
        self.network.add_edge(user1, user2, 1000, "user")

    def user1_liked_user2_post(self, user1, user2):
        weight = self.network.get_weight(user1, user2)
        if not weight:
            self.network.add_edge(user1, user2, 1000, "post")
        elif weight > 0:
            self.network.add_edge(user1, user2, weight - 2, "post")
        else:
            self.network.add_edge(user1, user2, 0, "post")

    def user1_commented_user2_post(self, user1, user2):
        weight = self.network.get_weight(user1, user2)
        if not weight:
            self.network.add_edge(user1, user2, 1000, "post")
        elif weight > 0:
            self.network.add_edge(user1, user2, weight - 4, "post")
        else:
            self.network.add_edge(user1, user2, 0, "post")

    def get_mutual_friends(self, user1, user2):
        mutual_count = 0
        mutual_friends = list()
        if self.network.has_vertex(user1) and self.network.has_vertex(user2):
            neighbour = self.network.get_neighbour_names(user1)
            for friend in neighbour:
                if self.network.has_edge(friend, user2) and self.network.has_edge(friend, user1):
                    mutual_count += 1
                    mutual_friends.append(friend)
        mutual = []
        mutual.append(mutual_friends)
        mutual.append(mutual_count)
        return mutual

    def get_people_you_may_know(self, user):
        recommended_friends= list()
        d = self.network.find_shortest_path(user)
        neighbours = self.network.get_neighbours(user)
        d.pop(user)


        for n in neighbours:
            d.pop(n[0])

        pq = []
        for el in d:
            heapq.heappush(pq, [d[el], el])

        counter = 0
        while len(pq) > 0:
            counter += 1
            data = heapq.heappop(pq)
            if data[0] == float('inf'):
                if self.network.has_edge(data[1],user):
                    recommended_friends.append(data[1])
            else:
                recommended_friends.append(data[1])

        return recommended_friends