# best_practise

**best_practise** is a template of git repository with some of best practises for projects code.<br/>
All project shall respect the :
- [Repository Structure](#repository-structure)
- [Code Structure](#code-structure)
- [Documentation](#documentation)
- [Installation](#installation)
- [Configuration](#config)
- [How to use](#use)

## Repository Structure <a name="repository-structure"></a>

```
|_ app
|____ __init__.py
|____ [your_code].py
|_ requirements.txt
|_ README.md
|_ .gitignore
```

- ```requirements.txt``` contains the list of all packages that need to be installed to make the code work well. <br/>
See example [here](requirements.txt).
- ```.gitignore``` lists all the files or files type that must not be loaded into the git repo.<br/> See example [here](.gitignore).
- The ```__init__.py``` can be an empty fill but is needed if you want to load your code as a package

## Code Structure <a name="code-structure"></a>

The code files (.py) must be as clear as possible and must respect python best practises. <br/>
An example is given [here](app/HelloWorld.py)

## Documentation <a name="documentation"></a>

**[ProjectName]** is ... 

Add description of the project, context and what can be done with the code.


## Installation <a name="installation"></a>

If your project is packaged :

```shell
pip install your-package
```

Otherwise :

```shell
git clone [link_to_your_git_repository]
cd your_repository
pip install -r requirements.txt
```

## Configuration <a name="config"></a>

If your code needs some configuration (connection parameters, API keys, name of database, path to local file...) you shall create a ```config.py``` file imported from within your code

## How to Use <a name="use"></a>

Show how to execute your code if it contains some scripts:

```shell
cd app
$ python your_code.py [some_parameters]  
```

or detail the methods that can be used in your code:<br/>
*(Name of the methods, inputs, outputs, usage)*

```shell
$ python
```

```python
>>> from app import your_code

>>> your_code.some_function(some_parameters)
"Hello World"

>>> your_code.some_other_function(some_other_parameters)
3
```
