# love-calculator

A program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Hussain Erfani"
name2 = "Katya Hutsul"
T occurs 2 times

R occurs 1 time

U occurs 3 times

E occurs 1 times

Total = 7

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 1 times

Total = 2

Love Score = 72

Print: "Your score is 72."

These functions will help you:
lower() https://www.w3schools.com/python/ref_string_lower.asp
count() https://www.w3schools.com/python/ref_list_count.asp
