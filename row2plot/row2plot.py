import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tqdm import notebook
import warnings
warnings.filterwarnings("ignore") 

class row2plot():
    def __init__(self, data):
        self.data = data

    def row2hist(self, foldername = "hist_plot"):
        try:
            if not os.path.isdir(foldername):
                os.makedirs(foldername)
                for i in notebook.tdqm(range(len(self.data))):
                    plt.figure(figsize = (15,6))
                    ax = sns.distplot(self.data.iloc[i,:])
                    fig = ax.get_figure()
                    fig.savefig(f'{foldername}/row_{i}.png')
                    fig.clf()
            else:
                for i in notebook.tqdm(range(len(self.data))):
                    plt.figure(figsize = (15,6))
                    ax = sns.distplot(self.data.iloc[i,:])
                    fig = ax.get_figure()
                    fig.savefig(f'{foldername}/row_{i}.png')    
                    fig.clf()
                    
        except Exception as e:
            print(f'{e}')
         

    def row2kde(self, foldername = "hist_plot"):
        try:
            if not os.path.isdir(foldername):
                os.makedirs(foldername)
                for i in notebook.tdqm(range(len(self.data))):
                    plt.figure(figsize = (15,6))
                    ax = sns.kdeplot(self.data.iloc[i,:])
                    fig = ax.get_figure()
                    fig.savefig(f'{foldername}/row_{i}.png')
                    fig.clf()
            else:
                for i in notebook.tdqm(range(len(self.data))):
                    plt.figure(figsize = (15,6))
                    ax = sns.kdeplot(self.data.iloc[i,:])
                    fig = ax.get_figure()
                    fig.savefig(f'{foldername}/row_{i}.png')                    
                    fig.clf()

        except Exception as e:
            print(f'{e}')
