import cvxpy as cp
import numpy as np


def main():
    n = 100

    W = np.zeros((n, n))
    for u in range(n):
        for v in range(u + 1, n):
            weight = np.random.uniform(0, 1)
            W[u, v] = weight
            W[v, u] = weight

    Y = cp.Variable((n, n), symmetric=True)
    objective = cp.Maximize(0.25 * cp.multiply(W, 1 - Y).sum())
    constraints = [Y[u, u] == 1 for u in range(n)] + [Y >> 0]

    prob = cp.Problem(objective, constraints)
    result = prob.solve()

    eigvals, eigvecs = np.linalg.eigh(Y.value)
    eigvals[eigvals < 0] = 0
    XT = eigvecs @ np.diag(np.sqrt(eigvals))

    # compute cuts & expected cost
    samples = 10
    costs = []
    for _ in range(samples):
        S = set()
        t = np.random.normal(0, 1, size=n)
        for i, x in enumerate(XT):
            if np.dot(x, t) >= 0:
                S.add(i)

        # compute cost of cut
        cost = 0
        for u in range(n):
            for v in range(u + 1, n):
                if u in S and v not in S:
                    cost += W[u, v]
                if u not in S and v in S:
                    cost += W[u, v]
        costs.append(cost)
    expected_cost = sum(costs) / samples

    estimated_rank = sum(np.abs(eigvals) > 1e-5)

    print(f"estimated rank of vectors: {estimated_rank}")
    print(f"expected cost: {expected_cost:.3f}")
    print(f"sdp bound: [{result * 0.878:.3f}, {result:.3f}]")


if __name__ == "__main__":
    main()
