---
title: Randomness vs. Pseudorandomness
description: Two different processes for generating random numbers.
---

[//]: # (
    TODO: add examples for pseudorandomness, i.e. give a mod example
    - also make a problem to say a linear equation is not random
    - specify domain and range for problems
)

[//]: # (content)
## Introduction

Every human is familiar with randomness in some form or another. Part of what
makes life so absurd is the randomness of it all.

In cryptography, randomness serves a very important role. Often secure communication
or authentication will rely on keeping some random data secret. If that random
data is not sufficiently random, then it's probably not sufficiently secret.

In this lesson, we'll see the main two kinds of randomness, and in future lessons
we'll see how they're used in cryptographic applications.

[//]: # (content)
## True randomness

True randomness is basically what is sounds like. Something random happens in the world.

But what does this mean in math/computer science/cryptography?

Something is random, when all possible outcomes are equally likely. Or in other words,
the probability distribution (the probabilities of any outcome happening) is *uniform*.

For example, a coin toss is random. The odds of it landing on heads is the same
as the odds of it landing on tails.

Another example, rolling a dice is random. The odds of it landing on any one side
is the same for all sides.

[//]: # (question)
If I pick a random number from 1-10, what are the odds that I pick 4?

[//]: # (choice)
$\frac{1}{4}$

[//]: # (choice correct)
$\frac{1}{10}$

[//]: # (choice)
$\frac{1}{5}$

[//]: # (choice)
$\frac{1}{2}$

[//]: # (explanation)
For anything random, the odds of any outcome is the same. In this case,
there are $10$ possible outcomes, so any one outcome has a $\frac{1}{10}$ chance.

[//]: # (question)
Which is an example of something random?

1. The suit of a card picked from a shuffled deck
2. A quarter that lands on heads 60% of the time and tails 40% of the time
3. The color of a cube chosen from a bag of 10 red, 10 green, and 10 blue cubes

[//]: # (choice)
1, 2

[//]: # (choice)
None

[//]: # (choice)
1, 2, 3

[//]: # (choice correct)
1, 3

[//]: # (explanation)
Let's walk through each choice.

Our definition of random is that all outcomes are equally likely.

1. The suit of a card chosen from a deck
    - There are 13 hearts, diamonds, clubs, and spades. A deck of cards has
    52 cards. The odds that a card will have a heart is $13/52 = 1/4$, and the same
    goes for every other suit. Since the odds are all the same, it's random.
2. A quarter that lands on heads 60% of the time and tails 40% of the time
    - The outcome that it lands on heads is different from the outcome
    that it lands on tails, so it's not random.
3. The color of a cube chosen from a bag of 10 red, 10 green, and 10 blue cubes
    - The outcome that the color is red green or blue are all $10/30$, so it's random.

So the final answer is 1 and 3.

[//]: # (content)
## Pseudorandomness

Something pseudorandom is something that looks random, but was generated deterministically. This means it was *seeded* with some input, and if you run the same
method on the seed (the input), you will get the same output.

As a really simple example, if we have a function defined as the following:

$$
f(x)=y
\\
0\leq x \leq 3 \quad 0 \leq y \leq 3
\\
f(0)=3
\\
f(1)=1
\\
f(2)=0
\\
f(3)=2
$$

Looking at the outputs from the inputs, they look random. However you can
reproduce the output if you know the input. This is not true for something
like flipping a coin because, well, we can't time travel.

[//]: # (question)
Is the following modulo function pseudorandom?

$$
f(x)=x*7 + 3 \ (mod \ 11)
$$

[//]: # (choice)
No

[//]: # (choice correct)
Yes

[//]: # (explanation)
Take a look at the outputs for this function:

| x | f(x) |
|---|------|
| 0 | 3    |
| 1 | 10   |
| 2 | 6    |
| 3 | 2    |
| 4 | 9    |
| 5 | 5    |
| 6 | 1    |
| 7 | 8    |
| 8 | 4    |
| 9 | 0    |
| 10| 7    |

Our main two qualities for something to be pseudorandom are:
1. The output looks random to an outside observer
2. The output can be reproduced if you know the input

Each output is equally likely and there is no clear pattern. And
if you know the input, you will always reproduce the same output.

[//]: # (question)
Is the following incrementing function pseudorandom?

$$
f(x)=x + x_{prev} \ (mod \ 13)
$$

where $x_{prev}$ is the last output of the function, starting at $0$. E.g. here are some outputs:

$$
f(2)=2+0=2
\\
f(3)=3+2=5
\\
f(9)=9+5=14 \ (mod \ 13)=1
\\
f(11)=11+1=12 \ (mod \ 13)=12
\\
f(6)=6+12=18 \ (mod \ 13)=5
$$

[//]: # (choice)
Yes

[//]: # (choice correct)
No

[//]: # (explanation)
The output of this function is...random-ish. But the main problem is that
this function is not deterministic, i.e. the same input doesn't always
return the same output.

$$
f(2)=2+0=2
\\
f(2)=2+2=4
$$

[//]: # (content)
## Keeping secrets

In cryptography, often the security of a system will rely on keeping some random data
secret. Ideally you can always generate enough data in a truly random way,
but often it is more practical/efficient to generate random data
pseudorandomly.

Say you generate some random string of letters/characters as your password.
If you generate it truly randomly, then the best someone could do to crack it is
to brute force guess and check every password. With a password of length 10 made up
of only lowercase letters, there are $26^{10}=141,167,096,000,000$ possible passwords.

However, if you generated it
pseudorandomly, based on a seed that was some number between 0-9999, your password
might be 1000 characters long, but there are only 10,000 possible passwords. With
pseudorandomness, your security relies on the security of the seed.

[//]: # (question)
Alice and Bob both generate numbers between $0 \leq x \leq 99,999,999$. They're trying to protect
their other friend Carol, who is known to be very nosy, and tries to guess
people's secrets. Carol does this all by hand, and so after 10000 guesses, she
gives up.

- Bob takes the day of the year from 0-365 of his dog's birthday, multiplies by 67820186, and takes the result modulo 100000000. Note: Carol does not know Bob's dog's birthday.
- Alice generates her number by rolling a 10-sided dice 8 times and recording each roll as a digit. She then multiplies by 3 and takes the result modulo 100000000. Note: Carol does not know the result of the dice rolls.

Who is safe from Carol if Carol knows their generation methods?

[//]: # (choice)
Neither Alice nor Bob

[//]: # (choice)
Only Bob

[//]: # (choice correct)
Only Alice

[//]: # (choice)
Both Alice and Bob

[//]: # (explanation)
Bob's method is pseudorandom, and could have been safe if he had generated a seed
with more true randomness. Unfortunately, even if Carol doesn't know the day of the year
or Bob's dog's age, she only has to make 365 guesses to crack Bob's secret. His seed is his the day of the year of his dog's birthday, and there are only 365 possibilities, which
is well within the attacker's computational abilities.

Alice's method is still pseudorandom, but her seed is chosen from a large enough space,
with true randomness. Carol would have to make $10^8$ guesses to crack Alice's secret,
but she can only makes 10000 guesses.
