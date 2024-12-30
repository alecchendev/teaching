---
title: XOR
description: Introduction to the XOR operation.
---

[//]: # (content)
## Introduction

XOR (pronounced "EX-or") is an binary operation that takes two bits as input, and returns one bit as output.
It's used all over the place in cryptography.

Here's what its inputs and outputs look like:

```
| x | y | x ⊕ y |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |
```

(The symbol ⊕ is the XOR operator.)

An intuitive way to think about XOR is that it returns 1 if the inputs are different, and 0 if they're the same.

Let's do some simple examples.

[//]: # (question)
What is $1 \oplus 0$?

[//]: # (choice)
0

[//]: # (choice correct)
1

[//]: # (explanation)
Since the inputs are different, the output is 1.

[//]: # (question)
What is $0 \oplus 0$?

[//]: # (choice correct)
0

[//]: # (choice)
1

[//]: # (explanation)
Since the inputs are the same, the output is 0.

[//]: # (content)
## XOR with sequences of bits

In practice, we won't just be XORing single bits. We'll be XORing sequences of bits.

When you XOR a sequence of bits, you just XOR each pair of bits in the sequence.

For example, let's evaluate $100$ and $110$.

```
100 ⊕ 110

1 ⊕ 1 = 0
0 ⊕ 1 = 1
0 ⊕ 0 = 0

= 010
```

[//]: # (question)
What is $1001110 \oplus 1101001$?

[//]: # (choice)
1100111

[//]: # (choice correct)
0100111

[//]: # (choice)
0101110

[//]: # (choice)
1100110

[//]: # (explanation)
To XOR a sequence of bits, we line up the two sequences and XOR each bit.

```
1001110
1101001

1 ⊕ 1 = 0
0 ⊕ 1 = 1
0 ⊕ 0 = 0
1 ⊕ 1 = 0
1 ⊕ 0 = 1
1 ⊕ 0 = 1
0 ⊕ 1 = 1

= 0100111
```

[//]: # (question)
What is $10101011 \oplus 01010101$?

[//]: # (choice)
11111111

[//]: # (choice)
00000000

[//]: # (choice)
00000001

[//]: # (choice correct)
11111110

[//]: # (explanation)
To XOR a sequence of bits, we line up the two sequences and XOR each bit.

```
10101011
01010101

1 ⊕ 0 = 1
0 ⊕ 1 = 1
1 ⊕ 0 = 1
0 ⊕ 1 = 1
1 ⊕ 0 = 1
0 ⊕ 1 = 1
1 ⊕ 0 = 1
1 ⊕ 1 = 0

= 11111110
```

[//]: # (question)
If you XOR a number with itself ($x \oplus x$), what do you get?

[//]: # (choice correct)
0

[//]: # (choice)
The number itself

[//]: # (choice)
All ones

[//]: # (explanation)
Since XOR always returns 0 when the inputs are the same, when we
XOR a number with itself, all bits are the same, so all the output's
bits are 0. A sequence of all zeroes is just 0!

For example, take a random number, say $1011$:

```
1011 ⊕ 1011

1 ⊕ 1 = 0
0 ⊕ 0 = 0
1 ⊕ 1 = 0
1 ⊕ 1 = 0

= 0000
```
