from collections import Counter

"""
Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has
in his shop. There are N number of customers who are willing to pay X[i] amount of money only if they get the shoe
of their desired size. Your task is to compute how much money Raghu earned.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    number_of_shoes: int = int (input ())
    shoes: Counter = Counter ([int (x) for x in input ().split ()])
    number_of_customers: int = int (input ())
    income: int = 0

    for _ in range (number_of_customers):
        shoe_size, price = tuple ([int (x) for x in input ().split ()])

        if shoe_size in shoes.keys () and shoes[shoe_size] > 0:
            income += price
            shoes[shoe_size] -= 1

    print (income)
