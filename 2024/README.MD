Advent of Code 2024.

Starting in Python to learn about the language.

I'll try and document my main learnings here as the days go by.

# Day 1

`zip` is very nice, exactly the kind of nice-to-have I expect from Python. It accepts any number of `iterables`, and returns a list of tuples with an element from each in order.

When dealing with dictionaries, found two different ways of setting default values if a key doesn't exist. First, using `.get(key, default)`. Didn't like it here because it made this particular code too verbose without any need. Looking more, I found the `defaultdict` in `collections` which allows to specify defaults on dictionary creation, which I liked much more for this particular case.

# Day 2

Day 2 causing unexpected problems already!  Ugly code this time, might try to refactor it later a bit. 

Regarding what I've learned about Python...

A better understanding of its iterators, and in particular learnt about `enumerate`, which I'm sure will come handy more than once on this Advent of Code.

I've now created a simple template for each day to save some time on the initial boiler plate.

# Day 3

Regular expression day. Raw string literals, `split`, `search` and `findall` functions around regular expressions. Also looked into lambda definition in Python.

# Day 4

A bit to learn today around arrays. `strings` are `arrays`, which makes this easy. Also some more lambda, and some more practice with `in`.  

# Day 5

First day of graphs with Python. I messed this one quite a bit in part 1, not realising the actual ask didn't care about transitive relationships between pages. Just got lucky my way of solving it actually worked. By part 2, I realised, which made the solution much simpler. I am not going to refactor this, rather leave the overcomplicated solution.

Regarding learnings... new for me have been the use of `list()` `dict()` `set()` `intersection()` and `sorted()`. All pretty basic stuff, but still useful. I am however feeling my code is very much not Pythonic. Not sure if I'll manage to improve that during this advent of code. 

# Day 6

Quite bad and ugly code today, with lot of bad code duplication. Not proud of this one.

Specific new things I've used this day: `match` expression.

# Day 7

Quite a simple one today, hasn't given me the chance of using anything stricitly new to me in Python.

# Day 8

Another surprisingly straightforward day. Has let me take an initial look into classes in Python, defining operator behaviours and making them hashable. Also, how to use `__name__` to know if a file is the main file being executed or if it is imported as a module.

# Day 9 

Worst day so far, took me very long to correct my totally wrong approach to part B. 

In Python learnings, mostly more dealing with classes.

# Day 10

Solution for part B required just a couple of small changes from the solution to part A, which is always nice. 

In learnings, I've used `list comprehension` and `list generators`.

# Day 11

Cache day. Not much more to say.

# Day 12
Nothing really new today

# Day 13
Not much today either. I did look in a bit more detail into numpy, but didn't use anything new in the end

# Day 14

Weird part 2 today. I first had to do some manual examination of resulting grids before knowing what to look for.

# Day 15

One learning to highlight: if a function returns several values on a tuple, you can't just get the first one without explicitly getting the others, or it will actually contain the tuple itself. Quite obvious in retrospect.

# Day 16

Part 1 has taken me forever today due to some silly mistakes due to me writing ugly code. I really should know better.

Small learning today regarding how to measure elapsed time.

# Day 17

Hard to approach second star today! Learnings: bitwise operations, that I hadn't really used before in Python.

# Day 18

Always one or two Dijkstra problems every year. For part two I am almost certain there is a smarter way of doing it, looking at the current minimal path and checking if a new byte lies in that path or not. If it does, then you would just need to recalculate a path from the previous node to the next one. Instead of that, given the limited number of bytes, I've just gone with a kind of force brute approach, using a binary search in the problem space. Worked well enough.

Not much new in question of Python lessons here. I think I am now being better at using list comprehension and generators.

# Day 19

Well, that was a day of a couple of great ideas for the wrong question. Those wrong approaches at least let me learn more about regular expressions on Python.

# Day 20

Not much new learnt today. My code still doesn't feel pythonic to me.

# Day 21

I chose a bad day to try and force me to write more pythonic code. Part 1 wasn't too bad, part 2 took me many hours of basically rewriting to be able to optimise it properly.

Learnings: `functools.cache` to memoize out of the box instead of creating my own caches. That is handy! Lot of extra learning around lists, generators, iterators.

# Day 22

Not too hard today, even though I clearly haven't found the correct way of doing it. Just a bit of brute force is enough though. Have been using what I learned yesterday, trying to still write more pythonic code. And I have discovered 'namedtuple' and 'NamedTuple' which are very nice indeed.

# Day 23

More practice with sets and list comprehension mostly. Also learned about 'frozenset'. Code is still ugly though.

# Day 24

That was painful! Not ready to push my code for part 2 just yet. In the end I've done part of the solution manually, helped by the code to find where the problems were, but I want to finish it to actually produce the bits I've done manually.

# Day 25

Happy Christmas! QUick one, with a quick and dirty solution. I'm also pushing whatever I have for part 2 of day 24, even though it is still unfinished and requires manual work.