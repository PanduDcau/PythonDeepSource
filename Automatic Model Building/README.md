# Automating the Archetypal Machine Learning Workflow and Model Deployment

This repository contains a Python-based Machine Learning (ML) project, whose primary aim is to demonstrate the archetypal ML workflow within a Jupyter notebook, together with some proof-of-concept ideas on automating key steps, using the Titanic binary classification dataset developed From `Plant Dispatch model from July`

### Running Python, IPython and JupyterLab from the Project's Virtual Environment

In order to continue development in a Python environment that precisely mimics the one the project was initially developed with, use Pipenv from the command line as follows,

```bash
pipenv run python3
```

The `python3` command could just as well be `ipython3` or the JupterLab, for example,

```bash
pipenv run jupyter lab
```

This will fire-up a JupyterLab *where the default Python 3 kernel includes all of the direct and development project dependencies*. This is how we advise that the notebooks within this project are used.
