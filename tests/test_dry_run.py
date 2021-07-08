from dry_run import trouble


@trouble.cause
def send_email_to_client(destination, content):
    """Function that maybe writes to s3."""

def expect_to_send_myself_email(token, args, kwargs):
    # TODO checking args like this is not resilient to changes
    return token == send_email_to_client.token and args[0] == "me@my.company"

@trouble.expected(expect_to_send_myself_email)
def send_to_me_correct():
    send_email_to_client("me@my.company", "Hi")

@trouble.expected(lambda func, args, kwargs: False)
def send_to_me_incorrect_1():
    send_email_to_client("me@my.company", "Hi")

@trouble.expected(expect_to_send_myself_email)
def send_to_me_incorrect_2():
    send_email_to_client("alice@wonder.land", "Hi")


def test_dry_run():
    send_to_me_correct()

    try:
        send_to_me_incorrect_1()
        assert False
    except trouble.PossibleTrouble as exc:
        pass

    try:
        send_to_me_incorrect_2()
        assert False
    except trouble.PossibleTrouble as exc:
        pass
