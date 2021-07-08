dry-run
=======
Prevent accidentally running code that does bad things.

Say you have a `send_email_to_client` function, and a few scripts
in your project: `notify-clients` and `run-local-tests`. You don't
want to accidentally send an email by running tests. But people who
are new to your project will not read every line of code before
running it so they might run `notify-clients` just to see what
happens and send them some garbage.

Here's the solution:
1. Import the `trouble` module: `from dry_run import trouble`
1. Create a token that represents email sending: `send_email = object()`
2. Decorate the `send_email_to_client` function with `@trouble.could_cause(send_email)`
3. Decorate the `run-local-tests` function with `@trouble.could_only_cause(trouble.nothing)`
   declaring that it couldn't cause trouble. Now the new team member can run this
   safely. If the function ends up trying to cause trouble, it will raise an error
   instead.
4. Decorate the `notify-clients` function with `@trouble.could_only_cause(trouble.only(send_email))`
   so that it wouldn't raise an error when it tries to send an email.

Local development
-----------------
- install poetry by running `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- run `poetry install`
- run `poetry run pytest`
