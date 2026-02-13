Time Limit: **1 second**

Memory Limit: **32 MB**

You are given $n$ artifacts. Artifact $i$ has an aura value $a_i$. You are also given weights $w_1, w_2, \dots, w_n$ (weights may be negative).

First, build a deterministic lineup:

- Create pairs $(a_i, i)$ for $i=1..n$.
- Sort these pairs by increasing $a_i$, and if $a_i$ are equal, by increasing $i$.
- Let the sorted aura values be $v_0, v_1, \dots, v_{n-1}$ in this order.

Now you will produce an array $p_1, p_2, \dots, p_n$ by taking elements from $v$ using the following rule:

- Choose any starting index $s$ ($0 \le s \le n-1$) and set $p_1 = v_s$.
- Mark position $s$ as taken. The taken positions always form an interval $[L, R]$ (initially $L=R=s$).
- For each step $k=2..n$, you must take exactly one element adjacent to the current taken interval:
  - if $L>0$, you may take $v_{L-1}$ (then set $L := L-1$),
  - if $R < n-1$, you may take $v_{R+1}$ (then set $R := R+1$).

For each prefix $p_1..p_i$, define:
- $\min_i = \min(p_1, p_2, \dots, p_i)$
- $\max_i = \max(p_1, p_2, \dots, p_i)$

The weighted score of the process is:
$$
\text{Score}(p) = \sum_{i=1}^{n} w_i \cdot (\max_i - \min_i).
$$

For each test case, find the maximum possible score over all valid ways to construct $p$.

**Input Format:-**

The first line contains an integer $t$ — the number of test cases.

For each test case:
- The first line contains an integer $n$.
- The second line contains $n$ integers $a_1, a_2, \dots, a_n$.
- The third line contains $n$ integers $w_1, w_2, \dots, w_n$.

**Output Format:-**

For each test case, output one integer — the maximum achievable score.

**Constraints:-**

- $1 \le t \le 20$
- $1 \le n \le 2000$
- $\sum n \le 2000$ over all test cases
- $1 \le a_i \le 10^9$
- $-10^6 \le w_i \le 10^6$
- The answer fits in signed 64-bit integer.

**Examples:-**
 - **Input:**
```
1
5
2 1 2 1 2
7 -3 7 -3 7
```

 - **Output:**
```
11
```

 - **Input:**
```
1
8
1 1000000000 2 999999999 3 999999998 4 999999997
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000
```

 - **Output:**
```
6999999972000000
```

**Note:-**

**First example:** With the given input $n=5$, $a = [2,1,2,1,2]$, $w = [7,-3,7,-3,7]$, after sorting pairs $(a_i,i)$ we get the lineup
$$
v = [1,1,2,2,2].
$$
One optimal construction is to start at $s=2$ (value $2$), then expand left twice, then right twice, producing
$$
p = [2,1,1,2,2].
$$
For each prefix, $(\max_i-\min_i)$ becomes $0,1,1,1,1$, so the score is
$$
7\cdot 0 + (-3)\cdot 1 + 7\cdot 1 + (-3)\cdot 1 + 7\cdot 1 = 11.
$$
Hence the output $11$ is correct.

**Second example:** With the given input $n=8$, auras $[1, 10^9, 2, 999999999, 3, 999999998, 4, 999999997]$, and weights all $10^6$, after sorting pairs $(a_i,i)$ we have
$$
v = [1,2,3,4,999999997,999999998,999999999,1000000000].
$$

All weights are $10^6$, so we want large ranges as early as possible; starting near the large gap and taking across it immediately is optimal. For example, start at $s=3$ (value $4$), then take $v_{4}=999999997$, then expand left until reaching $1$, and finally expand right to the end, producing
$$
p = [4,999999997,3,2,1,999999998,999999999,1000000000].
$$

Then
$$
(\max_i-\min_i) = 0,999999993,999999994,999999995,999999996,999999997,999999998,999999999.
$$
Thus the score equals
$$
10^6 \cdot (0+999999993+999999994+999999995+999999996+999999997+999999998+999999999)
= 6999999972000000.
$$
Hence the output $6999999972000000$ is correct.