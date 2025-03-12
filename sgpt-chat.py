import subprocess
import json
import time
# from azure.identity import DefaultAzureCredential
# from azure.core.exceptions import AzureError
# from azure.core.pipeline.transport import HttpRequest
# from azure.core.pipeline import PipelineClient

# Microsoft Purview details
# PURVIEW_ACCOUNT_NAME = "your-purview-account"
# PURVIEW_ENDPOINT = f"https://{PURVIEW_ACCOUNT_NAME}.purview.azure.com"

# # Initialize Azure authentication
# credential = DefaultAzureCredential()

# # Create an HTTP client for interacting with Purview API
# client = PipelineClient(base_url=PURVIEW_ENDPOINT, credential=credential)

LOG_FILE = "sgpt_logs.json"

def get_sgpt_response(prompt):
    """Send a prompt to ShellGPT and capture the response."""
    try:
        result = subprocess.run(
            ["sgpt", prompt], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def log_prompt_response(prompt, response):
    """Log the prompt and response into a JSON file."""
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "prompt": prompt,
        "response": response
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# def send_to_purview(prompt, response):
#     """Send prompt and response to Microsoft Purview."""
#     try:
#         data = {
#             "name": f"SGPT_Interaction_{int(time.time())}",
#             "typeName": "custom_sgpt_log",  # Define this type in Purview
#             "attributes": {
#                 "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
#                 "prompt": prompt,
#                 "response": response
#             }
#         }

#         # Create an HTTP request
#         request = HttpRequest("POST", f"{PURVIEW_ENDPOINT}/catalog/api/atlas/v2/entity", json=data)

#         # Send request to Microsoft Purview
#         response = client.send_request(request)

#         if response.status_code == 200 or response.status_code == 201:
#             print("Data successfully sent to Microsoft Purview.")
#         else:
#             print(f"Failed to send data: {response.status_code} - {response.text}")

#     except AzureError as e:
#         print(f"Azure Error: {str(e)}")
#     except Exception as e:
#         print(f"Error: {str(e)}")

# User interaction loop
while True:
    user_prompt = input("\nEnter your prompt (or type 'exit' to quit): ")
    if user_prompt.lower() == "exit":
        print("Exiting ShellGPT interaction.")
        break

    response = get_sgpt_response(user_prompt)
    print(f"\nSGPT Response:\n{response}")

    log_prompt_response(user_prompt, response)
    print("Response logged successfully.")

    # send_to_purview(user_prompt, response)
