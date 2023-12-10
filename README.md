# Botor 🩺
There is a repository for my chat-bot project. The application, wrote in Python, answer to a human question using the FHIR resources taked from a [HAPI FHIR Test Server](https://hapi.fhir.org/).

## Requirements 📝
- Machine with minimum 8GB of RAM

## Instruction 📖
Install this application:

- [Visual Studio Code](https://code.visualstudio.com/download) (Optional)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Large Language Model (you can download your favoirite LLM, but if you don't don't know any LLM, you could try [this](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) one.)

Run the terminal:
- docker build -t botor .
- docker run --name botor -p 8080:5000 -d botor

### Mac OS
Work in progress...

### Windows
Work in progress...

### Linux
Work in progress...


### Curiosity 🧐
The name "Botor" is the merge of "Bot" with the "Doctor".
