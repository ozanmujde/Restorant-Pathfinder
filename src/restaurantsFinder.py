import math

import numpy as np
import pandas as pd
from numpy.random import rand, randint

np.random.seed(0)

NAME = 0
XCOR = 1
YCOR = 2
SCORE = 3
FOODPRICE = 4


class restaurantFinder:
    # name[0]	xcor[1]	ycor[2]	score[3]  foodPrice[4]
    def __init__(self):
        """Initializes the restaurantFinder class

        Args:
            restaurants (npArray): Array of restaurants
            method (string): Method to use
            time (int): Time
            money (int): Money
        """
        df = pd.read_csv("data/restaurants.csv")
        self.city_list = list(range(0, 100))

        self.restaurants = np.array(df)
        self.method = "genetic"
        self.time = 240
        self.money = 500

        self.runMethod()

    def runMethod(self):
        # define the total iterations
        n_iter = 100
        # visitNumber
        visitNumber = 10
        # define the population size
        n_pop = 100
        # crossover rate
        r_cross = 0.9
        # mutation rate
        r_mut = 1.0 / float(visitNumber)
        if self.method == "greedy":
            return self.greedyBestFirstSearch(self.money, self.time)
        else:
            return self.genetic_algorithm(
                self.objective_function, visitNumber, n_iter, n_pop, r_cross, r_mut
            )

    def getDistance(self, firstRestaurant, secondRestaurant):
        """Calculates the distance between two restaurants

        Args:
            firstRestaurant (npArray): First restaurant
            secondRestaurant (npArray): Second restaurant

        Returns:
            int: Distance between the two restaurants
        """
        # if firstRestaurant is None or secondRestaurant is None:
        if firstRestaurant is None:
            return math.floor(
                np.sqrt(
                    (0 - secondRestaurant[XCOR]) ** 2
                    + (0 - secondRestaurant[YCOR]) ** 2
                )
            )

        return math.floor(
            np.sqrt(
                (firstRestaurant[XCOR] - secondRestaurant[XCOR]) ** 2
                + (firstRestaurant[YCOR] - secondRestaurant[YCOR]) ** 2
            )
        )

    def countTotalScore(self, restaurants):
        totalScore = 0
        if self.method == "greedy":
            for restaurant in restaurants:
                totalScore += restaurant[SCORE]
        else:
            for restaurant in restaurants[0]:
                totalScore += self.restaurants[restaurant][SCORE]
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

    def bestRestaurant(
        self, visitedRestaurants, visitedMoney, visitedTime, visitedRestaurant
    ):
        """Finds the best restaurant
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
                    if restaurant[SCORE] >= bestScore and flag and cost <= minCost:
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
                visitedRestaurants, visitedMoney, visitedTime, visitedRestaurant
            )
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

    def crossOver(self, p1, p2, r_cross):
        """Performs crossover between two parents

        Args:
            p1 (Array): First Parent
            p2 (Array): Second Parent
            r_cross (float): Crossover rate

        Returns:
            Array: Array of two children
        """
        # children are copies of parents by default
        c1, c2 = p1.copy(), p2.copy()
        # check for recombination
        if rand() < r_cross:
            # select crossover point that is not on the end of the string
            pt = randint(1, len(p1))
            length = len(p1) - pt
            c1 = p1[:pt]
            c2 = p2[:pt]
            # perform crossover
            # c1 = p1[:pt] + p2[pt:]
            # c2 = p2[:pt] + p1[pt:]
            for city in p2:
                if len(c1) == len(p1):
                    break
                if not city in c1:
                    c1.append(city)
                else:
                    tempNumber = randint(low=0, high=99)
                    while tempNumber in c1:
                        tempNumber = randint(low=0, high=99)
                    c1.append(tempNumber)

            for city in p1:
                if len(c2) == len(p2):
                    break
                if not city in c2:
                    c2.append(city)
                else:
                    tempNumber = randint(low=0, high=99)
                    while tempNumber in c2:
                        tempNumber = randint(low=0, high=99)
                    c2.append(tempNumber)

            # for city in p1:
            #     if not city in c2:
            #         c2 = np.concatenate((c2,[city]))
        return [c1, c2]

    def mutation(self, array, r_mut):
        for i in range(len(array)):
            # array[i] = randint(low=0, high=99)
            # check for a mutation
            if rand() < r_mut:
                flag = True
                # change the value
                tempNumber = randint(low=0, high=99)
                while tempNumber in array:
                    tempNumber = randint(low=0, high=99)
                array[i] = tempNumber

    def selection(self, pop, scores, k=3):
        # first random selection
        selection_ix = randint(len(pop))
        for ix in randint(0, len(pop), k - 1):
            # check if better (e.g. perform a tournament)
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return pop[selection_ix]

    def objective_function(self, x):
        """Objective function for genetic algorithm

        Args:
            x (Array): Array of visited restaurants

        Returns:
            float: Objective function value
        """
        totalScore = 0
        prevRestaurant = None
        for restaurant in x:
            totalScore += self.restaurants[restaurant][SCORE]
            # if prevRestaurant is not None:
            #     totalScore -= self.getDistance(
            #         self.restaurants[prevRestaurant], self.restaurants[restaurant]) / 5
            # else:
            #     totalScore -= self.getDistance(None,
            #                                    self.restaurants[restaurant]) / 5
            prevRestaurant = restaurant
        return -totalScore

    def genetic_algorithm(self, objective, visitNumber, n_iter, n_pop, r_cross, r_mut):
        # initial population of random bitstring
        pop = [
            np.random.choice(list(range(0, 100)), visitNumber, replace=False).tolist()
            for _ in range(n_pop)
        ]

        # keep track of best solution
        best, best_eval = 0, objective(pop[0])
        # enumerate generations
        for gen in range(n_iter):
            # evaluate all candidates in the population
            scores = [objective(c) for c in pop]
            # check for new best solution
            for i in range(n_pop):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
            # select parents
            selected = [self.selection(pop, scores) for _ in range(n_pop)]
            # create the next generation
            children = list()
            for i in range(0, n_pop, 2):
                # get selected parents in pairs
                p1, p2 = selected[i], selected[i + 1]
                # crossover and mutation
                for c in self.crossOver(p1, p2, r_cross):
                    # mutation
                    self.mutation(c, r_mut)
                    # store for next generation
                    children.append(c)
            # replace population
            pop = children
        return [best, best_eval]


if __name__ == "__main__":
    result = restaurantFinder().runMethod()
    print(result)
    print(restaurantFinder().countTotalScore(result))
