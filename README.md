# Chatbot com PDFs usando Streamlit e LangChain

Este é um chatbot interativo que permite o **upload de arquivos PDF** e **responde perguntas** com base no conteúdo dos documentos. O projeto usa **Streamlit** para a interface, **LangChain** para o processamento de linguagem natural e **ChromaDB** para armazenamento vetorial.

---

## Funcionalidades

✅ **Upload de PDFs**  
✅ **Divisão e processamento de textos**  
✅ **Armazenamento vetorial com ChromaDB**  
✅ **Chat baseado em IA (OpenAI GPT-3.5)**  
✅ **Memória de conversa integrada**  

---

## Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** – Interface interativa
- **[LangChain](https://python.langchain.com/)** – Framework de IA
- **[OpenAI API](https://openai.com/)** – Modelo GPT-3.5
- **[ChromaDB](https://www.trychroma.com/)** – Banco de vetores para recuperação de informações
- **[Docker](https://www.docker.com/products/docker-hub/)** - Container para execução do projeto
---

## Estrutura do Projeto

```
chatbot
    📁 src
    │── main.py              # Executor do projeto
    │── 📂 backend
        │── main.py             # Configuração do chatbot e integração LangChain
        │── configs.py          # Configurações gerais do modelo e recuperação de dados
        │── 📂 arquivos      # PDFs carregados pelo usuário(serão removidos automaticamente após a finalização da interação)  
    │── 📂 frontend
       │── Home.py           # Interface do chatbot com Streamlit
    
│── README.md            # Documentação
│── .env                 # Chaves da API OpenAI (não incluídas no repositório)
│── docker-compose.yml   # Container para execução da imagem docker
│── Dockerfile           # Imagem docker do programa


```

---

## Como Rodar o Projeto

### Clone o Repositório  
```bash
git clone https://github.com/angelogagno/chatbot.git
cd chatbot
```

### Configure as Variáveis de Ambiente  
Crie um arquivo `.env` na raiz do projeto e adicione:  
```
OPENAI_API_KEY="sua-chave-aqui"
```

### Execute o Container
```bash
docker-compose up --build

```

Agora, basta **fazer o upload dos PDFs** e começar a conversar com seus documentos!  

---

## Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- 📧 Email: angelogagno@gmail.com
- 🔗 LinkedIn: [Angelo Gagno](https://www.linkedin.com/in/angelogagno)
- 🐙 GitHub: [Angelo Gagno](https://github.com/angelogagno)

---

Desenvolvido por [Angelo Gagno](https://github.com/angelogagno).

