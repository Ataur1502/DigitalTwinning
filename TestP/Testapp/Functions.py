import json
from web3 import Web3

# Load contract details from deployment.json
with open(r"E:\NLP\Test\experiment_contract.json", "r") as f:
    deployment_data = json.load(f)
contract_address = deployment_data["address"]
contract_abi = deployment_data["abi"]

with open(r"E:\NLP\Test\experiment_storage.json", "r") as f:
    storage_data = json.load(f)
storage_address = storage_data["address"]
storage_abi = storage_data["abi"]



# Connect to Ganache
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connected
if web3.is_connected():
    print("Connected to Ganache ✅")
else:
    print("Failed to connect to Ganache ❌")

# Load smart contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
account = web3.eth.accounts[0]  # Use first account from Ganache

storage_contract = web3.eth.contract(address=contract_address, abi=contract_abi)


### **1️⃣ CREATE - Assign Experiment & Store Values**
def assign_experiment(roll_no, experiment_name):
    """Assign an experiment to a student."""
    try:
        tx = contract.functions.assignExperiment(roll_no, experiment_name).transact({'from': account})
        web3.eth.wait_for_transaction_receipt(tx)
        print(f"Experiment '{experiment_name}' assigned to {roll_no} ✅")
    except Exception as e:
        print(f"Error assigning experiment: {e}")

def store_experiment_values(roll_no, v1, v2, m1, m2, status):
    """Store experiment values in the blockchain."""
    try:
        tx = contract.functions.storeExperiment(
            roll_no, int(v1 * 100), int(v2 * 100), int(m1 * 100), int(m2 * 100), status
        ).transact({'from': account})
        web3.eth.wait_for_transaction_receipt(tx)
        print(f"Experiment values stored for Roll No: {roll_no} ✅")
    except Exception as e:
        print(f"Error storing experiment values: {e}")

### **2️⃣ READ - Retrieve Assigned Experiments & Stored Values**
def get_assigned_experiments(roll_no):
    """Retrieve all assigned experiments for a student."""
    try:
        experiments = contract.functions.getAssignedExperiments(roll_no).call()
        print(f"Assigned Experiments for Roll No {roll_no}: {experiments} ✅")
        return experiments
    except Exception as e:
        print(f"Error retrieving assigned experiments: {e}")

def get_experiment_values(roll_no):
    """Retrieve all stored experiment values for a student."""
    try:
        experiments = storage_contract.functions.getExperiments(roll_no).call()
        experiment_list = [
            {
                "v1": exp[0] / 100,
                "v2": exp[1] / 100,
                "m1": exp[2] / 100,
                "m2": exp[3] / 100,
                "status": exp[4]
            } for exp in experiments
        ]
        print(f"Experiment values for Roll No {roll_no}: {experiment_list} ✅")
        return experiment_list
    except Exception as e:
        print(f"Error retrieving experiment values: {e}")

### **3️⃣ UPDATE - Modify Experiment Status**
def update_experiment_status(roll_no, index, status):
    """Update the status of an experiment."""
    try:
        tx = contract.functions.updateExperimentStatus(roll_no, index, status).transact({'from': account})
        web3.eth.wait_for_transaction_receipt(tx)
        print(f"Experiment status updated for Roll No: {roll_no} ✅")
    except Exception as e:
        print(f"Error updating experiment status: {e}")

### **4️⃣ DELETE - Remove Assigned Experiment & Stored Values**
def delete_assigned_experiment(roll_no, experiment_name):
    """Remove an assigned experiment for a student."""
    try:
        tx = contract.functions.removeAssignedExperiment(roll_no, experiment_name).transact({'from': account})
        web3.eth.wait_for_transaction_receipt(tx)
        print(f"Experiment '{experiment_name}' removed for Roll No: {roll_no} ✅")
    except Exception as e:
        print(f"Error deleting assigned experiment: {e}")

def delete_experiment_values(roll_no, index):
    """Delete an experiment record (if supported in smart contract)."""
    try:
        tx = storage_contract.functions.deleteExperiment(roll_no, index).transact({'from': account})
        web3.eth.wait_for_transaction_receipt(tx)
        print(f"Experiment data deleted for Roll No: {roll_no} ✅")
    except Exception as e:
        print(f"Error deleting experiment values: {e}")
