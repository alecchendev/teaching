---
title: Hex
description: Kinda like binary, but base 16 this time!
---

[//]: # (content)
## Introduction

In previous modules, we've seen how information is encoded into binary. Oftentimes
we may want to print some arbirtrary data as text, but displaying every single
one and zero is too verbose. Most often, if you have a bunch of bytes, you'll
see it represented in *hexadecimal*, or *hex* for short.

Similar to how binary is just base 2, hex is base 16. So instead of each digit
representing a power of 2, each digit represents a power of 16. Let's see
examples of the first 20 numbers in hex:

| Base 10 | Base 16 |
|---------|---------|
| 0       | 0       |
| 1       | 1       |
| 2       | 2       |
| 3       | 3       |
| 4       | 4       |
| 5       | 5       |
| 6       | 6       |
| 7       | 7       |
| 8       | 8       |
| 9       | 9       |
| 10      | a       |
| 11      | b       |
| 12      | c       |
| 13      | d       |
| 14      | e       |
| 15      | f       |
| 16      | 10      |
| 17      | 11      |
| 18      | 12      |
| 19      | 13      |
| 20      | 14      |

Notice how when we reach $10_{10}$, we start using letters to represent numbers,
i.e. $10_{10}=a_{16}$.

[//]: # (content)
## Example: converting from hex to decimal

How would we convert $2c_{16}$ to base 10?

Since each digit corresponds to a power of 16, we multiply each digit by its
power, and sum up the result.

```
2c -> ???

2    c
|    |
16^1 16^0

2 * (16^1) + 12 * (16^0) =
2 * 16     + 12 * 1     =
32 + 12 =
44
```

Final answer: $2c_{16} = 44_{10}$

[//]: # (question)
What is $7a_{16}$ in decimal (base 10)?

[//]: # (choice correct)
122

[//]: # (choice)
9

[//]: # (choice)
59

[//]: # (choice)
50

[//]: # (question)
What is $35_{16}$ in decimal (base 10)?

[//]: # (choice)
77

[//]: # (choice)
68

[//]: # (choice correct)
53

[//]: # (choice)
86

[//]: # (content)
## Example: converting from decimal to hex

How would we convert $62_{10}$ to hex?

Similar to how we've converted decimal to other bases like binary,
we find the biggest power of our base (here, 16) that fits into our number,
and then find the remainder. We then repeat this process with smaller powers
until our remainder is 0.

```
62
?    ?
|    |
16^1 16^0
|    |
16    1
```

Let's scan through the powers of 16: 1, 16, 256. 256 is too big, so we'll
use 16.

How many times does 16 fit into 62? $62 \div 16 = 3 \ \text{remainder} \ 14$

So we update our number:

```
    14
3   ?
|   |
16  1
```

Now we have 14, and our power is 1. $14/1 = 14 \ \text{remainder} \ 0$

In hex, we represent numbers 10-15 as a-f, so our digit for this power is "e".

```
3   e
|   |
16  1
```

Final answer: $62_{10} = 3e_{16}$

[//]: # (question)
What is $31_{10}$ in hex (base 16)?

[//]: # (choice)
12

[//]: # (choice correct)
1f

[//]: # (choice)
13

[//]: # (choice)
4

[//]: # (question)
What is $138_{10}$ in hex (base 16)?

[//]: # (choice)
8f

[//]: # (choice)
7d

[//]: # (choice correct)
8a

[//]: # (choice)
43

[//]: # (content)
## Colors

You may have seen colors represented as hex before. For example, the color below
can be represented as #32a852.

![Color](https://alecchen.dev/teaching/cryptography_for_beginners/images/green.png)

This representation is just the hex values for the red, green, and blue components
of the color, i.e. the red value is $32_{16}$, the green value is $a8_{16}$, and
the blue value is $52_{16}$. And so their decimal/base 10 values are 50, 168, and
82 respectively.

[//]: # (question)
What is the decimal value of blue component of the color #5324bf?

[//]: # (choice)
75

[//]: # (choice correct)
191

[//]: # (choice)
208

[//]: # (choice)
70

[//]: # (content)
## Binary/bytes and hex

Most often when using hex in this course, it will be used to display
some bytes in a more compact form. Binary and hex have a nice relationship
where there is a fairly straight forward way to convert between the two.

For any 4 binary digits, it directly translates to a single hex digit. For
example, $1001_2 = 9_{16}$. Notice that 4 bits can represent 0-15,
just like a single hex digit.

And say we have a byte, $11011001_2$, we can just translate it to hex
4 bits at a time:

```
1101 = 13 = d
1001 = 9

11011001 = d9
```

Similar to how 4 bits always translate to a single hex digit, a
byte (8 bits) always translates to 2 hex digits.

[//]: # (question)
What is $0110011101100011_2$ in hex (base 16)?

[//]: # (choice)
487a

[//]: # (choice correct)
6763

[//]: # (choice)
7754

[//]: # (choice)
850c

[//]: # (question)
What is $ba3e_{16}$ in binary (base 2)?

[//]: # (choice)
0110000010111101

[//]: # (choice)
0001000100000001

[//]: # (choice correct)
1011101000111110

[//]: # (choice)
1001111011010011

[//]: # (question)
How many bytes are in the hex string $f3a2b1beef_{16}$?

[//]: # (choice correct)
5

[//]: # (choice)
3

[//]: # (choice)
8

[//]: # (choice)
4
