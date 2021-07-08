dry-run
=======

Prevent accidentally running code that does bad things. It works like this:

#. You mark certain functions potentially trouble-causing (e.g. sending email to clients, dropping a database, etc.) with the :code:`@trouble.cause` decorator.
#. You explicitly specify expected trouble certain functions might cause (most useful for functions near the executable entry points) using the :code:`@trouble.expected` decorator.
#. This library (mostly) prevents a function from causing unexpected trouble by raising a :code:`PossiblyTrouble` exception.

Example
-------

See tests

Local development
-----------------

- install poetry by running :code:`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- run :code:`poetry install`
- run :code:`poetry run pytest`
