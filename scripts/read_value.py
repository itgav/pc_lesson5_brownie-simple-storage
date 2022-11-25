from brownie import SimpleStorage, accounts, config

# brownie already knows address and ABI
# address in the 'build/deployments' folder
# ABI in the 'build/contracts' folder
def read_contract():
    simple_storage = SimpleStorage[-1]  # most recent deployment of SimpleStorage object
    print(simple_storage.retrieve())


def main():
    read_contract()
