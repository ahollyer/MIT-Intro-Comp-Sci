# problem_set_02.py
# By Aspen
# An iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity. For details, see problem_set_02.md


# Hypothesize instances of numbers of McNuggets that cannot be purchased exactly, starting with one
test_range = range(1, 100)
package_sizes = (6, 9, 20)
largest_unbuyable = 0
buyable_counter = 0

# For each possible instance, n,
for n in possible_instances:
    a = 0
    b = 0
    c = 0
    # Test if there exist non-negative integers a, b, and c, such that 6a + 9b + 20c = n. (This can be done by looking at all feasible combinations of a, b, and c)
    for a in range(10):
        if 6a + 9b + 20c = n
        for b in range(10):
            if 6a + 9b + 20c = n
            for c in range(10):
                if 6a + 9b + 20c = n
    # If not, n cannot be bought in exact quantity, save n

# When you have found six consecutive values of n that pass the test of having an exact solution, the last answer that was saved is the correct answer, since we know by the theorem that any amount larger can also be bought in exact quantity.

print("Largest number of McNuggets that cannot be bought in exact quantity:", n)


def main():

main()
