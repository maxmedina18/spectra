import numpy as np

def simulate_brownian_motion(T, n_steps, n_paths, seed=None):
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    Z = rng.normal(0.0, 1.0, size=(n_paths, n_steps))
    dW = np.sqrt(dt) * Z
    W = np.zeros((n_paths, n_steps + 1))
    W[:, 1:] = np.cumsum(dW, axis=1)
    t = np.linspace(0, T, n_steps + 1)
    return t, W



def simulate_geometric_brownian_motion(T, n_steps, n_paths, mu=0.0, sigma=1.0, S0=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)

    dt = T / n_steps
    t = np.linspace(0, T, n_steps + 1)
    Z = np.random.normal(size=(n_paths, n_steps))
    increments = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
    log_paths = np.cumsum(increments, axis=1)
    log_paths = np.hstack([np.zeros((n_paths, 1)), log_paths])
    S = S0 * np.exp(log_paths)
    return t, S