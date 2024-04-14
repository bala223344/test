from web3 import Web3
from web3.middleware import geth_poa_middleware
import web3
import time

import mysql.connector

dataBase = mysql.connector.connect(
  host ="127.0.0.1",
  user ="root",
  passwd ="hhz3Gq5jGNJcYs",
  database = "skale"

)
 
cursorObject = dataBase.cursor()



def update_block(block,ts) :

    cursorObject.execute("UPDATE `block` SET `ts` = %s, no=%s WHERE `block`.`id` = 1;", (ts, block))
    dataBase.commit()

def get_db_block() : 
    cursorObject.execute("SELECT no FROM block")
    result = cursorObject.fetchone()
    return result[0]


def insert_mint(address,token_id,  block,ts) :
    cursorObject.execute("INSERT INTO `mint_logs` (`address`, `token_id`,  `block`, `ts`) VALUES (%s, %s, %s, %s);", ((address), token_id,  block, ts))
    return
    

def conexec() :
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.skalenodes.com/v1/green-giddy-denebola'))

    onchain_block = w3_instance.eth.block_number

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
    print (len(logs))
    #no tx found..
    if len(logs) == 0:
        update_block(onchain_block, time.time())
        return

    for tx in logs:
        #print (tx)
        #print (tx['blockNumber'])
        token_id =  Web3.to_int(tx['topics'][3])
        hexstr = Web3.to_hex(tx['topics'][2])[26:66]
        print (hexstr)
        address = Web3.to_hex(hexstr=hexstr)
        #skip everything
        if (prev_block == tx['blockNumber']):
            pass
        else : 
            block = w3_instance.eth.get_block(tx['blockNumber'])
            ts = block['timestamp']
            prev_block = tx['blockNumber']
            update_block(prev_block, ts)
        
        insert_mint(address, token_id, prev_block, ts)
        print (token_id)

    


conexec()