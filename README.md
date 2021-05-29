Barebones  VAE

###  Purpose and Scope

This brief demo vae ingests plain numerical data from a csv and attempts to put it through a very
simple VAE.

### This work is derived from two sources:

1.  Abhishek Thakur

This includes his book, "Approaching (Almost) Any Machine Learning" and his youtube tutorials, 101 and Approaching.  This work is used to motivate the data preprocessing  and loading data into Datasets and DataLoaders.  Also information on working with categorical data:  ohe, labels and embeddings.

github:  https://github.com/abhi1thakur/mlframework

2.  Alfredo Canziani

As a demo vae I imported a tutorial from his 2020 course on ML:

https://atcold.github.io/pytorch-Deep-Learning/

https://www.youtube.com/watch?v=7Rb4s9wNOmc&t=2617s

github:  https://github.com/Atcold/pytorch-Deep-Learning


### Clone the repo

The current branch is 'initial"

```
cd 
git clone -b initial https://github.com/marilynwaldman/doggievae
cd doggievae

```


### Setting up the environment

set up conda and create the environment.  This assumes anaconda3 or miniconda3 is installed.



If the 'ml' conda environment is not already installed run:

```
conda env create -f environment.yml

```

Once 'ml' is created, activate it:

```
conda activate ml

```