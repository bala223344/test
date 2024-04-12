from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN

#USING web3==6.15.1
#explorer https://green-giddy-denebola.explorer.mainnet.skalenodes.com/address/0xD16539Fa2Fe90F80066a103dDB78cA81Bc33166B/transactions#address-tabs

def conexec() :
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.skalenodes.com/v1/green-giddy-denebola'))




    burn_address = '0xD16539Fa2Fe90F80066a103dDB78cA81Bc33166B'

    abi = '[{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"strength","type":"uint256"},{"indexed":false,"internalType":"bool","name":"uniqueBurns","type":"bool"}],"name":"CrystalStrength","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"burnCrystals","outputs":[{"internalType":"uint8[]","name":"_classIds","type":"uint8[]"},{"internalType":"uint256","name":"leng","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"burnCrystals2","outputs":[{"internalType":"uint8[]","name":"_classIds","type":"uint8[]"},{"internalType":"uint256","name":"leng","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8[]","name":"classIds","type":"uint8[]"}],"name":"calcStrength","outputs":[{"internalType":"uint256","name":"strength","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"crystalContract","outputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract CG_SKLAE_CRYS","name":"_crystalContract","type":"address"}],"name":"setConfigCrystalContract","outputs":[{"internalType":"bool","name":"result","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

    contract = w3_instance.eth.contract(
        address=burn_address,
        abi=abi
    )




    #receipt = w3_instance.eth.get_transaction_receipt("0xdc92aa876e895e78c419a3ab4e29f6621e649b0f0a1a80937fd2fed9087a7bae")
    receipt = w3_instance.eth.get_transaction_receipt("0x9704a996dcd8bcdeaf661318ed83a9bd0f8d66a4120253140346c9288a863f04")


    events = contract.events.CrystalStrength().process_receipt(receipt, errors=DISCARD)

    strength =  (events[0]['args']['strength'])
    print ( round( Web3.from_wei(strength, 'ether')))


    



conexec()