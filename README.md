# DSA_Learning
This Repo consists of the Learnings and know how's about the DSA that I learn and solve along the way of my Journey to Data Scientist

## Basic Terminology used in DSA
---
1️⃣ What is Time Complexity?

Time Complexity means:

How the running time of an algorithm grows when the input size increases.

Important:
We are not measuring seconds, because computers differ.

Instead we measure:
```
How many operations does the algorithm perform?
```

What Does the Big O Mean?
| Big O      | Meaning            |
| ---------- | ------------------ |
| O(1)       | constant time      |
| O(log n)   | very fast          |
| O(n)       | linear             |
| O(n log n) | sorting algorithms |
| O(n²)      | nested loops       |
| O(2ⁿ)      | exponential        |
| O(3ⁿ)      | very slow          |
---

3️⃣ What is Space Complexity?

Space complexity means:

How much memory an algorithm uses as input size grows.

```md
countWays(4)
├── countWays(3)
│   ├── countWays(2)
│   │   ├── countWays(1)
│   │   ├── countWays(0)
│   │   └── countWays(-1)
│   ├── countWays(1)
│   └── countWays(0)
├── countWays(2)
│   ├── countWays(1)
│   ├── countWays(0)
│   └── countWays(-1)
└── countWays(1)
```

