

# How to Use

## If using locally

### Conda Virtual Environment & Installing dependencies + necessary packages
conda env create -f environment.yml
conda activate gstatsmcmc
OR 
conda deactivate 

## If working on a node

### 1. Navigate into your repo
cd MonteCarloMarkovChain

### 2. Create a virtual environment
python3 -m venv venv

### 3. Activate it
source venv/bin/activate

### 4. Upgrade pip (important!)
pip install --upgrade pip

### Installing packages
pip install -r requirements.txt


# Software 
Python 3.10.9