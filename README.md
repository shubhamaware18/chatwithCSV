# ChatCSV: Chat with any CSV

Welcome to ChatCSV, a simple Streamlit app designed to help you gain insights from any CSV file. Whether you're exploring data or looking for quick analyses, this tool makes it easy to interact with your CSV data.

## SetUp

Follow these steps to set up and run ChatCSV on your local machine:

1. **Python Installation:** Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. **Clone the Repository:** Clone the ChatCSV repository to your local machine.

    ```bash
    git clone https://github.com/your-username/chat-with-csv.git
    ```

3. **Navigate to the Repository:** Change your current directory to the cloned repository.

    ```bash
    cd chat-with-csv
    ```

4. **Create and Activate a Virtual Environment:** Set up a virtual environment for ChatCSV and activate it.

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

5. **Install Dependencies:** Install the required packages listed in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

6. **Add OpenAI API Key:** Obtain an OpenAI API key and add it to the `.streamlit/secrets.toml` file.

7. **Run the Streamlit App:** Launch the ChatCSV app using the following command.

    ```bash
    streamlit run app.py
    ```

8. **Access the App:** Once the app is running, open your browser and go to [http://localhost:8501/](http://localhost:8501/). Upload your CSV file and start exploring!

Feel free to contribute, report issues, or suggest improvements. Happy chatting with ChatCSV!