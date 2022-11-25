# need file name to start with 'test_' to tip off Brownie
# run test in terminal with: 'brownie test'
# to test just 1 function: 'brownie test -k {function name}'
# to see what went wrong, can run 'brownie test --pdb' --> 'quit()' to exit this mode in the terminal
# to see print lines and get more robust info: 'brownie test -s'

from brownie import SimpleStorage, accounts


def test_deploy():
    # typical setup for testing: 1) arrange, 2) act, 3) assert
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 1  # since it hasn't been set, expect favorit number to be 0
    # assert
    assert starting_value == expected


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # assert
    assert expected == simple_storage.retrieve()
