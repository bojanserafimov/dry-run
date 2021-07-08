from dry_run import trouble, utils
import inspect


@trouble.cause
def send_email(destination, content):
    """Pretend this function sends email, which could cause trouble."""


def expect_to_send_myself_email(cause, args, kwargs):
    destination = utils.get_arg(cause, args, "destination")
    return cause == send_email and destination == "me@my.company"


@trouble.expected(expect_to_send_myself_email)
def send_to_me():
    """Correctly send email to myself."""
    send_email("me@my.company", "Hi")


@trouble.expected(trouble.no_trouble)
def send_to_me_without_declaring():
    """Send email without declaring this function could send an email."""
    send_email("me@my.company", "Hi")


@trouble.expected(expect_to_send_myself_email)
def send_to_alice_thinking_it_goes_to_me():
    """Declare sending email to myself, but actually send to someone else."""
    send_email("alice@wonder.land", "Hi")


valid_functions = (
    send_to_me,
)

invalid_functions = (
    send_to_me_without_declaring,
    send_to_alice_thinking_it_goes_to_me,
)


def test_dry_run():
    for fn in valid_functions:
        fn()

    for fn in invalid_functions:
        try:
            fn()
            assert False
        except trouble.PossibleTrouble as exc:
            pass
