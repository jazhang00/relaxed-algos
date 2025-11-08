### Max Cut Approximation via SDP Rounding

Given a weighted, undirected graph $G=(V,E)$. We wish to find a partition $(S, V\setminus S)$ that maximizes the weight of the cut.

**Integer program**: we assign to each vertex $-1$ or $1$, and try to maximize the weight of the cut.

$$
\begin{align*}
&\max &&\sum_{(u,v) \in E} w_{uv} \cdot \frac{|x_u - x_v|}{2} \\
&\text{s.t.} &&x_u \in \{-1, 1\} \quad \forall u \in V
\end{align*}
$$

**SDP Relaxation**: Instead of just $\{-1, 1\}$, we give each vertex a unit vector. Let $n = |V|$. We can relax max cut to the following problem:

$$
\begin{align*}
&\max_{\{x_u \in \mathbb{R}^n: u \in V \}} &&\sum_{(u,v) \in E} w_{uv} \cdot \frac{||x_u - x_v||^2}{4} \\
&\text{s.t.} &&||x_u|| = 1 \quad \forall  u \in V
\end{align*}
$$

This is a semidefinite program because:
- $||x_u - x_v||^2 = ||x_u||^2 + ||x_v||^2 - 2x_u^Tx_v = 2 - 2x_u^Tx_v$
- Define a matrix $Y \in \mathbb{R}^{n \times n}$ such that $Y_{uv} = x_u^Tx_v$
- $Y = X^TX$ is positive semidefinite
- $||x_u|| = 1$ implies $Y_{uu} = 1$

This produces the following SDP:

$$
\begin{align*}
&\max_{Y} &&\frac{1}{2}\sum_{(u,v) \in E} w_{uv} \cdot (1 - Y_{uv}) \\
&\text{s.t.} &&Y_{uu} = 1 \quad \forall u \in V \\
& &&Y \succeq 0
\end{align*}
$$

Upon solving the SDP and obtaining $Y$, we can factor it as $Y=X^TX$ to obtain vectors $x_u$ for all $u \in V$.

**Goemans-Williamson Rounding**:
- Pick a random unit vector $t \in \mathbb{R}^n$
- Return $S = \{u : t^Tx_u \geq 0\}$

**Approximation Ratio**:

Let $\theta_{uv}$ be the angle between $x_u$ and $x_v$. Note that $||x_u - x_v||^2 = 2 - 2\cos\theta_{uv}$.
- The probability edge $(u,v)$ is cut is $\theta_{uv}/\pi$
    - To show this, consider the component of $t$ within the subspace spanned by $x_u$ and $x_v$.
- The expected weight of the cut is $\sum_{(u,v) \in E} w_{uv} \theta_{uv} / \pi$
- The SDP relaxation has cost $\sum_{(u,v) \in E} w_{uv} \cdot \frac{1 - \cos \theta_{uv}}{2}$
- For $1/\alpha = \max_\theta \{\frac{1 - \cos\theta}{2} \cdot \frac{\pi}{\theta}\}$, $\alpha \approx 0.878$.