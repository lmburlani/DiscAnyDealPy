# DiscAnyDealPy

O script a seguir é um exemplo de um bot para o Discord que usa a API IsThereAnyDeal para enviar notificações de jogos gratuitos para um canal específico. Ele foi escrito em Python usando a biblioteca do Discord.

Para usar esse script, é preciso fazer algumas configurações prévias:

    Substitua "TOKEN" pelo token do seu bot. Você pode obter o token do seu bot no portal do desenvolvedor do Discord em https://discord.com/developers/applications/.
    Substitua "CHANNEL_ID" pelo ID do canal no qual deseja enviar as notificações. Você pode obter o ID de um canal clicando com o botão direito no nome do canal e selecionando "Copiar ID".
    Substitua "suakeyaqui" na URL da API IsThereAnyDeal pelo sua chave de API. Você precisa se inscrever para obter uma chave de API em https://isthereanydeal.com/dev/docs/.
    
 Resumidamente, esse script faz o seguinte:

    Inicializa o bot do Discord, habilitando as intenções de ver os membros de um servidor.
    Quando o bot estiver pronto, ele irá buscar a lista de jogos gratuitos disponíveis na API IsThereAnyDeal, filtrando apenas os jogos das plataformas Steam, Epic, GOG, Origin e Prime.
    Se houver jogos gratuitos disponíveis, o bot enviará uma mensagem no canal especificado com a lista de jogos.
    Por fim, o bot é iniciado com o token fornecido.
