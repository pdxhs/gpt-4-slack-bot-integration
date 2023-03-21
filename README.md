# gpt-4-slack-bot-integration



A Slack bot integration powered by OpenAI's GPT-4 model, with a significant portion of its code written by GPT-4 itself, designed to provide assistance and information on a wide range of topics, customizable for any community or workspace.

Features
--------

-   Responds to direct messages and mentions in channels
-   Handles conversation history in threads (up to 8192 tokens for the gpt-4 and gpt-4-0314 models)
-   Easily deployable to Heroku

Prerequisites
-------------

-   Python 3.x
-   Slack API tokens
-   OpenAI API key
-   Heroku, or similar, to enable 'Slack App Event Subscriptions > Events'

Installation and Setup
----------------------

Follow these steps to install and set up the GPT-4 Slack bot:

### A. Deploy to Heroku

1.  Clone the repository to your local machine by running `git clone https://github.com/your-username/your-repo-name.git`, replacing `your-username` and `your-repo-name` with the appropriate values.
2.  Navigate to your project's local directory using the terminal.
3.  Create a new Heroku app at <https://dashboard.heroku.com/new-app>.
4.  Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if you haven't already.
5.  Login to your Heroku account by running `heroku login` in your terminal.
6.  Connect your local repository to the Heroku app by running `heroku git:remote -a your-app-name`, replacing `your-app-name` with the name of your Heroku app.
7.  Deploy your project to Heroku by running `git push heroku master`.
8.  In the **Settings** tab of your Heroku app, click **Reveal Config Vars** and add the following variables:
    -   SLACK_BOT_TOKEN: Your Slack Bot User OAuth Token (you'll obtain this in Section C.3).
    -   OPENAI_API_KEY: Your OpenAI API key (you'll obtain this in Section F.2).
    -   PORT: The port you want the app to listen on (e.g., 3000).

### B. Create a Slack App

1.  Go to <https://api.slack.com/apps> and sign in to your Slack account.
2.  Click the **Create New App** button, enter a name for your app (e.g., 'gpt-4'), and choose a workspace to develop it in.
3.  Click **Create App**.

### C. Configure the Slack Bot

1.  In the **Features** section, click **OAuth & Permissions**.
2.  Scroll down to the **Scopes** section, and add the following bot token scopes: `app_mentions:read`, `channels:history`, `chat:write`, `users:read`, `im:history`, and `im:write`.
3.  Click **Install App** to install the bot to your workspace and obtain the **Bot User OAuth Token** (starts with `xoxb-`). Keep this token for later use.

### D. Set up Event Subscriptions

1.  In the **Features** section, click **Event Subscriptions**.
2.  Enable events and add a request URL that points to your deployed app's `/slack/events` endpoint (e.g., `https://your-app-name.herokuapp.com/slack/events`).
3.  Subscribe to the `message.channels` and `message.im` events.

### E. Set up Interactivity & Shortcuts

1.  In the **Features** section, click **Interactivity & Shortcuts**.
2.  Enable the "Allow users to send Slash commands and messages from the messages tab" option.

### F. Set up OpenAI API Key

1.  Sign up for an OpenAI API key at <https://beta.openai.com/signup/>.
2.  After signing up, go to <https://beta.openai.com/account/api-keys> to obtain your API key. Keep this key for later use.

### G. Set up Environment Variables

In the **Settings** tab of your Heroku app, click **Reveal Config Vars** and add the following variables:

-   `SLACK_BOT_TOKEN`: Your Slack Bot User OAuth Token from step B.3.
-   `OPENAI_API_KEY`: Your OpenAI API key from step E.2.
-   `PORT`: The port you want the app to listen on (e.g., 3000).

Usage
-----

To use the GPT-4 Slack bot, simply mention the bot in a channel or send a direct message to it. The bot will respond with helpful information related to your query.

Example interaction:


User: `@gpt-4 How can I set up a home automation project using open source hardware?`
gpt-4: 

Customization
-------------

You can customize the GPT-4 model and settings by modifying the `gpt-4.py` file. For example, you can change the temperature or max tokens for the model.

Completion vs. ChatCompletion
-----------------------------

`Completion` is used for earlier models like `text-davinci-003` and lower. It provides a single string as input and gets a single string as output. `ChatCompletion` is used for later models like GPT-4. It takes a series of messages as input and returns a generated message as output, allowing for more interactive and context-aware conversations.

Troubleshooting and Known Issues
--------------------------------

If you encounter any issues or need help, please report them by creating a new issue in the GitHub repository.

Contributing
------------

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

License
-------

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
----------------

-   [OpenAI](https://www.openai.com/) for providing the GPT-4 API
-   [Slack API](https://api.slack.com/) for enabling bot integration

Screenshots
-----------

*Image of the GPT-4 Slack bot in action in a channel*

* * * * *

