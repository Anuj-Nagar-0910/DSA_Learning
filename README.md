# DSA_Learning
This Repo consists of the Learnings and know how's about the DSA that I learn and solve along the way of my Journey to Data Scientist

## Basic Terminology used in DSA
---
### What is Time Complexity?

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
### What is Space Complexity?

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
---
### The Universal LEGO Rule

Dynamic Programming always follows this pattern:
```
Solution(n) =
combine(
   solution(n-1),
   solution(n-2),
   solution(n-3)
)
```
We build big solutions using smaller solutions.

#### The Deep Insight

Almost every DP problem in interviews follows this LEGO rule.

Examples:
| Problem     | Recurrence                |
| ----------- | ------------------------- |
| Fibonacci   | F(n)=F(n−1)+F(n−2)        |
| Stairs      | W(n)=W(n−1)+W(n−2)+W(n−3) |
| Coin Change | ways(n)=ways(n−coin)      |

Dynamic Programming is actually just:
```
Recursion + Memory
```

---
