from dry_run import trouble


send_email = object()


@trouble.could_cause(send_email)
def send_email_to_client(destination, content):
    """Function that maybe writes to s3."""
    # Just pretend it does


@trouble.could_only_cause(trouble.nothing)
def rebuild_cache():
    # ...
    # This shouldn't be allowed
    send_email_to_client("alice@wonder.land", "Hello")


@trouble.could_only_cause(trouble.only(send_email))
def process_request(request):
    # ...
    send_email_to_client("alice@wonder.land", "Hello")


def test_1():
    # rebuild_cache should be prevented from sending email
    try:
        rebuild_cache()
        assert False
    except trouble.PossibleTrouble as exc:
        assert exc.trouble_token == send_email

    # We might need to send an email while processing a
    # request. Verify that it's allowed.
    process_request({})
