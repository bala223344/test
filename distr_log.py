from web3 import Web3
from web3.middleware import geth_poa_middleware
import web3
import time

import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="password",
  database = "skale"

)
 
cursorObject = dataBase.cursor()


print(dataBase)
  
def update_block(block,ts) :
    query = "UPDATE `block` SET `ts` = '{ts}', no='{block}' WHERE `block`.`id` = 1"
    cursorObject.execute(query)
    dataBase.commit()

def get_db_block() : 
    cursorObject.execute("SELECT no FROM block")
    result = cursorObject.fetchone()
    return result ['no']


def insert_mint(address,token_id,  block,ts) : 
    cursorObject.execute("INSERT INTO `mint_logs` (`address`, `token_id`,  `block`, `ts`) VALUES ('{address}', '{token_id}', '{block}', '{ts}');")
    return
    

def conexec() :
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.skalenodes.com/v1/green-giddy-denebola'))

    onchain_block = w3_instance.eth.get_block('latest')

    start_block = get_db_block()
    end_block = start_block + 999
    

    if (end_block > onchain_block) :
        return





    logs = w3_instance.eth.get_logs(
        {
            "fromBlock": start_block,
            "toBlock": end_block,
            "address": "0xB4F39D20de49EE86c1d880B1b236684a5F875a87",
            "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"],
        },
    )

    prev_block = 0
    ts = 0

    print ('--length')
    print (length(logs))
    #no tx found..
    if length(logs) == 0: 
        update_block(onchain_block, time.time())
        return

    for tx in logs:
        #print (tx)
        #print (tx['blockNumber'])
        token_id =  Web3.to_int(tx['topics'][3])
        address = Web3.to_hex(tx['topics'][2])
        #skip everything
        if (prev_block == tx['blockNumber']):
            pass
        else : 
            block = w3_instance.eth.get_block(tx['blockNumber'])
            ts = block['timestamp']
            prev_block = tx['blockNumber']
            update_block(prev_block, ts)
        
        insert_mint(address, token_id, prev_block, ts)
        print ("---")
    

       # print ("wwwferer")
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