# IACC
My iacc (Intelligent Artificial Call Center) is a proof-of-concept project that integrates several AI technologies to simulate an intelligent outbound call center. It is capable of making real-time calls, speaking with customers, understanding their responses, and replying intelligently using natural voice synthesis — all in an automated flow.

## Features
- Outbound Call Bot Flow:
  1. Call Handling: Uses Twilio to initiate real phone calls and manage live audio streams.
  2. Text-to-Speech (TTS): Converts predefined scripts and dynamic AI responses into natural-sounding voice using ElevenLabs.
  3. Speech-to-Text (STT): Transcribes real-time customer responses using OpenAI Whisper.
  4. Natural Language Processing (NLP): Interprets the customer's intent and generates dynamic responses using GPT-4-turbo from OpenAI.
  5. Conversational Loop: The AI continuously listens, processes, and responds, maintaining a natural back-and-forth conversation.
- Modular Backend:
  - Built with FastAPI (Python) for speed, scalability, and easy integration of AI and telecom services

## Technologies Used
### Core AI Tools
- NLP: OpenAI GPT-4-turbo
- TTS: ElevenLabs
- STT: OpenAI Whisper

### Telephony
- Twilio: Outbound call initiation and media handling

### Backend
- Python 3.11+
- FastAPI: API framework
- Uvicorn: ASGI server

## Setup
### Create and Activate Virtual Environment
```bash
# Create a virtual environment (you can change 'aienv' to any name)
python3 -m venv ~/venvs/aienv

# Activate the virtual environment
source ~/venvs/aienv/bin/activate

# To list all virtual environments
ls ~/venvs

# To check installed packages in current env
ls ~/venvs/aienv/bin

# To deactivate when finished
deactivate
   ```
### Install Dependencies
```bash
pip install fastapi uvicorn openai twilio
# You can add others as needed, for example:
pip install python-dotenv requests
   ```
Don’t forget to install the SDKs for the services you're using (e.g., openai, twilio, etc.).

## Run the Project
```bash
# From the root of your project
uvicorn main:app --reload
   ```
Make sure the file where your FastAPI app is declared is called main.py, or modify the command accordingly.

## Future Improvements
- First considerations (high priority)
  - CRM integration: Connect with tools like Make or Zapier to send data to a Google Sheets document as a CRM prototype, facilitating lead tracking and management.
  - Outbound call infrastructure: Optimize integration with Twilio and its webhooks to efficiently manage the call flow and real-time responses.
  - Call and transcription logging: Store conversations in text format to enable post-call analysis, error detection, and continuous improvement of the conversational model.

- Second considerations (medium priority)
  - Advanced conversational flow management: Implement robust logic to handle conversational states (start, interaction, end) and maintain contextually coherent responses based on the user’s intent.
  - Error and interruption handling: Design strategies to allow the bot to recover if the user says something unexpected, remains silent, or deviates from the conversation.
  - Latency optimization: Reduce response times between conversation turns by improving performance in the STT → NLP → TTS pipeline, ensuring a smooth and natural call experience.
   
## Contributions
Contributions are welcome. If you wish to improve the project, please fork it and submit a pull request.

## Contact
For questions or suggestions, you can contact me at [ezioeg@gmail.com].
