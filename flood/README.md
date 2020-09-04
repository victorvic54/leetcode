## Flooding

Q1: Highest point then the (8-neighbour)
```
1 2 3      0 0 0
4 5 8  ->  0 0 1
9 7 0      1 0 0
```

Q2: Flowing water from high point to the surroundings (also make sure lower can't flow to higher)
```
1 2 3      0 0 0
4 5 8  ->  0 0 1
9 7 0      1 0 0
```
```
At (1, 2)
1 1 1
1 1 1
0 1 1

At (2, 0)
1 1 1
1 1 1
1 1 1

Answer:
2 2 2
2 2 2
1 2 2
```

Q3: Plateau: any same level height will be higher then the 8 neighbours
```
1 2 3 4    0 0 0 0
5 5 5 2    1 1 1 0
1 1 1 1 -> 0 0 0 0
0 0 0 9    0 0 0 1
```
```
1 2 3 9    0 0 0 0
5 5 5 2    0 0 0 0
1 1 1 1 -> 0 0 0 0
0 0 0 9    0 0 0 1
```