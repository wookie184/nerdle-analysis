## Nerdle Analysis

https://nerdlegame.com/

This repository contains some analysis of possible nerdle answers. Here's a quick overview:
- [`nerdle.py`](nerdle.py) contains code to generate all possible nerdle answers.
- [`all_answers.txt`](all_answers.txt) contains those generated answers.
- [`analysis.ipynb`](analysis.ipynb) contains analysis of those generated answers, including various frequency plots, and information on the likelyhood of different operator combinations and number lengths appearing.
- [`plots/*`](plots/) are plots from the notebook.

### Probability of a given symbol appearing
<img src="plots/symbol_probability.jpg" width="500">

### Frequency of symbols per position
<img src="plots/frequency_of_symbols_per_position.jpg" width="1000">


Take a look at [`analysis.ipynb`](analysis.ipynb) for more!
