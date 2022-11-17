import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Visualizer:
    def make_histogram(self, data: pd.DataFrame, variable: str, binwidth: int, lower_limit: int = None, upper_limit: int = None) -> None:
        if upper_limit is None:
            upper_limit = data[variable].max()
        if lower_limit is None:
            lower_limit = data[variable].min()
        bins = np.arange(lower_limit, upper_limit + binwidth, binwidth)
        plt.hist(data[variable], bins=bins, edgecolor='black',
                 alpha=0.75, range=[data[variable].min(), upper_limit])
        plt.ylabel("Count")
        plt.xlabel(variable)

    def make_scatter_plot(self, data: pd.DataFrame, para1: str, para2: str, logx: bool = False, logy: bool = False ):
        plt.plot(data[para1], data[para2], '*', alpha=0.1)
        if logx:
            plt.xscale("log")
        if logy:
            plt.yscale('log')
        plt.xlabel(para1)
        plt.ylabel(para2)

    def corr_heatmap(self, figsize=(10, 10), data=None):
        if data is None:
            data = self.df

        _, axs = plt.subplots(figsize=figsize)
        ax = sns.heatmap(
            data.corr(), vmin=-1, vmax=1, cmap="BrBG", linewidths=0.5, annot=True, ax=axs)
        ax.set_title('Correlation matrix')
        return ax
