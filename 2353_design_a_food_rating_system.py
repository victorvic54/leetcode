import heapq

class Food:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating > other.rating

        return self.name < other.name

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine_rating = {}
        for i in range(len(foods)):
            self.food_to_cuisine_rating[foods[i]] = (cuisines[i], ratings[i])

        self.cuisine_to_rating_food = defaultdict(list)
        for i in range(len(foods)):
            heapq.heappush(self.cuisine_to_rating_food[cuisines[i]], Food(foods[i], ratings[i]))


    def changeRating(self, food: str, new_rating: int) -> None:
        old_cuisine, old_rating = self.food_to_cuisine_rating[food]
        self.food_to_cuisine_rating[food] = (old_cuisine, new_rating)
        heapq.heappush(self.cuisine_to_rating_food[old_cuisine], Food(food, new_rating))
        

    def highestRated(self, cuisine: str) -> str:
        food_obj = self.cuisine_to_rating_food[cuisine][0]
        if self.food_to_cuisine_rating[food_obj.name][1] != food_obj.rating:
            heapq.heappop(self.cuisine_to_rating_food[cuisine])
            return self.highestRated(cuisine)
        
        return food_obj.name
        

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
