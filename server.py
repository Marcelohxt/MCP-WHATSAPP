from fastapi import FastAPI, Request
import uvicorn
from datetime import datetime
from typing import List, Dict

app = FastAPI()

# Armazenamento em memória para mensagens (simulando um chat)
messages_history: List[Dict] = []

def process_command(message: str) -> str:
    """Processa comandos e retorna uma resposta apropriada"""
    message = message.lower()
    
    if message == "hora":
        return f"Agora são: {datetime.now().strftime('%H:%M:%S')}"
    elif message == "data":
        return f"Hoje é: {datetime.now().strftime('%d/%m/%Y')}"
    elif message == "ajuda":
        return "Comandos disponíveis:\n- hora: mostra a hora atual\n- data: mostra a data atual\n- ajuda: mostra esta mensagem\n- historico: mostra últimas mensagens"
    elif message == "historico":
        if not messages_history:
            return "Nenhuma mensagem no histórico"
        return "\n".join([f"De: {msg['from']}, Mensagem: {msg['body']}" for msg in messages_history[-5:]])
    else:
        return f"Recebi sua mensagem: {message}\nUse 'ajuda' para ver os comandos disponíveis"

@app.post("/send-message")
async def send_message(request: Request):
    """Endpoint para simular o envio de mensagens"""
    try:
        data = await request.json()
        from_number = data.get("from", "usuario")
        message = data.get("message", "")

        # Salva a mensagem no histórico
        messages_history.append({
            "from": from_number,
            "body": message,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

        # Processa o comando e gera resposta
        resposta = process_command(message)
        
        # Salva a resposta no histórico
        messages_history.append({
            "from": "bot",
            "body": resposta,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

        return {
            "status": "success",
            "message": "Mensagem processada",
            "response": resposta,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }

    except Exception as e:
        print(f"\nErro ao processar mensagem: {str(e)}")
        return {"status": "error", "message": str(e)}

@app.get("/messages")
async def get_messages():
    """Retorna o histórico de mensagens"""
    return {
        "status": "success",
        "messages": messages_history
    }

@app.get("/")
async def root():
    """Rota de teste para verificar se o servidor está online"""
    return {
        "status": "online", 
        "message": "Servidor de teste está funcionando",
        "comandos_disponíveis": [
            "hora - mostra a hora atual",
            "data - mostra a data atual",
            "ajuda - lista todos os comandos",
            "historico - mostra últimas mensagens"
        ]
    }

if __name__ == "__main__":
    print("=== Iniciando servidor de teste ===")
    print("Servidor estará disponível em: http://localhost:3001")
    print("\nComandos disponíveis:")
    print("- hora: mostra a hora atual")
    print("- data: mostra a data atual")
    print("- ajuda: lista todos os comandos")
    print("- historico: mostra últimas mensagens")
    print("\nPara testar, envie POST para http://localhost:3001/send-message com:")
    print("""
    {
        "from": "seu_nome",
        "message": "seu_comando"
    }
    """)
    uvicorn.run(app, host="localhost", port=3001) 