import numpy as np
import math
import pandas as pd
from tree import Tree
NAME = 0
XCOR = 1
YCOR = 2
SCORE = 3
FOODPRICE = 4


class restaurantFinder:
    # name[0]	xcor[1]	ycor[2]	score[3]	foodPrice[4]
    def __init__(self):
        """Initializes the restaurantFinder class

        Args:
            restaurants (npArray): Array of restaurants
            method (string): Method to use
            time (int): Time
            money (int): Money
        """
        df = pd.read_csv("data/restaurants.csv")
        self.restaurants = np.array(df)
        self.method = "greedy"
        self.time = 240
        self.money = 500
        self.root = Tree(None, None)
        self.runMethod()

    def runMethod(self):
        if self.method == "greedy":
            return self.greedyBestFirstSearch(self.money, self.time)
        else:
            return self.aStarSearch(self.money, self.time)

    def getDistance(self, firstRestaurant, secondRestaurant):
        """Calculates the distance between two restaurants

        Args:
            firstRestaurant (npArray): First restaurant
            secondRestaurant (npArray): Second restaurant

        Returns:
            int: Distance between the two restaurants
        """
        if firstRestaurant is None or secondRestaurant is None:
            return math.floor(
                np.sqrt((0 - secondRestaurant[XCOR])**2 + (0 - secondRestaurant[YCOR])**2))

        return math.floor(np.sqrt((firstRestaurant[XCOR] - secondRestaurant[XCOR])**2 + (firstRestaurant[YCOR] - secondRestaurant[YCOR])**2))

    def countTotalScore(self, restaurants):
        totalScore = 0
        for restaurant in restaurants:
            totalScore += restaurant[SCORE]
        return totalScore

    def getRestaurantsInRadius(self, xcor, ycor, radius):
        """Finds all restaurants within a certain radius

        Args:
            xcor (float): X coordinate
            ycor (float): Y coordinate
            radius (float): Radius

        Returns:
            npArray: Array of restaurants
        """
        restaurants = []
        for restaurant in self.restaurants:
            if self.getDistance(restaurant, [0, xcor, ycor]) <= radius:
                restaurants.append(restaurant)
        return restaurants

    def bestRestaurant(self,  visitedRestaurants, visitedMoney, visitedTime, visitedRestaurant):
        """ Finds the best restaurant
        Args:
            restaurants (npArray): Array of restaurants
            visitedRestaurants (npArray): Array of visited restaurants
            visitedMoney (int): Money spent on visited restaurants
            visitedTime (int): Time spent on visited restaurants
            visitedRestaurant (npArray): Visited restaurant

        Returns:
            npArray: Best restaurant

            """
        bestRestaurant = None
        bestScore = 0
        minCost = math.inf

        print(visitedRestaurants)
        for restaurant in self.restaurants:
            # eating take 15 min
            cost = self.getDistance(visitedRestaurant, restaurant)
            flag = True
            if 15 + visitedTime + cost <= self.time:
                if restaurant[FOODPRICE] + cost + visitedMoney <= self.money:
                    for visited in visitedRestaurants:
                        if (restaurant == visited).all():
                            flag = False
                    # if restaurant[SCORE] > bestScore and restaurant not in visitedRestaurants:
                    if restaurant[SCORE] >= bestScore and flag and cost < minCost:
                        bestRestaurant = restaurant
                        bestScore = restaurant[SCORE]
                        minCost = cost
        return bestRestaurant

    def greedyBestFirstSearch(self, money, time):
        """Greedy Best First Search

        Args:
            money (int): Money
            time (int): Time

        Returns:
            npArray: Array of restaurants
        """
        visitedRestaurants = []
        visitedMoney = 0
        visitedTime = 0
        visitedRestaurant = None
        while True:
            bestRestaurant = self.bestRestaurant(
                visitedRestaurants, visitedMoney, visitedTime, visitedRestaurant)
            if bestRestaurant is None:
                break
            visitedRestaurants.append(bestRestaurant)
            cost = self.getDistance(visitedRestaurant, bestRestaurant)
            visitedMoney += bestRestaurant[FOODPRICE] + cost
            visitedTime += 15 + cost
            visitedRestaurant = bestRestaurant
        return visitedRestaurants

    def find(self, name):
        for restaurant in self.restaurants:
            if restaurant[0] == name:
                return restaurant
        return None


if __name__ == "__main__":
    result = restaurantFinder().runMethod()
    print(result)
    print(restaurantFinder().countTotalScore(result))
