
import chainlit as cl
from my_agent.atm_agent import ATMVirtualAgent
from main import load_user_db


@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to the AI ATM! 💰").send()

@cl.on_message
async def handle_message(message: cl.Message)
    await cl.Message(content=f"You said: {message.content}").send()

if __name__ == '__main__':
    user_db = load_user_db()
    agent = ATMVirtualAgent(user_db)
    agent.load_chat_history()
    print("Welcome to the Virtual ATM!")
