
import openai
import streamlit as st


def chat_with_bot(conversation_history):
    message_placeholder = st.empty()
    full_response = ""
    # Send the prompt to OpenAI's chat-based model (e.g., gpt-3.5-turbo, gpt-4)
    for response in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]}
                    for m in conversation_history],
        stream = True, # for lively writing
        ):
        # get content in response
        full_response += response.choices[0].delta.get("content", "")
        # Add blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "|")

    # Return the response
    return full_response, message_placeholder

# create a Gradio interface
def create_streamlit_interface():

    st.title("GPT based Conversational AI bot")

    # Display the chat message
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.text_input("What's up?"):
        # add user to chat history
        st.session_state.messages.append({"role": "user",
                                           "content": prompt})
        # display the user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display the bot response
        with st.chat_message("assistant"):
            # Simulate the stream of responses with milliseconds delay
            full_response, message_placeholder = chat_with_bot(st.session_state.messages)
            message_placeholder.markdown(full_response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    

if __name__ == "__main__":
    create_streamlit_interface()
