---
title: Binary
description: How does the human readable stuff we see convert to ones and zeroes that computers can process?
---


[//]: # (content)
## Introduction

Information can be *encoded* in many different ways. At the lowest level, computers process information encoded as binary, i.e. a sequence of zeroes and ones.

For example:
- The number 20 can be written *in binary* as 10100.
- The message "hello" can be written *in binary* as 110100001100101011011000110110001101111.

Each digit in a string of ones and zeroes is called a *bit*.

But how does that work?

In this module, we'll learn how to convert information between binary and different encodings.

This will be key to being able to understand what's really going on behind the scenes when a computer is doing pretty much anything.

[//]: # (content)
## Converting binary to numbers

In a previous module, we learned about bases. We saw how we can convert between decimal (base 10) numbers, and other bases.

Binary is simply base 2! So if you know how to convert numbers from base 2, you practically already know how to read binary numbers.

Here's a reminder of how the natural numbers map to binary:

```
| Base 10 | Base 2 |
| ------- | ------ |
| 0       | 0      |
| 1       | 1      |
| 2       | 10     |
| 3       | 11     |
| 4       | 100    |
| 5       | 101    |
| 6       | 110    |
| 7       | 111    |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |
```

[//]: # (content)
## Example: converting binary to decimal numbers

How would we convert the number $1011_2$ to base 10?

Each digit in binary corresponds to a power of 2. We need to go through each digit, multiply it by it's associated power of 2, and sum up the result:

```
1101 -> ???

1   1   0   1
|   |   |   |
2^3 2^2 2^1 2^0

1 * (2^3) + 1 * (2^2) + 0 * (2^1) + 1 * (2^0) =
1 * 8     + 1 * 4     + 0 * 2     + 1 * 1     =
8 + 4 + 0 + 1 =
13
```

Final answer: $1011_2 = 13_{10}$


[//]: # (question)
How would we convert 10101 (base 2) to base 10?

[//]: # (choice)
20

[//]: # (choice)
22

[//]: # (choice correct)
21

[//]: # (choice)
24

[//]: # (question)
What is 11110 (base 2) in decimal (base 10)?

[//]: # (choice correct)
30

[//]: # (choice)
15

[//]: # (choice)
35

[//]: # (choice)
29

[//]: # (content)
## Converting numbers to binary

Converting from a decimal number to binary is slightly trickier, but still follows a simple recipe. Similar to converting from decimal to other bases, the steps are roughly:
- Find the largest power of 2 that fits into the number.
- Divide the number by that power, and record the quotient as the digit.
- Take the remainder, and the next smaller power of two, and do the same thing, until you get to the last digit.

Let's see an example to help illustrate.


[//]: # (content)
## Example: converting numbers to binary

Let's try to convert the base 10 number $25_{10}$ to binary.

What is the largest power of 2 that fits into 25?

Let's just scan through each power of 2: 1, 2, 4, 8, 16, 32. 16 is what we want since it's the largest that's less than or equal to our number 25.

From here, given 16 is our starting power, we know that because binary numbers' digits correspond to powers of 2, our number will look something like this:

```
25
?   ?   ?   ?   ?
|   |   |   |   |
16  8   4   2   1
```

Now, let's divide: $25 / 16 = 1 \ \text{remainder} \ 9$

Let's update our number:

```
    9
1   ?   ?   ?   ?
|   |   |   |   |
16  8   4   2   1
```

Now let's divide with the next power of 2: $9 / 8 = 1 \ \text{remainder} \ 1$

Update our number:

```
        1
1   1   ?   ?   ?
|   |   |   |   |
16  8   4   2   1
```

Divide with the next power of 2: $1 / 4 = 0 \ \text{remainder} \ 1$

```
            1
1   1   0   ?   ?
|   |   |   |   |
16  8   4   2   1
```

$1 / 2 = 0 \ \text{remainder} \ 1$

```
                1
1   1   0   0   ?
|   |   |   |   |
16  8   4   2   1
```

$1 / 1 = 1 \ \text{remainder} \ 0$

```
1   1   0   0   1
|   |   |   |   |
16  8   4   2   1
```

And we're done! $25_{10} = 11001_2$


[//]: # (question)
What is 35 (base 10) in binary (base 2)?

[//]: # (choice)
11101

[//]: # (choice)
11110

[//]: # (choice)
10110

[//]: # (choice correct)
100011

[//]: # (question)
What is 29 (base 10) in binary (base 2)?

[//]: # (choice)
1111

[//]: # (choice correct)
11101

[//]: # (choice)
10110

[//]: # (choice)
1001

[//]: # (content)
## Bytes

Computers don't typically process data in individual bits. Instead, they chunk pieces together in a variety of different structures. One fundamental chunk is called a *byte*, and it just means 8 bits together.

So a byte is really just a number from 0 to 255 (inclusive), since that's how many numbers can be represented in 8 bits (if you think about it, $00000000_2=0_{10}$ and $11111111_2=255_{10}$).

Computers convert between text and bytes using a simple fixed table, an ASCII table, which looks like this:

![](https://www.asciitable.com/asciifull.gif)

For the purposes of this module, we'll want to pay attention to the mapping between the "Dec" (decimal number) and "Chr" (character).

This table shows all the most commonly used ASCII characters, but there are more, all the way up to 255.

[//]: # (content)
## Example: converting between numbers and characters

If we want to convert a character, say "D" to a number, we simply look for the "D" in the character column, and see what number it corresponds to. In this case it's 68.

If we want to convert from a number to a character, we do the reverse, i.e. look for our number, say 114, in the decimal number column, and see what character is corresponds to. In this case it's "r".

[//]: # (question)
What number does the character "j" correspond to in ASCII?

[//]: # (choice)
100

[//]: # (choice)
99

[//]: # (choice correct)
106

[//]: # (choice)
35

[//]: # (question)
What character does the number 61 correspond to in ASCII?

[//]: # (choice)
A

[//]: # (choice correct)
=

[//]: # (choice)
3

[//]: # (choice)
;

[//]: # (content)
## Converting between strings and bytes

When you have words, sentences, lines of code, or any sort of text, it's represented as a sequence of bytes, called a *string*.

Converting a string is as simple as repeatedly converting each character/byte.

For example, the word "hello" converts to \[104, 101, 108, 108, 111\]. And \[119, 111, 114, 108, 100\] converts to "world".

Here's the table again to save you some scrolling:

![](https://www.asciitable.com/asciifull.gif)


[//]: # (question)
What would the sequence of bytes be for "Hi Bob"?

[//]: # (choice correct)
[72, 105, 32, 66, 111, 98]

[//]: # (choice)
[73, 105, 32, 106, 111, 66]

[//]: # (choice)
[98, 121, 32, 114, 111, 98]

[//]: # (choice)
[108, 121, 32, 107, 110, 111, 98]

[//]: # (question)
What string represents the sequence of bytes [66, 65, 78, 65, 78, 65]?

[//]: # (choice)
BOARD

[//]: # (choice correct)
BANANA

[//]: # (choice)
BASKET

[//]: # (choice)
BOWLED

[//]: # (content)
## Converting between text and binary

If we piece everything together, we can understand how to encode data as either human-readable text, or computer-readable binary.

Let's take the example from the beginning: "hello". To convert this to binary, we convert each character to it's respective number (byte) in ASCII, i.e. \[104, 101, 108, 108, 111\]. Then convert each byte to binary, i.e. \[01101000, 01100101, 01101100, 01101100, 01101111\]. String them together to get $0110100001100101011011000110110001101111$.

```
   h        e        l        l        o    
01101000 01100101 01101100 01101100 01101111
```

Note: we "pad" the left side of some of these numbers with extra zeroes to align them to be 8-bits wide.

To go from binary to a string, you do the reverse. Chop the sequence of ones and zeroes into 8-bit chunks, and convert numbers, then map it in ASCII.

For the binary sequence $01100101011011100110001101110010011110010111000001110100$ can be read a string like so:
- Chop it into bytes: 01100101 01101110 01100011 01110010 01111001 01110000 01110100
- Convert each byte to its decimal number represenation:
```
01100101 01101110 01100011 01110010 01111001 01110000 01110100
  101       110      99       114     121      112       116
```
- Convert each byte to a character with the ascii table:
```
101, 110, 99, 114, 121, 112, 116
"e", "n", "c","r", "y", "p", "t"
```
- Tada! The final result is the word "encrypt".


[//]: # (question)
Convert the string "pen" to binary:

[//]: # (choice)
011000100110010101101110

[//]: # (choice correct)
011010000110010101111001

[//]: # (choice)
011100100110000101100100

[//]: # (choice)
011100000110010101101110

[//]: # (question)
Convert the binary sequence 011011000110111101100111 to text:

[//]: # (choice correct)
log

[//]: # (choice)
dig

[//]: # (choice)
song

[//]: # (choice)
fig
