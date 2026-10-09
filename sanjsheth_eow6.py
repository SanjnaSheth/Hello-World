# Sanjna Sheth
# 10/5/2025
# end of week assignment-week 6


# Exercise 1
# Orginal list of employees and printed list
employees = ["Bob", "Carlos", "Alice"]
print(employees)
# Add Dana as an employee to the list and print list
employees.append("Dana")
print(employees)
# Remove Bob from the employee list and print list
employees.remove("Bob")
print(employees)
# Make Evelyn the first name in list due to status and print list
employees.insert(0, "Evelyn")
print(employees)
# Sort employee names by alphabet order and print list
employees.sort()
print(employees)

print("")

# Exercise 2
# List of ratings by customers
ratings = [5, 4, 3, 5, 5, 5, 2, 3, 3, 3, 3, 2, 5, 4, 3]
# See if any 5 star ratings are in list
any_five = 5 in ratings
print("There are 5's in the rating list:", any_five)
# How many 5 star ratings are there?
number_of_five = ratings.count(5)
print("The number of fives in the ratings:", number_of_five)
# What is the average of all the ratings earned
average = sum(ratings) / len(ratings)
print("The average for all ratings is:", average)
# if rating is 1 then you have to show that the rating is low
if 1 in ratings:
    print("Low rating exists.")
# if no one star ratings are found then show user this message
else:
    print("No 1-star ratings found")

print("")
# Exercise 3
# inventory stock list displayed
stock = [120, 45, 300, 53, 90, 6, 200, 108, 43, 2]
# sort inventory stock in ascending order and print it
stock.sort()
print(stock)
# sort inventory stock in descending order and print it
stock.sort(reverse=True)
print(stock)

print("")
# Exercise 4
# list of revenue amounts for the year
revenue = [
    12000,
    15000,
    14000,
    16000,
    18000,
    17000,
    20000,
    21000,
    19000,
    22000,
    23000,
    24000,
]
# divide the revenue amounts into quarters and print the lists for each quarter
q1 = revenue[0:3]
print("Q1:", q1)
q2 = revenue[3:6]
print("Q2:", q2)
q3 = revenue[6:9]
print("Q3:", q3)
q4 = revenue[9:12]
print("Q4:", q4)

print("")
# for each quarter calculate the total sum of that quarter sales and the average of the sum
total_one = sum(q1)
average_one = total_one / 3
print("Total:", total_one, ", Average:", round(average_one, 2))

total_two = sum(q2)
average_two = total_two / 3
print("Total:", total_two, ", Average:", average_two)

total_three = sum(q3)
average_three = total_three / 3
print("Total:", total_three, ", Average:", average_three)

total_four = sum(q4)
average_four = total_four / 3
print("Total:", total_four, ", Average:", average_four)

# Exercise 5
# List of things purchased by consumers
customer_purchases = [
    "milk",
    ["milk", "bread", "eggs"],
    "bread",
    ["milk", "bread", "eggs", "tp"],
]

# how many customers were there
print("Number of customers", len(customer_purchases))
# report if tp was in the things consumers bought
if "tp" in customer_purchases:
    print("Tp purchased:", "False")
else:
    print("Tp purchased:", "True")
# covert tp into butter and print the deepcopy
import copy

deep = copy.deepcopy(customer_purchases)
deep[8] = "butter"
print("Orginal List:", customer_purchases)
print("Deep Copy:", deep)
