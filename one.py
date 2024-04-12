from web3 import Web3

def conexec() :
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.skalenodes.com/v1/green-giddy-denebola'))
    user_address = "0xd00faF7c2a837DC457389758Ea1271aE6256dc44"
    nonce = w3_instance.eth.get_transaction_count(user_address)

    contract_address = '0xE9d487B950A5075D8eaB084e2E04971340765b86'

    abi = '[{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"},{"internalType":"address","name":"_token","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"class_id","type":"uint8"}],"name":"CrystalMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"commonChance","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"crystalContract","outputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getOwnedNftsRanged","outputs":[{"internalType":"uint256[]","name":"tokensIds","type":"uint256[]"},{"internalType":"uint8[]","name":"classIds","type":"uint8[]"},{"internalType":"uint256","name":"itemsCount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getRandom","outputs":[{"internalType":"bytes32","name":"addr","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"legendaryChance","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mineCrystalFree","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mineCrystalPay","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintCooldownPeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paidBonusTimes","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"}],"name":"setConfigCrystalContract","outputs":[{"internalType":"bool","name":"result","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_commonChance","type":"uint32"},{"internalType":"uint32","name":"_legendaryChance","type":"uint32"},{"internalType":"uint256","name":"_mintPrice","type":"uint256"},{"internalType":"uint8","name":"_paidBonusTimes","type":"uint8"},{"internalType":"uint256","name":"_mintCooldownPeriod","type":"uint256"}],"name":"setMiscConfig","outputs":[{"internalType":"bool","name":"result","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

    contract = w3_instance.eth.contract(
        address=contract_address,
        abi=abi
    )

    print ("wwwttey")


    #return 

    pvt_key = 'b49b3c7fcb628485bc51c4104c4c90b999351f4ab20e1a6c24d90206f1271012'







    # Manually build and sign a transaction:
    tx = contract.functions.mineCrystalFree().build_transaction({
        "chainId": w3_instance.eth.chain_id,
        "from": user_address,
        "nonce": w3_instance.eth.get_transaction_count(user_address),
    })

    signed_tx = w3_instance.eth.account.sign_transaction(tx, private_key=pvt_key)

    # Send the raw transaction:
    #assert contract.functions.message().call() == "gm"
    tx_hash = w3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3_instance.eth.wait_for_transaction_receipt(tx_hash)

    #assert billboard.functions.message().call() == "gn"


    #gas = web3.eth.estimate_gas(tx)

    # tx = contract.functions.mineCrystalFree().buildTransaction(
    #     {
    #         "gasPrice": gas_price,
    #         "from": user_address,
    #         "nonce": nonce,
    #     },
    # )


    #     # Create transacrion


    # print(tx)

    # # Sign Tx
    # signed_tx = w3_instance.eth.account.sign_transaction(tx, user_private_key)

    # # Make transacrion
    # tx_hash_raw = w3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)




conexec()