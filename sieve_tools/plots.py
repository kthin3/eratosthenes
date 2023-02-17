import matplotlib.pyplot as plt

def plot_sieve(all_nmax, all_proportions,log_scale=True):
    """
    Create a line plot of proportion of prime numbers against N.
    """
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    
    if log_scale:
        plt.xscale("log")
        plt.yscale("log")

