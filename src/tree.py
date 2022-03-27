class Tree:
    def __init__(self, restaurant, parentNode=None):
        self.value = Node(None, 0, 0, 0)
        self.children = []
        self.parent = parentNode

    def addChild(self, restaurant, time, money, totalScore):
        self.children.append(Node(self, restaurant, time, money, totalScore))

    def removeChild(self, restaurant, time, money, totalScore):
        self.children.remove(Node(self, restaurant, time, money, totalScore))

    def updateNodeValue(self, Node, totalScore):
        Node.totalScore = totalScore

    def updateParentNodeValue(self, totalScore):
        self.parent.updateNodeValue(self.parent, totalScore)


class Node:
    def __init__(self, restaurant, time, money, totalScore):
        self.restaurant = restaurant
        self.time = time
        self.money = money
        self.totalScore = totalScore
