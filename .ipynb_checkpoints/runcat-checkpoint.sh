# RUN to set up environment with all the packages

#conda env create -f environment.yml # This command will create an environment
conda env create --name ml --file=environment.yml
#conda activate ml
source activate ml
  
python mycategorical.py