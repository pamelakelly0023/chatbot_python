import telebot

TOKEN = "1315371458:AAHiWwiaLkSXGi7aO_BAU_5JvJln0a4_mx8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Olá, tudo bem?\nDigite o número correspondente a uma das opções a seguir:\n\n 1 - Promoções\n 2 - Fatura Digital\n 3 - Investimentos\n 4 - Central de Atendimento eletrônico")

@bot.message_handler(func=lambda m: True)
def teste(message):
    print("Mensagem:", message.text)
    chat_id = message.chat.id
    if message.text == "1":
        bot.send_message(chat_id, "HORA DA VIRADA \n\nPara participar é fácil:\nVocê ganha um número da sorte a cada R$10 reais em compras com o cartão Carrefour.\n"
         "São 8 prêmios de R$50 mil em barras de ouro!\n\nConfira mais informações em: https://www.carrefoursolucoes.com.br/promocao")
    elif message.text == "2":
        bot.send_message(chat_id, "Prezado Sr.(a) Cliente, faltam 5 dias para o vencimento da sua fatura no valor de R$350,00.\n\nCaso já queira efetuar o pagamento, acesse:\nhttps://www.carrefoursolucoes.com.br/web/guest/fatura-digital")
    elif message.text == "3":
        bot.send_message(chat_id, "Gostaria de começar a investir?\n\nO Banco Carrefour, em parceria com a Guide Investimentos, traz uma ótima opção de investimento com condições especiais para você que é nosso colaborador.\n\n"
        "1º passo: Abra sua conta, sem custo, de forma simples e digital\n2º passo: Invista no CDB Banco Carrefour com condições especiais\n3º passo: Conte com a assessoria para o que precisar!\n\n"
        "Para começar investir, acesse: https://www.guide.com.br/carrefour/")
    elif message.text == "4":
        bot.send_message(chat_id, "No atendimento eletrônico por telefone, você consulta informações sobre a sua fatura e sobre o seu Cartão Carrefour, além de poder solicitar seguros.\n\n"
        "Atendimento Eletrônico\n"
        "De segunda a sábado das 08h00 às 21h00\n\n"

        "São Paulo e Regiões Metropolitanas\n"
        "3004 2222\n\n"

        "Demais Localidades\n"
        "0800 718 2222")
    else:
        bot.reply_to(message, "Por favor, escolha uma opção válida:\n\n 1 - Promoções\n 2 - Fatura Digital\n 3 - Investimentos\n 4 - Central de Atendimento eletrônico")


bot.polling()