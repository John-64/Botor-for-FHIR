# Botor 🩺
There is a repository for my chat-bot project. The application, wrote in Python, answer to a human question using the FHIR resources taked from a [HAPI FHIR Test Server](https://hapi.fhir.org/).

## Requirements 📝
- Install [Docker](https://www.docker.com/products/docker-desktop/);
- Download the project Zip and extract it;
- Download the LLM of your choice (check that it is compatible with Llama).

## Instruction 📖
1. Start the Docker application
2. Put the model.gguf into the "model" folder, inside the Botor project
3. Edit the config.JSON with your API Key and the name of your LLM
4. Open the terminal and go in the located project folder
5. Then run this two commands: 
  - docker build -t botor .
  - docker run --ulimit memlock=-1:-1 -it -p 9000:5000 --name botor -d botor

Now you can check if everything is ok going to the docker desktop app and check the images and the container. If everything is ok the contiainer have as status "Running" and we can use the Botor app reaching the localhost (localhost:9000 in this case).
    
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
