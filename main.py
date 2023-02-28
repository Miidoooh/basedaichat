import telegram
import openai

# Set up Telegram bot
bot = telegram.Bot(BOT_TOKEN='5880966736:AAEbyHifSR8jy8uFmcvdactmzNZf8XpOSqQ')

# Set up OpenAI API
openai.api_key = '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'

# Handle incoming messages from Telegram
def handle_message(update, context):
    # Get the user's message
    user_message = update.message.text

    # Check if the message is a command
    if user_message.startswith('/'):
        # Handle the command
        if user_message.startswith('/based'):
            # Get the user's message without the command
            user_message = user_message.replace('/based', '', 1).strip()

            # Send the user's message to the ChatGPT API
            response = openai.Completion.create(
                engine='davinci',
                prompt=user_message,
                max_tokens=1024,
                temperature=0.7,
            )

            # Get the AI-generated text from the response
            ai_message = response.choices[0].text

            # Send the AI-generated text back to the user
            context.bot.send_message(chat_id=update.effective_chat.id, text=ai_message)
        else:
            # Unknown command
            context.bot.send_message(chat_id=update.effective_chat.id, text="Unknown command. Please use /based to talk to the AI.")
    else:
        # Unknown message
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please use /based to talk to the AI.")

# Set up webhook to receive updates from Telegram
updater = telegram.ext.Updater(BOT_TOKEN='5880966736:AAEbyHifSR8jy8uFmcvdactmzNZf8XpOSqQ', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the Telegram bot
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
