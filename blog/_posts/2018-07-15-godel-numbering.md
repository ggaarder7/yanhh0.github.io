---
title: Gödel numbering
source: https://en.wikipedia.org/wiki/G%C3%B6del_numbering
---

In mathematical logic, a Gödel numbering is a function that assigns to
each symbol and well-formed formula of some formal language a unique
natural number, called its Gödel number. The concept was used by Kurt
Gödel for the proof of his incompleteness theorems. (Gödel 1931)

A Gödel numbering can be interpreted as an encoding in which a number
is assigned to each symbol of a mathematical notation, after which a
sequence of natural numbers can then represent a sequence of
symbols. These sequences of natural numbers can again be represented
by single natural numbers, facilitating their manipulation in formal
theories of arithmetic.

Since the publishing of Gödel's paper in 1931, the term "Gödel
numbering" or "Gödel code" has been used to refer to more general
assignments of natural numbers to mathematical objects.

## Simplified overview

Gödel noted that statements within a system can be represented by
natural numbers. The significance of this was that properties of
statements - such as their truth and falsehood - would be equivalent
to determining whether their Gödel numbers had certain properties. The
numbers involved might be very long indeed (in terms of number of
digits), but this is not a barrier; all that matters is that we can
show such numbers can be constructed.

In simple terms, we devise a method by which every formula or
statement that can be formulated in our system gets a unique number,
in such a way that we can mechanically convert back and forth between
formulas and Gödel numbers. Clearly there are many ways this can be
done. Given any statement, the number it is converted to is known as
its Gödel number. A simple example is the way in which English is
stored as a sequence of numbers in computers using ASCII or Unicode:

- The word HELLO is represented by 72-69-76-76-79 using decimal ASCII.
- The logical statement x=y => y=x is represented by
  120-61-121-32-61-62-32-121-61-120 using decimal ASCII.

## Gödel's encoding

Gödel used a system based on prime factorization. He first assigned a
unique natural number to each basic symbol in the formal language of
arithmetic with which he was dealing. 

To encode an entire formula, which is a sequence of symbols, Gödel
used the following system. Given a sequence $$(x_1,x_2,x_3,...,x_n)$$ of
positive integers, the Gödel encoding of the sequence is the product
of the first n primes raised to their corresponding values in the
sequence:

$$\mathrm {enc} (x_{1},x_{2},x_{3},\dots ,x_{n})=2^{x_{1}}\cdot
3^{x_{2}}\cdot 5^{x_{3}}\cdots p_{n}^{x_{n}}$$
