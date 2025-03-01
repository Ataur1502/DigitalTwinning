from web3 import Web3

# Connect to Ganache (Make sure Ganache is running)
ganache_url = "HTTP://127.0.0.1:7545"  # Update if needed
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Verify connection
if web3.is_connected():
    print("Connected to Ganache ✅")
else:
    print("Failed to connect to Ganache ❌")
    exit()

# Contract details
contract_address = "0xB7E16659f68852FF1811e1b5170ce94b35235FdE"  # Your deployed contract address

# ABI from your contract
contract_abi = [
    {
        "inputs": [
            {"internalType": "string", "name": "rollNo", "type": "string"}
        ],
        "name": "getExperiments",
        "outputs": [
            {
                "components": [
                    {"internalType": "string", "name": "description", "type": "string"},
                    {"internalType": "enum ExperimentsAssignment.Status", "name": "status", "type": "uint8"}
                ],
                "internalType": "struct ExperimentsAssignment.Experiment[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Load contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Define the roll number to retrieve experiments
roll_no = "12CHEM001"

# Fetch experiments for the given roll number
experiments = contract.functions.getExperiments(roll_no).call()

# Mapping Status Codes to Readable Text
Status = {0: "Not Started", 1: "Pending", 2: "Completed"}

# Display the retrieved experiments
if experiments:
    print(f"\nExperiments for Roll No: {roll_no}")
    for i, exp in enumerate(experiments):
        print(f"{i+1}. {exp[0]} - Status: {Status.get(exp[1], 'Unknown')}")
else:
    print(f"No experiments found for Roll No: {roll_no}")
