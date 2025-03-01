from web3 import Web3
import solcx
import json

# 1️⃣ Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("✅ Connected to Ganache")
else:
    print("❌ Connection failed")
    exit()  # Stop execution if not connected

# 2️⃣ Get the first Ganache account
account = web3.eth.accounts[0]

# 3️⃣ Install and Set Solidity Version
solcx.install_solc('0.8.0')
solcx.set_solc_version('0.8.0')

# 4️⃣ Read and Compile Solidity Contract
with open("ExperimentStorage.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = solcx.compile_source(
    contract_source_code, 
    output_values=["abi", "bin"]
)

contract_id, contract_interface = compiled_sol.popitem()

# 5️⃣ Deploy the Contract
ExperimentContract = web3.eth.contract(
    abi=contract_interface['abi'], 
    bytecode=contract_interface['bin']
)

tx_hash = ExperimentContract.constructor().transact({'from': account})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# 6️⃣ Get Contract Address
contract_address = tx_receipt.contractAddress
print(f"✅ Contract deployed at: {contract_address}")

# 7️⃣ Save Contract ABI & Address
contract_info = {
    "abi": contract_interface['abi'],
    "address": contract_address
}

with open("experiment_storage.json", "w") as f:
    json.dump(contract_info, f)

print("✅ Contract ABI & Address saved in `experiment_contract.json`")
