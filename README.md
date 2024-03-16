# Insurance product propensity model

**Note**: _This template uses poetry to manage project dependencies

## How to reproduce this project
Install poetry:
```bash
pip install poetry
```
All main dependencies for this project are specified in pyproject.toml. 
To install all dependencies: 
* Locate to folder containing pyproject.toml.
* Run following command in a separate venv
```bash
poetry install
```

## Tools used in this project
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management

* [Venn-ABERs](https://github.com/ptocca/VennABERS): SOTA classifier calibration method from conformal prediction framework
  
## Project Structure
```bash
.
├── .gitignore                      # ignore files that cannot commit to Git
├── data 
|   ├── submission                  # final submission
│   ├── train_data                  # data after training the model
│   └── test_data                   # data after processing
├── models                          # store models
├── notebooks.ipynb                 # notebooks
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── eda.py                      # explotory data analysis and vizualisation
│   └── feat_select.py              # feature selection
├── catboost_info                   # experiment logging
```

