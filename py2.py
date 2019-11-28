# `pc_transaction.py` example
from bitcoin.rpc import RawProxy

p = RawProxy()

# Alice's transaction ID
txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

txid = input("Iveskite transakcijos ID\n")

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

input_sum = 0

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vin']:
    print("Gaunama " + output['txid'] + " info")
    dtx = p.decoderawtransaction(p.getrawtransaction(output['txid']))
    for dtxo in dtx['vout']:
        print("+ " + str(dtxo['value']))
        input_sum += dtxo['value']

output_sum = 0
for output in decoded_tx['vout']:
    output_sum += output['value']

print(str(input_sum) + " - " + str(output_sum) + " = " + str(input_sum - output_sum))
