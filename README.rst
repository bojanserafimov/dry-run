dry-run
=======
Prevent accidentally running code that does bad things.

Example
-------

.. end-to-end-sql-example-start

.. code:: python
    from dry_run import trouble

    # Declare that accidentally sending emails to clients is one of our worries
    send_email = object()

    # Specify that this function potentially send emails
    @trouble.could_cause(send_email)
    def send_email(destination, content):
        # ... stuff

    # This function might send an email
    @trouble.could_only_cause(trouble.nothing)
    def process_request(request):
        # ... stuff

    # Local tests shouldn't be doing anything sketchy.
    @trouble.could_only_cause(trouble.nothing)
    def run_local_tests():
        # ... stuff

        # This would raise trouble.PossibleTrouble
        # send_email("alice@foo.bar", "Hello")

.. end-to-end-sql-example-end


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
