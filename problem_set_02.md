## Problem Set 2
### MIT 6.00 Introduction to Computer Science & Programmming

-----

### McDiophantine: Selling McNuggets

From the MIT OpenCourseWare:

> "McDonald's sells Chicken McNuggets in packages of 6, 9, or 20 McNuggets. Thus, it is possible, for example, to buy exactly 15 McNuggets . . . but it is not possible to buy exactly 16 nuggets . . . . To determine if it is possible to buy exactly n McNuggets, one has to solve a Diophantine equation: find non-negative integer values of a, b, and c, such that 6a + 9b + 20c = n."

-----

#### Problem 1.

Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets by finding solutions to the Diophantine equation.

##### Solution:

6a + 9b + 20c = 50,
a = 5,
b = 0,
c = 1

6a + 9b + 20c = 51,
a = 7,
b = 1,
c = 0

6a + 9b + 20c = 52,
a = 2,
b = 0,
c = 2

6a + 9b + 20c = 53,
a = 1,
b = 3,
c = 1

6a + 9b + 20c = 54,
a = 0,
b = 6,
c = 0

6a + 9b + 20c = 55,
a = 1,
b = 1,
c = 2

--------

#### Problem 2.

> *Theorem:* If it is possible to buy x, x+1,..., x+5 sets of McNuggets, for some x, then it is possible to buy any number of McNuggets >= x, given that McNuggets come in 6, 9, and 20 packs.
>
> Explain, in English, why this theorem is true.

##### Solution:

After researching on the web, I understand that if you can find a set of sequential solutions that is as long as the smallest counting unit, then you can count to any subsequent number by adding the smallest counting unit to your set of sequential solutions. In this case, the smallest counting unit is 6. The set of sequential solutions is x, x+1,..., x+5 (that is, our solutions for 50-55).

*TL;DR:* We have 6 sequential solutions, and 6 is our smallest counting unit.

------

#### Problem 3.

> Write an iterative program that finds the largest number of McNuggets that *cannot* be bought in exact quantity. Your program should print the answer in the following format (where the correct number is provided in place of <n>):
>
> "Largest number of McNuggets that cannot be bought in exact quantity: <n>"

##### Solution:

See problem_set_02.py
