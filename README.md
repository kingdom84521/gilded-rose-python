# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)

## Initialize & Startup the project

Please ensure your python version is at least `3.12` first，this project hasn't test through python that is older then `3.12`

```bash
python3 -m venv .venv
.venv/bin/pip install .
source .venv/bin/activate
```

## Run the unit tests from the Command-Line

```bash
./scripts/start_unittest.py
```

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```bash
python -m tests.texttest.texttest_fixture 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

```bash
./scripts/start_texttest.sh
```
