from web3 import Web3
from web3.middleware import geth_poa_middleware
import web3

def conexec() :
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.skalenodes.com/v1/green-giddy-denebola'))
    user_address = "0xd00faF7c2a837DC457389758Ea1271aE6256dc44"
    nonce = w3_instance.eth.get_transaction_count(user_address)

    contract_address = '0xD16539Fa2Fe90F80066a103dDB78cA81Bc33166B'


    abi = '[{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"strength","type":"uint256"},{"indexed":false,"internalType":"bool","name":"uniqueBurns","type":"bool"}],"name":"CrystalStrength","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"burnCrystals","outputs":[{"internalType":"uint8[]","name":"_classIds","type":"uint8[]"},{"internalType":"uint256","name":"leng","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"burnCrystals2","outputs":[{"internalType":"uint8[]","name":"_classIds","type":"uint8[]"},{"internalType":"uint256","name":"leng","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"classIds","type":"uint8[]"}],"name":"calcStrength","outputs":[{"internalType":"uint256","name":"strength","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"crystalContract","outputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"}],"name":"setConfigCrystalContract","outputs":[{"internalType":"bool","name":"result","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

    print("started....")

    contract = w3_instance.eth.contract(
        address=contract_address,
        abi=abi
    )

    logs = contract.events.CrystalStrength().get_logs(fromBlock=5359929)


    for log in logs:
        print (log)

    return
   # events = contract.events.CrystalStrength().process_receipt(receipt, errors=DISCARD)

   # w3_instance.middleware_onion.inject(geth_poa_middleware)

    if not w3_instance.is_connected():
        print("connection failed....")
        return

    address = Web3.to_checksum_address(contract_address)

    start_block = 5359929
    end_block = 5359930
     
    #end_block = w3_instance.eth.get_block("latest")["number"]
    #end_block = 5383777
    print(end_block)

    if not end_block:
        print("End Block not found....")
        return

    # if (end_block - start_block) > 999:
    #     end_block = start_block + 999

    print(start_block, end_block)

    if start_block >= end_block:
        print("Reached to latest block....")
        return

    
    #0x07526bf28fcea2c436c5233ef3c600e2d5496a4b31f397efbeff2ff7f36d4ea9

    print (address)
    logs = w3_instance.eth.get_logs(
        {
            "fromBlock": start_block,
            "toBlock": end_block,
            "address": address,
            "topics": [""],
        },
    )

    print (logs)
    fetching_block = end_block

    for event in logs:
        print(event)

        print ("wwwferer")
        # raw_log_data = event["data"]

        # decoded_data = decode_data(raw_log_data)

        # strength = decoded_data.get("strength")
        # unique_burns = decoded_data.get("uniqueBurns")
        # tx_hash = event["transactionHash"].hex()

        # tx = w3_instance.eth.get_transaction(tx_hash)
        # sender = tx["from"].lower()

        # print("sender ==> ", sender)
        # print("strength ==> ", strength)
        # print("unique_burns ==> ", unique_burns)
        # print("tx_hash ===>", tx_hash)
        # print("block_height ===>", event["blockNumber"])

        # timestamp = w3_instance.eth.get_block(event["blockNumber"]).timestamp
        # block_signed_at = datetime.datetime.utcfromtimestamp(timestamp)
        # print("block_signed_at ===>", block_signed_at)

conexec()