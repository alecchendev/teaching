---
title: Bases
description: How to convert numbers between bases.
---


[//]: # (content)
## Introduction

Information can be *encoded* in many different ways. Computers process information in sequences of ones and zeroes called *binary*. Often cryptographic operations will express raw data in *hexadecimal* or hex for short.

We'll learn more about these specific encodings in future lessons, but to understand those, we must first understand what *bases* are.

In this lesson we'll learn what a number's base is, and how to convert between bases.

[//]: # (content)
## Numbers

Typically when we encounter numbers on a day-to-day basis, they are *decimal* numbers, i.e. they are written in *base 10*. Keep in mind, it can be sort of unintuitive to understand what this means because it's so normal.

Any number can be expressed in any *base*. The base just expresses at what number we add a new digit.

In base 10, we count single digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, and then boom, we need to add another digit at 10!

What about bases that are not 10? Let's see some examples.

[//]: # (content)
## Base 5

In base 5, we have 5 digits (0, 1, 2, 3, 4) before we add a new digit. Here's how we would express each number from 0 to 10 in base 5:

[//]: # (TODO: figure out rendering tables)

```

| Base 10 | Base 5 |
| ------- | ------ |
| 0       | 0      |
| 1       | 1      |
| 2       | 2      |
| 3       | 3      |
| 4       | 4      |
| 5       | 10     |
| 6       | 11     |
| 7       | 12     |
| 8       | 13     |
| 9       | 14     |
| 10      | 20     |
```

As you can see, when we get to 5 in base 10, we add a new digit and reset the old digit in base 5. And when we go from 9 to 10 in base 10, we increment the left digit, going from 14 to 20 in base 5. 

Let's try some conversions:

[//]: # (question)
How do you represent 7 (base 10) in base 5?

[//]: # (choice)
21

[//]: # (choice)
14

[//]: # (choice)
10

[//]: # (choice correct)
12

[//]: # (explanation)
When you count in base 5, when you reach 5 on any digit, you reset to 0 and add to the next digit over.

Let's count all the way to 17 (base 10) in both bases:

```
| Base 10 | Base 5 |
| ------- | ------ |
| 0       | 0      |
| 1       | 1      |
| 2       | 2      |
| 3       | 3      |
| 4       | 4      |
| 5       | 10     |
| 6       | 11     |
| 7       | 12     |
```

[//]: # (question)
How do you represent 17 (base 10) in base 5?

[//]: # (choice correct)
32

[//]: # (choice)
21

[//]: # (choice)
43

[//]: # (choice)
19

[//]: # (explanation)
When you count in base 5, when you reach 5 on any digit, you reset to 0 and add to the next digit over.

Let's count all the way to 17 (base 10) in both bases:

```
| Base 10 | Base 5 |
| ------- | ------ |
| 0       | 0      |
| 1       | 1      |
| 2       | 2      |
| 3       | 3      |
| 4       | 4      |
| 5       | 10     |
| 6       | 11     |
| 7       | 12     |
| 8       | 13     |
| 9       | 14     |
| 10      | 20     |
| 11      | 21     |
| 12      | 22     |
| 13      | 23     |
| 14      | 24     |
| 15      | 30     |
| 16      | 31     |
| 17      | 32     |
```

[//]: # (content)
## Review: Exponents and Powers

As a quick review, when we write something in the form $x^n$ this translates to $x$ multiplied by itself $n$ times. For example $3^4$ translates to $3 * 3 * 3 * 3 = 243$. We refer to this as "three to the power of four."

Here $x$ is called the *base*, and $n$ is the *exponent*.

If you increase the exponent, you simply multiply again by the base. So to go from $3^4$ to $3^5$, we multiply by $3$, i.e. $3^5 = 3^4 * 3 = 243 * 3 = 729$.

To go backwards, we divide. $3^3 = 3^4 / 3 = 243 / 3 = 81$.

From this, notice that any number to the zeroth power is $1$. E.g. $3^0 = 3^1 / 3 = 1$

Soon we will look at a more generic way to understand bases. But first it's important we remember how powers/exponents work.

[//]: # (question)
Calculate 5^3:

[//]: # (choice correct)
125

[//]: # (choice)
25

[//]: # (choice)
15

[//]: # (choice)
64

[//]: # (explanation)
Explanation:

For any exponent $x^n$ we can calculate the result by multiply $x$ by itself $n$ times.

$$
5 ^ 3 = 5 * 5 * 5 = 125
$$

[//]: # (question)
Calculate 8^0:

[//]: # (choice)
Undefined

[//]: # (choice)
1/8

[//]: # (choice correct)
1

[//]: # (choice)
0

[//]: # (choice)
8

[//]: # (explanation)
Any number raised to the zeroth power is 1.

[//]: # (content)
## Another definition of base

Our initial definition of a base is the number at which we add a new digit. But another way to define the base is to say that each digit expresses the next *power* of the base.

Let's see an example:

The number 3 (base 10) expressed in base 5 is 3.

From here on out, we'll represent a number and its base with subscript, e.g. 3 (base 10) = $3_{10}$. And you can assume any number without a base is in base 10.

3 (base 5) = $3_5 = 5^0 * 3 = 3_{10}$

The number $7_{10}$ is expressed in base 5 as $12_5$.

$12_5 = 5^1 * 1 + 5^0 * 2 = 5 + 2 = 7_{10}$

$21_{10}$ can be expressed as $41_5$.

$41_5 = 5^1 * 4 + 5^0 * 1 = 20 + 1 = 21_{10}$

$82_{10}$ can be expressed as $312_5$.

$312_5 =$

$5^2 * 3 + 5^1 * 1 + 5^0 * 2 =$

$25 * 3 + 5 * 1 + 1 * 2 = 75 + 5 + 2 =$

$82_{10}$

[//]: # (question)
What is the base 10 equivalent of 241 base 5?

[//]: # (choice correct)
71

[//]: # (choice)
86

[//]: # (choice)
76

[//]: # (choice)
81

[//]: # (explanation)
To convert from base 5 to base 10, we multiply each digit by the respective power of 5, and sum them together:

$$
241_5 = 2 * (5 ^ 2) + 4 * (5 ^ 1) + 1 * (5 ^ 0)
\\ = 2 * 25 + 4 * 5 + 1 * 1
\\ = 71_{10}
$$

[//]: # (question)
What is the base 10 equivalent of 2013 base 5?

[//]: # (choice)
298

[//]: # (choice)
343

[//]: # (choice)
157

[//]: # (choice correct)
258

[//]: # (explanation)
To convert from base 5 to base 10, we multiply each digit by the respective power of 5, and sum them together:

$$
2013_5 = 2 * (5 ^ 3) + 0 * (5 ^ 2) + 1 * (5 ^ 1) + 3 * (5 ^ 0)
\\ = 2 * 125 + 0 * 25 + 1 * 5 + 3 * 1
\\ = 258_{10}
$$

[//]: # (content)
We can apply what we understand about bases to convert to and from any base:

```
| Base 10 | Base 1 | Base 2 | Base 3 | Base 5 |
| ------- | ------ | ------ | ------ | ------ |
| 0       | 0      | 0      | 0      | 0      |
| 1       | 00     | 1      | 1      | 1      |
| 2       | 000    | 10     | 2      | 2      |
| 3       | 0000   | 11     | 10     | 3      |
| 4       |        | 100    | 11     | 4      |
| 5       |        | 101    | 12     | 10     |
| 6       |        | 110    | 20     | 11     |
| 7       |        | 111    | 21     | 12     |
| 8       |        | 1000   | 22     | 13     |
| 9       |        | 1001   | 100    | 14     |
| 10      |        | 1010   | 101    | 20     |
```


[//]: # (question)
How would you represent 64 (base 10) in base 3?

[//]: # (choice correct)
2101

[//]: # (choice)
148

[//]: # (choice)
3104

[//]: # (choice)
2200

[//]: # (explanation)
This one is a bit challenging. For converting from base 10 to another base, we need to do the following:

- Find the largest power that fits into the number
- Divide the current number. The result is the digit, and the remainder is the new "current number."
- Repeat with smaller powers.

For this example, we start with 64.

Find the largest power of 3 smaller than 64: $3^1=3,3^2=9,3^3=27,3^4=81$. 81 is too big, so 27 is our number.

27 fits into 64 twice, i.e. $64 / 27 = 2$ with a remainder 10. So our final result is 2...something.

The next power of 3 is 9.

9 fits into 10 once, i.e. $10/9=1$ with a remainder 1. So our final result is 21...something.

The next power of 3 is 3.

3 doesn't fit into 1 at all, so our digit here is 0, and our final result is 210...something.

Our last power is $3^0=1$. It fits into 1 once. So our final result is 2101!

[//]: # (question)
How would you represent 46 (base 7) in base 10?

[//]: # (choice)
17

[//]: # (choice correct)
34

[//]: # (choice)
21

[//]: # (choice)
28

[//]: # (explanation)
To convert from base 7 to base 10, we multiply each digit by the respective power of 7, and sum them together:

$$
46_7 = 4 * (7 ^ 1) + 6 * (7 ^ 0)
\\ = 4 * 7 + 6 * 1
\\ = 34_{10}
$$
