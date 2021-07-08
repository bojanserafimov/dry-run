dry-run
=======
Prevent accidentally running code that does bad things.

Example
-------

See tests

Features and non-features
-------------------------
- Supports arbitrary user-defined system of troubles and permissions
- Not fool-proof and will never be (impossible in python)
- Not thread-safe yet, though it could be if someone asked

Local development
-----------------
- install poetry by running `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- run `poetry install`
- run `poetry run pytest`
