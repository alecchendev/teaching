---
title: Modular Arithmetic
description: Like arithmetic, but modular!
---

[//]: # (
Note: another way to think about modular arithmetic is just dividing and taking
the remainder. This doesn't work that well as an analogy for subtraction tho.

Would be great to make a visualization of chopping a number
into blocks and taking the last block. Or maybe a clock of some sorts.
)

[//]: # (content)
## Introduction

Modular arithmetic is like normal arithmetic on integers (addition, subtraction, multiplication,
division), but each operation it performed *modulo* some number, $m$. Performing
an operation modulo some number $m$ means doing normal arithmetic, but *wrapping
around* at $m$.

For example:

Addition: $5 + 6 = 4 \ (mod \ 7)$

Normally, $5 + 6 = 11$, but we wrap around at seven, so our result is $11 - 7 = 4$.

Addition with larger numbers: $30 + 46 = 6 \ (mod \ 7)$. Here we'd normally get $70$, but
we keep wrapping around over and over until we can't anymore.

It works similarly for subtraction, but it wraps around the other way for negative
numbers.

Subtraction: $4 - 7 = 5 \ (mod \ 8)$.

Normally we'd get $4 - 7 = -3$ but when we hit $0$, we wrap around back to $8$.

Modular multiplication is similar to addition or subtraction, since multiplication
is simply repeated addition/subtraction.

Multiplication: $3 * 12 = 4 \ (mod \ 16)$

Normally we'd get $3 * 12 = 36$, but it wraps at $16$, so $36 - 16 = 20$, and wrap
again, $20 - 16 = 4$.

In a nutshell, when doing arithmetic modulo an integer $m \geq 1$:

1. Do arithmetic as normal
2. If the result is greater than or equal to $m$, subtract $m$.
3. If the result is less than $0$, add $m$.

[//]: # (question)
What is $x$ if $9 * 7 = x \ (mod \ 11)$

[//]: # (choice)
12

[//]: # (choice correct)
8

[//]: # (choice)
10

[//]: # (choice)
3

[//]: # (explanation)
$$
9 * 7 = 63
\\
63 - 11 - 11 - 11 - 11 - 11 = 63 - 55
\\
= 8 \ (mod \ 11)
$$

[//]: # (question)
What is $x$ if $25 * 4 + 20 = x \ (mod \ 10)$

[//]: # (choice)
10

[//]: # (choice correct)
0

[//]: # (choice)
24

[//]: # (choice)
8

[//]: # (explanation)
$$
m = 10
\\
25 * 4 + 20 = 100 + 20 = 120
\\
120 \geq 10
\\
120 - 10 - 10 - 10 ...
\\
= 0 \ (mod \ 10)
$$

[//]: # (content)
## More modular arithmetic

A neat trick with modular arithmetic when you're working with larger
numbers is that you can perform the modulo operation at each step.

When you see $(mod \ m)$ at the right side of an expression or equation, it means
*all operations and numbers* are modulo $m$.

Say we want to calculate $x$ where $22 * 3 = x \ (mod \ 9)$.

We can calculate the modulo at each step, and even on each number itself:

$$
22 = 4 \ (mod \ 9)
\\
22 * 3 \ (mod \ 9) = (22 \ mod \ 9) * 3 \ (mod \ 9) = 4 * 3 \ (mod \ 9)
$$

Is this true? Let's see:

$$
22 * 3 = 66
\\
66 - 9 - 9 - 9 - ... = 66 - 63 = 3
\\
22 * 3 = 3 \ (mod \ 9)
$$

And with the shortcut:

$$
4 * 3 = 12
\\
12 = 3 \ (mod \ 9)
$$

Similarly, we can perform the modulo operation at individual steps:

For example: $(14 + 11) * 5 \ (mod \ 16)$

$$
(14 + 11) = 25 = 9 \ (mod \ 16)
\\
(14 + 11) * 5 \ (mod \ 16)
\\
= (25 \ mod \ 16) * 5 \ (mod \ 16)
\\
= 9 * 5 = 45 = 13 \ (mod \ 16)
$$

And if we brute force it:

$$
(14 + 11) * 5 = 125
\\
125 - 16 - 16 - 16 = 125 - 112 = 13
\\
(14 + 11) * 5 = 13 \ (mod \ 16)
$$


[//]: # (question)
What is $x$ if $(13 + 20) * 4 = x \ (mod \ 10)$

[//]: # (choice)
0

[//]: # (choice)
4

[//]: # (choice)
8

[//]: # (choice correct)
2

[//]: # (explanation)
$$
(13 + 20) * 4 \ (mod \ 10)
\\
= (33 \ mod \ 10) * 4 \ (mod \ 10)
\\
= (3) * 4 = 12 \ (mod \ 10)
\\
= 2 \ (mod \ 10)
$$

[//]: # (question)
What is $x$ if $(7 * 68) + 27 = x \ (mod \ 9)$

[//]: # (choice)
4

[//]: # (choice)
6

[//]: # (choice correct)
8

[//]: # (choice)
7

[//]: # (explanation)
$$
(7 * 68) + 27 \ (mod \ 9)
\\
= (7 * 5) + 27 \ (mod \ 9)
\\
= 35 + 27 \ (mod \ 9)
\\
= (35 \ mod \ 9) + 27 \ (mod \ 9)
\\
= 8 + 0 \ (mod \ 9)
\\
= 8 \ (mod \ 9)
$$
