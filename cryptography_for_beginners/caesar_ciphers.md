---
title: Caesar Ciphers
description: Basic introduction to ciphers.
---


[//]: # (content)
## Elementary school encryption

To understand how encryption works, let's start with a basic example.

When I was in elementary school, I would pass notes to my crush. To avoid the teacher from understanding our messages, we would write the letters backwards. Unfortunately, this method of encryption was not cryptographically secure, but it was on the right track.

Goal: Communicate with each other, while preventing any outside observers from knowing what we were saying.

[//]: # (content)
## Caesar ciphers

Let's improve on my encryption protocol.

Instead of writing the letters backwards, let's *change* the message itself.

If we change the message, we need a way for our recipient to change it back to the original message.

Let's create a *key*:

a -> b, b -> c, c -> d, and so on...

[//]: # (question)
Using the key above, what would the letter k map to?

[//]: # (choice)
j

[//]: # (choice correct)
l

[//]: # (choice)
m

[//]: # (choice)
b

[//]: # (question)
Using the key above, let's encrypt the message: "hello world". What do we get?

[//]: # (choice)
bello borld

[//]: # (choice)
idmmn vnqkc

[//]: # (choice)
ifnnp xrqme

[//]: # (choice correct)
ifmmp xpsme

[//]: # (content)
## Our protocol

Assuming both us and the recipient have the same key, then we can effectively communicate.

I have a message: "hello world".

I encrypt the message with the key:
h -> i
e -> f
l -> m
o -> p
w -> x
r -> s
d -> e
-> "ifmmp xpsme"

My recipient decrypts the message with the key: "hello world"

Boom!

[//]: # (content)
## Variations of caesar ciphers

So far we've only seen a caesar cipher where we shift the letters over by one. But we could shift them by any number.

Say our *shift count* is 3. Then our key is a -> d, b -> e, c -> f, ...

[//]: # (question)
Decrypt the following message given a shift count of 4: "tieryx".   Alphabet for reference: abcdefghijklmnopqrstuvwxyz

[//]: # (choice)
peanut

[//]: # (choice)
purple

[//]: # (choice)
peachy

[//]: # (choice correct)
pearls

[//]: # (question)
What does "a" map to if we encrypt it with a shift count of 24?

[//]: # (choice)
c

[//]: # (choice correct)
y

[//]: # (choice)
z

[//]: # (choice)
u

[//]: # (question)
What is the total number of different shift counts we could have that would result in unique keys? (note: shift count 0 counts as a unique key)

[//]: # (choice)
24

[//]: # (choice)
25

[//]: # (choice correct)
26

[//]: # (choice)
27

[//]: # (choice)
23

[//]: # (content)
## Attacking caesar ciphers

Given there's only 26 unique keys, if an attacker knows someone is using a caesar cipher, they could simply guess every possible shift count, and find whichever one decrypts to a plausible message.

This might be enough manual work to prevent your elementary school teacher from finding out your message.

But for anyone willing to use a computer, they could compute every possible decrypted message instantly, for a extremely long messages!

In future lessons, we'll continue to improve our encryption protocol until it gets close to what's used today.
