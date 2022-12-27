!pip install discord

import discord
import requests
import asyncio

# Substitua "TOKEN" pelo token do seu bot
TOKEN = "seu toke aqui"

# Substitua "CHANNEL_ID" pelo ID do canal no qual deseja enviar as notificações
CHANNEL_ID = "seu channel id aqui"

# Crie uma instância da classe Intents com os eventos que o seu bot deve ser capaz de processar
intents = discord.Intents.default()
intents.members = True  # Permite que o bot veja os membros de um servidor+

# Crie uma instância da classe Intents com as intenções que você deseja habilitar
intents = discord.Intents(members=True, guilds=True)

# Crie uma instância do cliente do Discord com as intenções habilitadas
client = discord.Client(intents=intents)

# Use o evento "on_ready" para verificar se o bot está funcionando corretamente
@client.event
async def on_ready():
    print("Bot pronto!")

# Defina a função que envia as notificações de jogos gratuitos
async def send_free_games_notification():
    # Faça uma requisição à API IsThereAnyDeal para obter a lista de jogos gratuitos
    url = "https://api.isthereanydeal.com/v02/game/list/?key=suakeyaqui&country=BR&type=free"
    response = requests.get(url)
    data = response.json()

    # Filtre a lista de jogos para incluir apenas os jogos das plataformas escolhidas
    games = [game for game in data["data"] if "steam" in game["platforms"] or "epic" in game["platforms"] or "gog" in game["platforms"] or "origin" in game["platforms"] or "prime" in game["platforms"]]

    # Se não houver jogos gratuitos, encerre a função
    if not games:
        return
        

    # Crie a mensagem de notificação com a lista de jogos gratuitos
    message = "Jogos gratuitos disponíveis:\n"
    for game in games:
        message += f"- {game['title']}\n"

    # Encontre o canal no qual deseja enviar a notificação
    channel = discord.utils.get(client.get_all_channels(), id=CHANNEL_ID)

    # Envie a mensagem para o canal
    await channel.send(message)

# Inicie o bot
await client.start(TOKEN)
