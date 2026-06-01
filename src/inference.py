"""
inference.py — Member C (Inference Analyst)
W12: Confidence Intervals & Credible Intervals
"""

import numpy as np
from scipy import stats


def ci_proportion_wald(k: int, n: int, conf: float = 0.95) -> dict:
    """CI untuk proporsi theta dengan pendekatan Wald (CLT)."""
    if n <= 0:
        raise ValueError("n harus positif.")
    if not (0 <= k <= n):
        raise ValueError("k harus 0 <= k <= n.")

    theta_hat = k / n
    se        = np.sqrt(theta_hat * (1 - theta_hat) / n)
    z         = stats.norm.ppf(1 - (1 - conf) / 2)
    margin    = z * se

    return {
        "theta_hat": round(theta_hat, 6),
        "se"       : round(se, 6),
        "z"        : round(z, 6),
        "margin"   : round(margin, 6),
        "lower"    : round(theta_hat - margin, 6),
        "upper"    : round(theta_hat + margin, 6),
        "conf"     : conf,
    }


def ci_proportion_wilson(k: int, n: int, conf: float = 0.95) -> dict:
    """Wilson score CI untuk proporsi theta (lebih akurat saat theta dekat 0/1)."""
    if n <= 0:
        raise ValueError("n harus positif.")
    if not (0 <= k <= n):
        raise ValueError("k harus 0 <= k <= n.")

    theta_hat = k / n
    z         = stats.norm.ppf(1 - (1 - conf) / 2)
    denom     = 1 + z**2 / n
    center    = (theta_hat + z**2 / (2 * n)) / denom
    half      = (z / denom) * np.sqrt(theta_hat * (1 - theta_hat) / n + z**2 / (4 * n**2))

    return {
        "theta_hat": round(theta_hat, 6),
        "z"        : round(z, 6),
        "lower"    : round(center - half, 6),
        "upper"    : round(center + half, 6),
        "conf"     : conf,
    }


def ci_poisson_mean(lam_hat: float, n: int, conf: float = 0.95) -> dict:
    """CI untuk mean Poisson lambda dengan CLT."""
    if lam_hat < 0:
        raise ValueError("lambda_hat tidak boleh negatif.")
    if n <= 0:
        raise ValueError("n harus positif.")

    se     = np.sqrt(lam_hat / n)
    z      = stats.norm.ppf(1 - (1 - conf) / 2)
    margin = z * se

    return {
        "lambda_hat": round(lam_hat, 6),
        "se"        : round(se, 6),
        "z"         : round(z, 6),
        "margin"    : round(margin, 6),
        "lower"     : round(max(0.0, lam_hat - margin), 6),
        "upper"     : round(lam_hat + margin, 6),
        "conf"      : conf,
    }


def credible_interval_beta(alpha: float, beta: float, conf: float = 0.95) -> dict:
    """Equal-tailed credible interval dari Beta posterior."""
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha dan beta harus positif.")

    dist  = stats.beta(alpha, beta)
    tail  = (1 - conf) / 2
    lower = dist.ppf(tail)
    upper = dist.ppf(1 - tail)
    mean  = alpha / (alpha + beta)
    mode  = (alpha - 1) / (alpha + beta - 2) if (alpha + beta - 2) > 0 else float("nan")

    return {
        "alpha": alpha,
        "beta" : beta,
        "mean" : round(mean, 6),
        "mode" : round(mode, 6),
        "lower": round(lower, 6),
        "upper": round(upper, 6),
        "conf" : conf,
    }