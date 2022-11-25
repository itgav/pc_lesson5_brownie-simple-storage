# from brownie import accounts
# added 'config' for private key in .yaml file
from brownie import accounts, config, network, SimpleStorage

# import os


def deploy_simple_storage():
    # will mark account as 0th index of the accounts that brownie spins up by default with ganache-cli
    account = get_account()
    # can also create account with 'brownie accounts new {account_name}'
    # account = accounts.load("test_account")  # load custom brownie account
    # or, can have private key pull in from a .env file
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # or can define in .yaml -> more explicit than just pulling from .env
    # account = accounts.add(config["wallets"]["from_key"])

    # to deploy: add contract to import; then, code below
    # Brownie can intiuitively determine if a transaction or a call
    simple_storage = SimpleStorage.deploy({"from": account})
    # since a 'view' function don't need the {from: account}
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # wait 1 block
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# if deploying on a dev chain can use account[0], otherwise pull from config
# get error for account[0] if not dev chain because no default account[0]
def get_account():
    if network.show_active() == "development":  # 'network' keyword in brownie
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
