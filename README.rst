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
