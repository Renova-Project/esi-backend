const sourceKnowledge = `

L'École nationale supérieure d'informatique (ESI), anciennement Institut national de formation en informatique (INI), est un établissement d'enseignement supérieur algérien formant des ingénieurs d’État en informatique. Elle est située à Oued Smar, à environ 15 km du centre-ville de la capitale Alger, en Algérie.
Créée sous le nom de Centre d’études et de recherche en informatique (CERI) sous la tutelle de l'ex-ministère de la planification et de l’aménagement du territoire, il a été renommée et placée sous la tutelle du ministère de l’enseignement supérieur et de la recherche scientifique en 1984.
Le CERI fut le premier centre de formation spécialisé en informatique d’Afrique. Il forma les premiers ingénieurs d’État, ingénieurs d’application et programmeurs d’Algérie et d’autres pays africains (Bénin, Cameroun, Gabon, Mali, Mauritanie, Sénégal, Tunisie, etc.).


DIRECTEUR , M. Mouloud KOUDIL , m_koudil@esi.dz  , +213 23 93 91 33 Poste 3008
SECRÉTAIRE GÉNÉRAL , M. Réda LOTMANI , +213 23 93 91 38 Poste 3092 , r_lotmani@esi.dz
DIRECTRICE ADJOINTE DE LA POST GRADUATION ET DE LA RECHERCHE SCIENTIFIQUE , Mme. Leila HAMDAD , +213 23 93 91 44 Poste 3141 , l_hamdad@esi.dz
DIRECTRICE ADJOINTE DES ETUDES , Mme Nassira CHERID ,+213 23 93 91 43 Poste 3006 ,n_cherid@esi.dz
Service Scolarité , Mme Naima LOUNES ,Poste 3084
Chef de département du second cycle ,Mr ANNANE Mohamed ,Poste 3089 ,m_anane@esi.dz

Chef de département du second cycle ,M. Rachid AIT AMRANE ,+213 23 93 91 46 Poste 3081 ,r_ait_amrane@esi.dz
Responsable des Stages ,M. Amar BALLA, Poste 3079
Service des diplômes ,diplome@esi.dz , Poste 3007
DIRECTEUR ADJOINT DES RELATIONS EXTÉRIEURES ET DE LA FORMATION CONTINUE ,M. Fouad DAHAK ,+213 23 93 91 31 Poste 3017 ,f_dahak@esi.dz
DIRECTEUR DE LA BIBLIOTHÈQUE ,M. Abderrahmane BELLAHRECHE ,+213 23 93 91 32 Poste 3059 , a_bellahreche@esi.dz
DIRECTION MOYENS INFORMATIQUES ,M. Daoud BOUMAZOUZA  ,+213 023 93 91 42 Poste 3052 ,d_boumazouza@esi.dz
LABORATOIRE DE RECHERCHE LCSI ,M. Djameleddine ZEGOUR ,+213 023 93 91 39
LABORATOIRE DE RECHERCHE LMCS ,Mme Karima BENATCHBA ,+213 023 93 91 30

* Club : Google Developer Groups
Date de créationSeptembre 2011
Président(e) Louggani Abderaouf
DomaineDéveloppement des produits technologiques
Nombre d'événements51
Evénements majeursDevFest


* Club : Sourire à l'innocence
Date de création2008
Président (e)Raniya KETFI
DomaineCharité
Nombre d'événements32
Evénements majeursArtDay / Qoufat Ramadhan / Collecte de vêtements

* Club Women Techmakers Algiers
Date de créationSeptembre 2017
Président(e)Asma HAIDOUR
DomaineFemme développeuse
Nombre d'événements24
Evénements majeursCode Quiz / Tech / Maths day / Women’s Day

* Club vert de l’ESI
Date de création2012
Président (e)Katia BENMOUHOUB
DomaineEnvironnement / Entreprenariat vert /Technologie verte
Nombre d'événements41
Evénements majeursFlash talk / Sahra it

* Club Etudiants En TIC
Date de création10 Novembre 2009
Président(e)Ahmed Mehdi BOUDJELLI
DomaineEntrepreneuriat
Nombre d'événements59
Evénements majeursSalon de l’emploi / Training Camp / Before S2EE

* Club scientifique de l'ESI
Date de création28 Avril 2008
Président(e)Wissal BOUZID
DomaineScientifique / Technologique
Nombre d'événements97
Evénements majeursHack IT / Leapfrog / Design Fest / Algeria Web Awards

* Club School of AI
Date de création2019
Président(e)Nassim Iheb AOUADJ
DomaineIntelligence artificielle
Nombre d'événements4
Evénements majeursAI2E / HAIck Algieria

* Club SHELLMATES
Date de création19/12/2011
Président(e)MABROUKI Mohamed Laid Malik
DomaineSécurité informatique
Nombre d'événements51
Evénements majeursHackINI / BSides Algiers / Hack Till S'hour

* Club CLUB ARTISTIQUE ET CULTUREL DE L’ESI
Date de création01 Décembre 2016
Président(e)Zakaria GOUTTEL
DomaineCulturel
Nombre d'événements54
Evénements majeursMovie Time Sing it

* Club Code and share
Date de création22 Février 2018
Président(e)Nour El Houda SAIDOUCHE
DomaineProgrammation
Nombre d'événements9
Evénements majeursKidsCanCode

` ;





import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";


const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null; // Variable to store user's message
const API_KEY = "sk-proj-Gz8uoyVCYi2NbeIqoX71T3BlbkFJGcWse1Bzza86P08kpIDP"; // Paste your API key here
const GOOGLE_API_KEY="AIzaSyCa0mvC9U89It-kGDjtfapHtXrNV-7GcMI" ;

const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);


function promptTemplate(query) {
    // Feed into an augmented prompt
    const augmentedPrompt = `Using the contexts below, answer the query.

    Contexts:
    ${sourceKnowledge}

    Query: ${query}`;
    
    return augmentedPrompt;
}

async function run(prompt) {
    // The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    return text;
  }

const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    // Create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<img src="esi_bot.svg" class="bot-img" alt="esi bot" width="48" height="48"><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return chat <li> element
}


// Access your API key (see "Set up your API key" above)


const handleChat = () => {
    userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
    if(!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        //const result =  gemini_model.generateContent(prompt);

        const messageElement = incomingChatLi.querySelector("p");
 
        console.log(userMessage)
        const my_prompt = promptTemplate(userMessage)
        //generateResponse(incomingChatLi);
        run(my_prompt).then(text => {
            messageElement.textContent = text;
            console.log(text);  // This will log the text returned from the run function
            }).catch(() => {
            messageElement.classList.add("error");
            messageElement.textContent = "Oops! Something went wrong. Please try again.";
            });

        //generateResponse(incomingChatLi);
    }, 600);
}

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window 
    // width is greater than 800px, handle the chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
document.body.classList.toggle("show-chatbot");
