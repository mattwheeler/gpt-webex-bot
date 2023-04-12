 # Webex Wiz

 Webex Wiz is a GPT AI-powered virtual assistant bot for Webex Teams rooms. It provides quick and relevant responses 
 to user prompts, helping users to get information and insights directly in their Webex Teams rooms.

 ## Features

 - GPT AI-powered responses
 - Easy integration with Webex Teams rooms
 - Responds to user prompts when mentioned by username

 ## Setup and Installation

 1. Clone this repository:
    ```
    git clone https:github.com/yourusername/webex-wiz.git
    cd webex-wiz
    ```

 2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

 3. Create an `.env` file in the root directory of the project and add your OpenAI API key and Webex access token:
    ```
    OPENAI_API_KEY=<your_openai_api_key>
    WEBEX_ACCESS_TOKEN=<your_webex_access_token>
    ```

 4. Replace `<your_openai_api_key>` and `<your_webex_access_token>` with your respective API keys.

 5. Run the Flask app:
    ```
    python app.py
    ```

 ## Usage

 Once the Webex Wiz bot is deployed, users can interact with it by mentioning the bot's username, @webexwiz, 
 followed by their prompt in the Webex Teams room where the bot is assigned. The bot will process the prompt 
 using the GPT AI API and respond with an appropriate message in the same Webex channel.

 For example, a user can type:

 ```
 @webexwiz Can you provide a brief history of Webex?
 ```

 The Webex Wiz bot will process the prompt and respond with relevant information in the Webex channel.

 ## License

 This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
