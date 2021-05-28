# RUN to set up environment with all the packages

conda env create -f environment.yml # This command will create an environment
#conda env create --name ml --file=environment.yml
# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
#conda env create -f environment.yml
#conda env list
conda activate ml
source activate ml


  
python mycategorical.py
