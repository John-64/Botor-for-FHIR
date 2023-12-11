# Botor 🩺
There is a repository for my chat-bot project. The application, wrote in Python, answer to a human question using the FHIR resources taked from a [HAPI FHIR Test Server](https://hapi.fhir.org/).

## Requirements 📝
- Install [Docker](https://www.docker.com/products/docker-desktop/);
- Download the LLM in the gguf format [here](https://huggingface.co/TheBloke) (check that it is compatible with Llama, i recommend [this](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) one).

## Instruction 📖
1. Start the Docker application
2. Download the project and extract it
3. Put the model.gguf into the "model" folder, inside the Botor project
4. Edit the config.JSON with your API Key and the name of your LLM.gguf
5. Open the terminal and go in the located project folder
6. Then run this two commands: 
  - docker build -t botor .
  - docker run --ulimit memlock=-1:-1 -it -p 9000:5000 --name botor -d botor

Now you can check if everything is ok going to the docker desktop app and check the images and the container. If everything is ok the contiainer have as status "Running" and we can use the Botor app reaching the showed in the Port(s) section (for example http://localhost:9000).

### Usefull commands 🛠️
- Run this command if you want to know what are the images avaible: docker images
- Run this command to see the stats (like cpu/ram used) of your container: docker stats botor

## Demo 🎥
Provide me the information of patient 30163
  
Provide me the observation of patient 30163 with code 8310-5 "Body temperature"
  
Provide me the observation of patient 30163 with code 3141-9 "Body weight Measured"

### Curiosity 🧐
The name "Botor" is the merge of "Bot" with the "Doctor".
