from dry_run import trouble, utils
import inspect


@trouble.cause
def send_email_to_client(destination, content):
    """Function that maybe writes to s3."""

def expect_to_send_myself_email(cause, args, kwargs):
    destination = utils.get_arg(cause, args, "destination")
    return cause == send_email_to_client and destination == "me@my.company"

@trouble.expected(expect_to_send_myself_email)
def send_to_me_correct():
    """Correctly send email to myself."""
    send_email_to_client("me@my.company", "Hi")

@trouble.expected(trouble.no_trouble)
def send_to_me_incorrect_1():
    """Send email without declaring it."""
    send_email_to_client("me@my.company", "Hi")

@trouble.expected(expect_to_send_myself_email)
def send_to_me_incorrect_2():
    """Declare sending email to myself, but actually send to someone else."""
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
