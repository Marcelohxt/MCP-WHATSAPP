# Agente de WhatsApp para Serralheria

Este projeto implementa um agente de WhatsApp inteligente para uma serralheria, utilizando CrewAI para gerenciar conversas e automatizar o atendimento ao cliente.

## Funcionalidades

- Atendimento automático de clientes via WhatsApp
- Envio de orçamentos
- Compartilhamento de imagens de portões
- Agendamento de visitas técnicas
- Processamento inteligente de mensagens usando CrewAI

## Requisitos

- Python 3.8+
- Conta WhatsApp Business API
- OpenAI API Key (para o CrewAI)

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` com as seguintes variáveis:
```
OPENAI_API_KEY=sua_chave_aqui
WHATSAPP_API_TOKEN=seu_token_aqui
```

## Como Usar

1. Inicie o servidor:
```bash
python whatsapp_integration.py
```

2. Configure o webhook do WhatsApp Business API para apontar para:
```
http://seu-servidor:8000/webhook
```

## Estrutura do Projeto

- `serralheria_agent.py`: Implementação do agente principal usando CrewAI
- `whatsapp_integration.py`: Integração com a API do WhatsApp
- `requirements.txt`: Dependências do projeto

## Agentes

O sistema utiliza dois agentes principais:

1. **Atendente**: Responsável pelo atendimento inicial, fornecendo informações e imagens
2. **Vendedor**: Responsável por fechar negócios e agendar visitas técnicas

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests. 