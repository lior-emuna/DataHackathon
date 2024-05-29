def main():
    try:
        import numpy as np
        import pandas as pd
        import networkx as nx
        import sklearn
        import tensorflow as tf
        import matplotlib.pyplot as plt
        import seaborn as sns
        import requests
        import websockets
        import bs4
        import lxml
        import PyQt5
        import scipy
        import statsmodels.api as sm
        import plotly
        import dash
        import jupyterlab

        print('All libraries imported successfully!')

    except ImportError as e:
        print(f'Error importing library: {e}')


if __name__ == "__main__":
    main()
