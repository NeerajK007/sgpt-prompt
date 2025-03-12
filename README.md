# sgpt-prompt

# Interacting with ShellGPT via Python

This project includes a Python script, `sgpt-chat.py`, that enables you to interact with ShellGPT (powered by Ollama) from the command line.

## Prerequisites

* **Python 3:** Ensure you have Python 3 installed on your system.
* **ShellGPT (via Ollama):** You must have ShellGPT running via Ollama. (Refer to the main project documentation for Ollama installation and running ShellGPT).
* **Microsoft Purview (Optional):** If you intend to use the Microsoft Purview integration, ensure you have the necessary credentials and setup configured.

## Usage

1.  **Installation (if not already done):** Follow the project's installation instructions to set up the environment.

2.  **Run the Script:** Open your terminal and navigate to the directory containing `sgpt-chat.py`. Execute the script using:

    ```bash
    python3 sgpt-chat.py
    ```

3.  **Provide a Prompt:** The script will prompt you to enter your query or request. Type your prompt and press Enter.

4.  **Receive the Response:** The script will send your prompt to ShellGPT and display the generated response in your terminal.

## Functionality

* **Prompt Input:** The script accepts user input from the command line as a prompt for ShellGPT.
* **ShellGPT Interaction:** It communicates with ShellGPT (running via Ollama) to generate a response based on the provided prompt.
* **Logging:** The script logs both the user's prompt and ShellGPT's response in a JSON file named `sgpt_logs.json`. This file is created or updated in the same directory as the script.
* **Microsoft Purview Integration (Optional):** If configured, the script sends the interaction data (prompt and response) to Microsoft Purview for auditing or compliance purposes.

## Example

```bash
python3 sgpt-chat.py
Enter your prompt: Explain the concept of recursion in programming.
ShellGPT: Recursion is a programming technique... (ShellGPT's response)