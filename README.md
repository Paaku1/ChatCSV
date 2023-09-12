# ChatCSV - A Streamlit Application for Querying CSV Files with OpenAI GPT-3


ChatCSV is a user-friendly web application that utilizes OpenAI's GPT-3 language model and Streamlit to query CSV files from natural language instructions. This project simplifies the process of creating CSV data by allowing users to interact with a chatbot-like interface, providing instructions in plain English and receiving well-formatted CSV files in response.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Getting Started

ChatCSV is designed to be easy to set up and use. Follow the steps below to get started:

### Prerequisites

Before you can run ChatCSV, ensure you have the following prerequisites installed:

- Python 3.X
- pip (Python package manager)
- OpenAI API key (Sign up at [OpenAI](https://beta.openai.com/signup/) if you don't have one)

### Installation

1. Clone the ChatCSV repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/chatCSV.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chatCSV
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure your OpenAI API key:

   Create a `.env` file in the project directory and add your API key:

   ```
   OPENAI_API_KEY=your-api-key-here
   ```

7. Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

The ChatCSV application should now be running locally and accessible in your web browser.

## Usage

1. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).

2. You will be greeted with the ChatCSV interface, which looks like a chatbot.

3. Start a conversation by typing your instructions in plain English. For example:

   ```
   Create a CSV file with columns: Name, Age, Email
   Add the following data:
   John Doe, 30, john@example.com
   Jane Smith, 28, jane@example.com
   ```

4. The chatbot will respond with a message indicating that the CSV file has been generated.

5. Download the generated CSV file by clicking the provided link.

## Contributing

We welcome contributions to improve ChatCSV. To contribute, follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them with descriptive commit messages.

5. Push your changes to your forked repository on GitHub.

6. Create a pull request to the main ChatCSV repository.

We appreciate your contributions!

---
