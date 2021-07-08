from dry_run import trouble


write_to_s3 = object()


@trouble.could_cause(write_to_s3)
def job_1():
    """Function that maybe writes to s3."""
    # Just pretend it does


@trouble.could_only_cause(trouble.nothing)
def command_1():
    job_1()


@trouble.could_only_cause(trouble.only(write_to_s3))
def command_2():
    job_1()


def test_1():
    # Running job_1 directly shouldn't raise
    job_1()

    # command_1 possibly causes write_to_s3 trouble
    # without declaring that. It should raise.
    try:
        command_1()
        assert False
    except trouble.PossibleTrouble as exc:
        assert exc.trouble_token == write_to_s3

    # command_2 declares that it's safe to write_to_s3
    # so it should't raise trouble.PossibleTrouble.
    command_2()
