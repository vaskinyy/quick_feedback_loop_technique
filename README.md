# Quick feedback loop technique

The quick feedback loop is a technique used by probably every single developer. The idea behind the technique 
is that you shorten the feedback loop and get a result of the execution immediately. Anything can be run this way - 
an API call, a CLI command, a function, an individual statement. This is such a simple and universal approach that 
it can be applied to many technologies.

This repository is a collection of examples that demonstrate the usage of the technique. It is mainly Python-based, yet,
there are other technologies as well.

## Running Python samples locally

Create a virtualenv. There are many ways to do this, here are a few of them:

```
python3 -m venv env
```

or

```
pip install virtualenv
virtualenv env
```

Activate the virtual environment
```
source env/bin/activate
```

Install dependencies locally
```
pip install -r requirements.txt
```

Run any example like 
```
python -m repl.main
```


## Examples

- REPL (incl. checking python built-ins)
- Running functions or snippets. Debugger
- Copy the code from somewhere and run it. Scratches
    - StackOverflow
    - ChatGPT
- Running tests
- Running APIs
- Large codebase or legacy + debugger
- Non-Python examples
    - Browser console for JS
    - JS samples
    - Databases
    - Terraform
