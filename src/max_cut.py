import cvxpy as cp
import numpy as np


def main():
    n = 10

    W = np.zeros((n, n))
    for u in range(n):
        for v in range(u, n):
            weight = np.random.normal(0, 1)
            W[u, v] = weight
            W[v, u] = weight

    Y = cp.Variable((n, n), symmetric=True)
    objective = cp.Maximize(0.5 * cp.multiply(W, 1 - Y).sum())
    constraints = [Y[u, u] == 1 for u in range(n)] + [Y >> 0]

    prob = cp.Problem(objective, constraints)
    result = prob.solve()

    eigvals, eigvecs = np.linalg.eigh(Y.value)
    eigvals[eigvals < 0] = 0
    XT = eigvecs @ np.diag(np.sqrt(eigvals))

    S = []
    t = np.random.normal(0, 1, size=n)
    for i, x in enumerate(XT):
        if np.dot(x, t) >= 0:
            S.append(i)


if __name__ == "__main__":
    main()
