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


def test_rebuild_cache_not_allowed_to_send_email():
    try:
        rebuild_cache()
        assert False
    except trouble.PossibleTrouble as exc:
        assert exc.trouble_token == send_email

def test_process_request_allowed_to_send_email():
    process_request({})
