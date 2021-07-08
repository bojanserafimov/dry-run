# dry-run

Prevent accidentally running python code that does bad things.

Decorate potentially troublesome functions with `@trouble.cause`
and decorate safe program entrypoints with `@trouble.expected(safety_predicate)`
to declare and enforce limitations.

## Example

See tests for complete example. TLDR:

```python
from dry_run import trouble

# Dropping a prod db can cause trouble, and we don't
# want to accidentally call this during local testing
# because of a misconfiguration
@trouble.cause
def drop_db(connection, db_name):
    # ...

# Accidentally sending a client emails is not good
@trouble.cause
def send_email(to, message):
    # ...

# This function has no business dropping databases or
# sending emails. If it (or any of the functions it
# calls) tries to cause such trouble, it will raise
# PossiblyTrouble instead
@trouble.expected(trouble.no_trouble)
def run_cache_warming_job():
    # ...

# This function is expected to send an email, but not
# to any arbitrary email address. See tests for a full
# definition of this function
@trouble.expected(expect_to_send_myself_email)
def test_email_client():
   # ...
```

## Limitations
- Not thread safe yet

## Local development

- install poetry by running `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- run `poetry install`
- run `poetry run pytest`
