import streamlit as st
from bot.ai_bot import AIBot

MENSAGENS_EXEMPLO = [
    ('assistant', 'Tudo bem?')
]

def pagina_chat():
  st.header('🤖Bem-vindo ao Chatbot RTrainers', divider=True)
  ai_bot = AIBot()

  mensagens = st.session_state.get('mensagens', MENSAGENS_EXEMPLO)
  for mensangem in mensagens:
      chat = st.chat_message(mensangem[0])
      chat.markdown(mensangem[1])

  input_usuario = st.chat_input('Digite sua mensagem')
  if input_usuario:
    with st.spinner('🤔 Processando sua pergunta...'):
      mensagens.append(('user', input_usuario))
      response_message = ai_bot.invoke(
          history_messages=mensagens,
          question=input_usuario,
      )
      mensagens.append(('assistant', response_message))
      st.session_state['mensagens'] = mensagens
      st.rerun()


def main():
    pagina_chat()


if __name__ == '__main__':
    main()