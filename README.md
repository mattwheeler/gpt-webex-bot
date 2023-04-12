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
    python webex_wiz_bot.py
    ```
 ## Deploy the Flask App
 You can deploy the Flask application to a web server like Heroku or use a tool like ngrok to expose your local server to the internet.

### Using ngrok:

1. Install ngrok from https://ngrok.com/download and follow the instructions to set it up.
2. Run your Flask application: `python webex_wiz_bot.py`
3. In a separate terminal, run ngrok to expose your Flask app on port 8080: `./ngrok http 8080`
4. Copy the public URL provided by ngrok (e.g., `https://yoursubdomain.ngrok.io`).

### Using Heroku:

1. Install the Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli) and sign up for a Heroku account.
2. Log in to Heroku using the CLI: `heroku login`
3. Create a new Heroku app: `heroku create your-app-name`
4. Add a file named `Procfile` in your project folder with the following content: ```web: python webex_wiz_bot.py```
5. Add a file named `requirements.txt` in your project folder with the following content:
```
Flask
openai
requests
```
6. Initialize a Git repository, commit your changes, and deploy to Heroku:
7. Copy your app's URL (e.g., `https://your-app-name.herokuapp.com`).

Finally, create a Webhook in Webex:

1. Go to https://developer.webex.com/docs/api/v1/webhooks/create.
2. Authorize with your Webex account and provide your Webex access token.
3. In the "Request" section, set the following values:
   - `name`: "Webex Wiz Bot"
   - `targetUrl`: The public URL from ngrok or Heroku (e.g., `https://yoursubdomain.ngrok.io/webhook` or 
   `https://your-app-name.herokuapp.com/webhook`)
   - `resource`: "messages"
   - `event`: "created"
4. Click "Run" to create the webhook.

Now your bot should be up and running. Users can mention the bot using "@webex_wiz_bot" followed by 
their prompt in a Webex Teams room, and the bot will respond with the generated answer.

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
