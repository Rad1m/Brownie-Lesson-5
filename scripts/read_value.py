from brownie import accounts, config, SimpleStorage


def read_contract():
    simple_storage = SimpleStorage[
        -1
    ]  # using -1 will always show the latest deployment. Using 0 would show the very first deployment.
    # we always need to know ABI and Address


def main():
    read_contract()
