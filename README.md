# Efficient Retrieval of Music Recordings Using Graph-Based Index Structures

## Background

This repository contains accompanying code for the following article.
If you use code from this repository, please consider citing the paper.

```
Frank Zalkow, Julian Brandner, and Meinard Müller. Efficient retrieval of music recordings using graph-based index
structures. Signals, 2(2):336–352, 2021. doi: 10.3390/signals2020021.
```

This paper compares indexing strategies based on K-d trees and HNSW graphs in a cross-modal music retrieval application.
In this repository, we provide an example dataset and a Jupyter notebook that shows how to load the dataset's features, generate shingles, reduce the shingle dimensionality using PCA, construct index structures (K-d trees and HNSW graphs), and search for the nearest shingles to a given query in the database.

For more details, we refer to [the paper](https://www.mdpi.com/2624-6120/2/2/21) and the accompanying website.

https://www.audiolabs-erlangen.de/resources/MIR/2020_signals-indexing

## Usage

You need to create an Anaconda environment to use the code in this repository.
If you are not familiar with Anaconda, we refer to the introductions in the FMP Notebooks ([Get Started](https://www.audiolabs-erlangen.de/resources/MIR/FMP/B/B_GetStarted.html), [Installation](https://www.audiolabs-erlangen.de/resources/MIR/FMP/B/B_Installation.html)).
The environment is created with the following command.

```
conda env create -f environment.yml
```

Then you may start a Jupyter server to execute the notebook containing our code.

```
conda activate music-indexing
jupyter notebook
```

## Acknowledgements

Frank Zalkow and Meinard Müller are supported by the German Research Foundation (DFG-MU 2686/11-1, MU 2686/12-1).
The International Audio Laboratories Erlangen are a joint institution of the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) and Fraunhofer Institute for Integrated Circuits IIS.
