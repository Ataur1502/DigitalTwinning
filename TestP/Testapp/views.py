import cohere
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pyttsx3
from web3 import Web3
import json

co = cohere.Client("VLyhTLpjX91xeA8nj1YfZcSGiUmQUbE9tNFneh59") 
with open(r"E:\NLP\Test\experiment_storage.json", "r") as f:
    storage_data = json.load(f)
storage_address = storage_data["address"]
storage_abi = storage_data["abi"]
 # Replace with your key
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Replace with your Ganache URL

if web3.is_connected():
    accounts = web3.eth.accounts  # Correct way to get accounts
    account = accounts[0]  # First account
    print("Connected to blockchain. Using account:", account)
else:
    print("Failed to connect to blockchain")

 # Use first account from Ganache

storage_contract = web3.eth.contract(address=storage_address, abi=storage_abi)
@csrf_exempt
def process_voice(request):
    if request.method == "POST":
        voice_text = request.POST.get('voice_text', '')  # Extract form data properly

        if not voice_text:
            return JsonResponse({"error": "No voice text received"}, status=400)

        # Cohere API Call
        response = co.generate(
            model="command",
            prompt=f"{voice_text} Answer in one short sentence.",
            max_tokens=40,
            truncate="END"
        )
        ai_response = response.generations[0].text.strip()
        engine = pyttsx3.init()
        engine.say(ai_response)
        engine.runAndWait()

        return render(request,"titration.html",{"ai_response": ai_response})

    return render(request, "titration.html")
3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for testing, but secure it in production
def api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received Data:", data)  # Print received data for debugging

            roll_no = data.get("rollNo", "")
            v1 = int(data.get("v1", 0))
            v2 = int(data.get("v2", 0))
            m1 = int(data.get("m1", 0))
            m2 = int(data.get("m2", 0))
            status = data.get("status", "Pending")

            # Prepare transaction to store experiment data
            tx_hash = storage_contract.functions.storeExperiment(
                roll_no, v1, v2, m1, m2, status
            ).transact({'from': account})

            # Wait for the transaction receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f"Transaction successful! Receipt: {receipt}")

            return JsonResponse({"message": "Experiment stored successfully", "receipt": str(receipt)}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"error": f"Error storing experiment values: {str(e)}"}, status=500)

    elif request.method == "GET":
        try:
            roll_no = request.GET.get("rollNo", "")
            if not roll_no:
                return JsonResponse({"error": "Roll number is required"}, status=400)

            # Retrieve stored experiments from blockchain
            experiments = storage_contract.functions.getExperiments(roll_no).call()

            response_data = [
                {
                    "v1": exp[0],
                    "v2": exp[1],
                    "m1": exp[2],
                    "m2": exp[3],
                    "status": exp[4]
                } for exp in experiments
            ]

            return JsonResponse({"message": "Experiments retrieved", "data": response_data}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard") # Redirect to dashboard or home page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def titration(request):
    return render(request,"titration.html")


from django.shortcuts import render
from .models import Experiment

def show_experiments(request):
    """Fetch and display all experiments."""
    roll_no = request.GET.get("roll_no")  # Optional filter by roll number
    if roll_no:
        experiments = Experiment.objects.filter(roll_no=roll_no)
    else:
        experiments = Experiment.objects.all()

    return render(request, "Asignned.html", {"experiments": experiments})

def completed(request):
    """Fetch and display all experiments."""
    roll_no = request.GET.get("roll_no")  # Optional filter by roll number
    if roll_no:
        experiments = Experiment.objects.filter(roll_no=roll_no)
    else:
        experiments = Experiment.objects.filter(status="completed")
       


    return render(request, "Completed.html", {"experiments": experiments})
def pending(request):
    """Fetch and display all experiments."""
    roll_no = request.GET.get("roll_no")  # Optional filter by roll number
    if roll_no:
        experiments = Experiment.objects.filter(roll_no=roll_no)
    else:
        experiments = Experiment.objects.filter(status="pending")
        


    return render(request, "Pending.html", {"experiments": experiments})
def ytb(request):
    """Fetch and display all experiments."""
    roll_no = request.GET.get("roll_no")  # Optional filter by roll number
    if roll_no:
        experiments = Experiment.objects.filter(roll_no=roll_no)
    else:
        experiments = Experiment.objects.filter(status="yet to begin")
        


    return render(request, "ytb.html", {"experiments": experiments})
