Simhash
===========

This is a Python implementation of [Simhash](http://www.wwwconference.org/www2007/papers/paper215.pdf).

## Getting Started

<http://leons.im/posts/a-python-implementation-of-simhash-algorithm/>

## Build Status

[![Build Status](https://travis-ci.org/leonsim/simhash.png?branch=master)](https://travis-ci.org/leonsim/simhash)

#
Following added by [Ela2Zofia](www.github.com/Ela2Zofia)

## Requirement
[jieba](https://github.com/fxsjy/jieba)
install with
```bash
pip install jieba
```


## time_test.py

This is the function which tests the execution time of the algorithm on texts of different lengths.

## sim_detect.py

It returns a list of number that indicates the indecies of near duplicates, and write them to a file called "result"
