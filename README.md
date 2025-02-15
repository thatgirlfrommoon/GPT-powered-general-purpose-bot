# get started with enviroment setup
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


# Python package
$ uv init 
$ uv run .\hello.py


# Install packaged
$ uv pip install -r requirements.txt

# Power up the bot
Set up the OpenAI API key in code before running it
$ uv run streamlit run .\bot\bot_ui2.py

*try another ui*
uv run streamlit run .\bot\bot_ui.py