import numpy as np
NAME = 0
XCOR = 1
YCOR = 2
SCORE = 3
FOODPRICE = 4

class restaurantFinder:
    # name[0]	xcor[1]	ycor[2]	score[3]	foodPrice[4]
    def __init__(self, restaurants):
        """Constructor for restaurantFinder

        Args:
            restaurants (npArray): Array of restaurants
        """
        self.restaurants = restaurants

    def getDistance(self, firstRestaurant, secondRestaurant):
        """Calculates the distance between two restaurants

        Args:
            firstRestaurant (npArray): First restaurant
            secondRestaurant (npArray): Second restaurant

        Returns:
            float: Distance between the two restaurants
        """
        return np.sqrt((firstRestaurant[XCOR] - secondRestaurant[XCOR])**2 + (firstRestaurant[YCOR] - secondRestaurant[YCOR])**2)

    def getRestaurants(self, xcor, ycor, radius):
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
    

    def find(self, name):
        for restaurant in self.restaurants:
            if restaurant[0] == name:
                return restaurant
        return None
