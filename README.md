# neetcode-submissions

A personal archive of solutions submitted while practicing problems on [NeetCode.io](https://neetcode.io).

## What's here

The repository stores each solved problem in its own folder (named after the problem), organized under a
top-level category folder. Each attempt at a problem is saved as a separate `submission-N.py` file, so
multiple submissions for the same problem (e.g. re-attempts or refactors) are kept side by side rather than
overwritten.

Currently the repo contains:

- **`Data Structures & Algorithms/`** — the only category present so far
  - `buy-and-sell-crypto/` — "Best Time to Buy and Sell Stock" (2 submissions, both a single-pass min-tracking solution)
  - `is-palindrome/` — "Valid Palindrome" (1 submission, a two-pointer solution)

That's 2 distinct problems / 3 submission files in total as of this writing.

## Tech stack

- **Python 3** — all solutions are written as a `Solution` class with a single method, matching the format
  LeetCode/NeetCode use for submissions. Files rely on `List` from `typing` without importing it, so they are
  not directly runnable as standalone scripts — they're meant to be pasted into the NeetCode/LeetCode online
  editor, which provides that import implicitly.

## Setup / running

There is no build tooling, package manifest, or test suite in this repo. To try a solution locally, add the
missing import and drive it yourself, e.g.:

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        maxProfit = 0
        for i in prices:
            if i < min_num:
                min_num = i
            profit = i - min_num
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
```

## Status

Work in progress / lightly populated. This is a personal practice log, not a curated solutions library:

- Only 2 problems solved so far, both from a single category.
- No tests, no README per problem, no difficulty/topic tagging beyond the one folder name.
- No CI, linting, or automation — solutions are added manually as problems are solved.
- Expect this repo to grow over time as more NeetCode problems are solved.
