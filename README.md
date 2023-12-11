# Botor 🩺
There is a repository for my chat-bot project. The application, wrote in Python, answer to a human question using the FHIR resources taked from a [HAPI FHIR Test Server](https://hapi.fhir.org/).

## Requirements 📝
**For the moment the application has only been tested on MacBooks with ARM64 M1 processor. In the future i will release the version that can be used with docker.**

- MacBook with ARM64 CPU with at least 8GB RAM.
- [Docker](https://www.docker.com/products/docker-desktop/) 

## Instruction 📖
1. Start the Docker application
2. Download the .zip and extract it
3. Edit the config.JSON with at least your API Key
4. Open the terminal and go in the located folder
5. Run this command: docker build -t botor .
6. Then run this other command: 
Install this application:

- [Visual Studio Code](https://code.visualstudio.com/download) (Optional)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Large Language Model (you can download your favoirite LLM, but if you don't don't know any LLM, you could try [this](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) one.)

Run the terminal:
Edit the config.json file and then run the terminal:

- 
- docker run --name botor -p 8080:5000 -d botor

### Curiosity 🧐
The name "Botor" is the merge of "Bot" with the "Doctor".
