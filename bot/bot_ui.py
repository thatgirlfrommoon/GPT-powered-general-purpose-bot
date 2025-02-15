
import openai
import streamlit as st


def chat_with_bot(user_input, conversation_history):
    # Send the prompt to OpenAI's chat-based model (e.g., gpt-3.5-turbo, gpt-4)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or use "gpt-4" for GPT-4 model
        messages=conversation_history + [{"role": "user", "content": user_input}],
        temperature=0.7,  # Control randomness of the response (higher = more random)
        max_tokens=150  # Limit on tokens per response
    )

    # Extract the assistant's reply
    print(response)
    bot_message = response['choices'][0]['message']['content']

    # Return the response
    return bot_message

# create a Gradio interface
def create_streamlit_interface():

    st.title("GPT based Conversational AI bot")
    # initial message to define assistant's behavion
    conversation_history = [{"role": "system",
             "content": "You are a helpful assistant."}]

    # Display the chat message
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Input box
    user_input = st.text_input("You: ")
    if user_input:
        # Get response from the chatbot
        bot_response = chat_with_bot(user_input, conversation_history)
        # update the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"You: {message['content']}")
        else:
            st.write(f"Assistant: {message['content']}")


if __name__ == "__main__":
    create_streamlit_interface()
