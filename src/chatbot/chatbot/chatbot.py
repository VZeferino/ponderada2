#! /bin/env python3

import re
from time import sleep

# Dicionário de intenções
intent_patterns = {
    'goto_pattern': re.compile(r'Vá para (.*)'),
    'goto_alt_pattern': re.compile(r'Dirija-se ao (.*)'),
    'goto_alt2_pattern': re.compile(r'Me leve para (.*)'),
}

# Dicionário de ações
def go_to_location(location):
    print(f"Entendido, devo ir para {location}")
    sleep(1)
    print(f"Andando...")
    sleep(2)
    print(f"Chegando no meu destino: {location}")
    sleep(3)
    print(f"Chegamos!")
    sleep(1)

    if location == 'banheiro':
        print("Já pode mijar!")
        sleep(1)

action_mapping = {
    'goto_pattern': go_to_location,
    'goto_alt_pattern': go_to_location,
    'goto_alt2_pattern': go_to_location,
}

def process_intent(user_input):
    for intent, pattern in intent_patterns.items():
        match = pattern.match(user_input)
        if match:
            return intent, match.group(1)
    return None, None

def execute_action(intent, location):
    if intent in action_mapping:
        action = action_mapping[intent]
        action(location)
        return True
    return False

def main():
    # Mensagem inicial do chatbot
    print("Bem-vindo ao Chatbot do Vitor!")
    print("Me diga, para onde quer que eu vá no Inteli?")

    user_input = input(">> ")
    intent, location = process_intent(user_input)
    if intent:
        success = execute_action(intent, location)
        if success:
            print('Meu trabalho foi concluído. Adeus!')
        else:
            print('Ação não reconhecida.')
    else:
        print('Comando não compreendido.')

if __name__ == '__main__':
    print("Bem-vindo ao Chatbot do Vitor!")
    print("Me diga, para onde quer que eu vá no Inteli?")
    main()