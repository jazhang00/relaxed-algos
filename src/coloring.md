### Graph Coloring Approximation of 3-Colorable Graphs with SDP Rounding

Imagine each vertex is assigned a unit vector and applying the SDP rounding technique from max cut on an unweighted bipartite graph $G=(U,V,E)$. What we should get intuitively is that the vectors in $U$ form one cluster and the vectors in $V$ form another cluster such that $u^Tv = -1$ for $u \in U$ and $v \in V$. All the edges between $U$ and $V$ go between the two clusters, and get cut by the hyperplane. A bipartite graph can be colored with 2 colors.

For the general coloring problem, when we have an edge $(u, v)$, we would want their associated vectors to be far apart. This may look like $x_u^Tx_v \leq c$, where, since $x_u$ and $x_v$ are unit vectors, $-1 \leq c \leq 1$.

Imagine a 3 colorable graph. The unit vectors can be assigned to the points of an equilateral triangle inscribed into the circle. Then, they are an angle of $2\pi / 3$ apart. So, $x_u^Tx_v = ||x_u||||x_v|| \cos \theta_{uv} = \cos (2\pi / 3) = -1/2$

---

SDP:

$$
\begin{align*}
    &\min_{x_u: \forall u \in V} &&c \\
    &\text{s.t.} \quad &&\langle x_u, x_v \rangle \leq c \\
    & \quad &&||x_u|| = 1 \quad \forall u \in V
\end{align*}
$$


---

We assume that if a graph is 3-colorable, then for any edge $(u, v)$ in the SDP, $x_u$ and $x_v$ have an angle of $2\pi / 3$ apart, which means that the chance that they are on the same side of a hyperplane is $1/3$.

The rounding works as follows. We first make $t$ cuts by picking random hyperplanes. The expected cost is:
$$
\sum_{u \in V} \sum_{(u,v) \in E} P[\text{$(u,v)$ is cut}]
$$
The chance that after $t$ cuts, $(u,v)$ remains unbroken is $(1/3)^t$. So, the expected cost is bounded by $n \cdot 