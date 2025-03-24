# # 24/03/2025
# import random 

# # random(): It returns a random float value between 0 and 1.
# print(random.random())

# # uniform(): It returns a random float value between the specified range (a and b).
# print(random.uniform(4, 10))

# # randint(): It returns a random integer between the specified range (a and b).
# print(random.randint(5, 10))

# # randrange(): It returns a random integer in a specified range, but the end value is exclusive.
# print(random.randrange(10))  # Random integer from 0 to 9.
# print(random.randrange(5, 10))  # Random integer from 5 to 9.
# print(random.randrange(1, 15, 3))  # Random integer from 1 to 14 with a step of 3.

# # choice(): It returns a random element from a specified list.
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Random choice from numbers 1 to 10.
# print(random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))  # Random choice from letters.

# # shuffle(): It shuffles the items in the list randomly.
# # Note: shuffle() modifies the list in place and doesn't return the shuffled list.
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(list1)  # Randomly shuffle list1.
# print(list1)

# list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# random.shuffle(list2)  # Randomly shuffle list2.
# print(list2)

#####or EXTRA EG#####
# import random

# # random(): Returns a random float between 0 and 1.
# print("random():", random.random())

# # uniform(a, b): Returns a random float between a and b (inclusive of both).
# print("uniform(4, 10):", random.uniform(4, 10))

# # randint(a, b): Returns a random integer between a and b (inclusive of both).
# print("randint(5, 10):", random.randint(5, 10))

# # randrange(start, stop, step): Returns a random integer in the range [start, stop), with an optional step value.
# print("randrange(10):", random.randrange(10))  # Random integer from 0 to 9.
# print("randrange(5, 10):", random.randrange(5, 10))  # Random integer from 5 to 9.
# print("randrange(1, 15, 3):", random.randrange(1, 15, 3))  # Random integer from 1 to 14 with a step of 3.

# # choice(seq): Returns a random element from the provided sequence (list, string, etc.).
# print("choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))  # Random choice from a list of numbers.
# print("choice(['a', 'b', 'c', 'd']):", random.choice(['a', 'b', 'c', 'd']))  # Random choice from a list of characters.

# # shuffle(seq): Randomly shuffles the elements of the list in place (modifies the original list).
# list1 = [1, 2, 3, 4, 5]
# random.shuffle(list1)  # Shuffling the list.
# print("shuffle([1, 2, 3, 4, 5]):", list1)

# # sample(seq, k): Returns a random sample of k unique elements from the sequence (without replacement).
# print("sample([1, 2, 3, 4, 5], 3):", random.sample([1, 2, 3, 4, 5], 3))  # Random sample of 3 elements from the list.

# # seed(a=None): Initializes the random number generator to make the results reproducible.
# random.seed(42)  # Setting the seed for reproducibility.
# print("seed(42) - random number after setting seed:", random.random())  # Random number after setting the seed.

# # betavariate(alpha, beta): Returns a random float following the Beta distribution.
# print("betavariate(2, 5):", random.betavariate(2, 5))

# # gammavariate(alpha, beta): Returns a random float following the Gamma distribution.
# print("gammavariate(2, 3):", random.gammavariate(2, 3))

# # normalvariate(mu, sigma): Returns a random float following a normal (Gaussian) distribution.
# print("normalvariate(0, 1):", random.normalvariate(0, 1))

# # lognormvariate(mu, sigma): Returns a random float following a log-normal distribution.
# print("lognormvariate(0, 1):", random.lognormvariate(0, 1))

# # paretovariate(alpha): Returns a random float following a Pareto distribution.
# print("paretovariate(2):", random.paretovariate(2))

# # triangular(low, high, mode): Returns a random float following a triangular distribution.
# print("triangular(0, 10, 5):", random.triangular(0, 10, 5))

# # weibullvariate(alpha, beta): Returns a random float following a Weibull distribution.
# print("weibullvariate(1, 1):", random.weibullvariate(1, 1))


# Wap Generate a 4-digit OTP
# import random
# for i in range(4) :
#     otp = random.randint(1000, 9999)
#     otp_with_spaces = ' '.join(str(otp))
#     print(otp_with_spaces)


# for j in range (4):
#     for i in range(4):
#     print(random.randint(0,9).end=" ")
# print()

