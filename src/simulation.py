import random
import math
from typing import Callable, List, Any

def estimate_probability(event_fn: Callable[[], bool], n_trials: int = 50000) -> float:
    """
    Estimate probability of an event using Monte Carlo simulation.
    
    Parameters
    ----------
    event_fn : Callable[[], bool]
        Function that returns True if event occurs, False otherwise.
    n_trials : int
        Number of Monte Carlo trials.
    
    Returns
    -------
    float
        Estimated probability of the event.
    """
    count = 0
    for _ in range(n_trials):
        if event_fn():
            count += 1
    return count / n_trials

class BloomFilter:
    """
    Simple Bloom Filter implementation.
    """

    def __init__(self, k: int, m: int):
        """
        Parameters
        ----------
        k : int
            Number of hash functions.
        m : int
            Size of bit array.
        """
        self.k = k
        self.m = m
        self.bits = [0] * m

    def _hashes(self, item: Any) -> List[int]:
        random.seed(hash(item))
        return [random.randint(0, self.m - 1) for _ in range(self.k)]

    def add(self, item: Any) -> None:
        for h in self._hashes(item):
            self.bits[h] = 1

    def contains(self, item: Any) -> bool:
        return all(self.bits[h] == 1 for h in self._hashes(item))

    def theoretical_fpr(self, n: int) -> float:
        """
        Theoretical false positive rate after inserting n items.
        Formula: (1 - (1 - 1/m)^n)^k
        """
        return (1 - (1 - 1 / self.m) ** n) ** self.k
    
def mcmc_knapsack(items, capacity, n_iter=100000):
    """
    MCMC for knapsack-like selection.
    
    items : list of dict with keys {'weight', 'value'}
    capacity : maximum total weight
    n_iter : number of MCMC iterations
    """
    import random
    
    n = len(items)
    # initial state: all 0
    state = [0] * n

    def total_weight(s):
        return sum(items[i]['weight'] * s[i] for i in range(n))

    def total_value(s):
        return sum(items[i]['value'] * s[i] for i in range(n))

    # ensure initial state is feasible
    while total_weight(state) > capacity:
        i = random.randint(0, n - 1)
        state[i] = 0

    best_state = state[:]
    best_value = total_value(state)

    for _ in range(n_iter):
        i = random.randint(0, n - 1)
        new_state = state[:]
        new_state[i] = 1 - new_state[i]

        if total_weight(new_state) <= capacity:
            # simple Metropolis: accept if value >=
            if total_value(new_state) >= total_value(state):
                state = new_state
                if total_value(state) > best_value:
                    best_state = state[:]
                    best_value = total_value(state)

    return {
        "best_state": best_state,
        "best_value": best_value,
        "best_weight": total_weight(best_state)
    }    