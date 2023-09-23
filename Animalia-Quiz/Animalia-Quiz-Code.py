import pygame
import random
import time
# Inicialização do Pygame
pygame.init()

pygame.mixer.music.load('music/Scheherazadeop35.mp3')
pygame.mixer.music.play()

#efeitos sonoros
som_tecla = pygame.mixer.Sound('music/keypress-001.wav')
som_space = pygame.mixer.Sound('music/Accept.mp3')
win = pygame.mixer.Sound('music/Win sound.wav')
#plaud = pygame.mixer.Sound('music/aplausos.mp3')
enter = pygame.mixer.Sound('music/new mission 08.wav')
# Configurações da janela do jogo
largura_janela = 1200
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Animalia Quiz")
# Cores

pygame.time.delay(9500)

cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_verde = (0, 255, 0)

# Fontes
fonte_titulo = pygame.font.Font(None, 80)
fonte_dicas = pygame.font.Font(None, 40)
fonte_resposta = pygame.font.Font(None, 50)
fonte_pontuacao = pygame.font.Font(None, 50)
fonte_resumo = pygame.font.Font(None,24)


acertos = [
    {
        'nome': 'Elefante',
        'imagem': 'sprites/elefante.png',
        'resumo': "O elefante é o maior mamífero terrestre, encontrado em diversas regiões da África e da Ásia.\n \n Eles vivem em grupos sociais chamados de manadas, lideradas por uma fêmea mais velha. Os elefantes são conhecidos por sua inteligência, memória e habilidades emocionais. Eles desempenham um papel importante na manutenção do ecossistema das florestas, ajudando na dispersão de sementes e na criação de clareiras através da derrubada de árvores. Infelizmente, eles estão ameaçados devido à caça ilegal e à perda de habitat.",
        
    },
    {
        'nome': 'Leão',
        'imagem': 'sprites/Lion.png',
        'resumo': "O leão é um dos maiores felinos do mundo e é encontrado principalmente nas savanas da África. Os leões são animais sociais e vivem em grupos conhecidos como 'coalizões'. Os machos têm uma juba distintiva, que varia em tamanho e cor. As leoas são as principais caçadoras do grupo, enquanto os machos protegem o território. Os leões têm um papel crucial no ecossistema, controlando as populações de herbívoros e mantendo o equilíbrio nos ecossistemas das savanas.",
    },
    {
        'nome': 'Girafa',
        'imagem': 'sprites/giraffe.png',
        'resumo': 'A girafa é um animal elegante e alto, encontrado nas regiões da África subsaariana. Elas são os mamíferos terrestres mais altos e possuem um pescoço longo e pernas longas. As girafas são herbívoras e se alimentam principalmente das folhas das árvores acácias. Elas têm uma língua preênsil que é usada para arrancar as folhas dos galhos. As girafas vivem em grupos sociais chamados de ''manadas'' e têm um papel importante na dispersão de sementes e na poda de árvores, o que ajuda a promover a diversidade vegetal',
    },
    {
        'nome': 'Tigre',
        'imagem': 'sprites/Tiger.png',
        'resumo': 'O tigre é um felino de grande porte encontrado principalmente na Ásia. É um dos predadores mais poderosos do mundo e é conhecido por suas listras distintivas e pelagem alaranjada. Os tigres são solitários e têm um território amplo. Eles são caçadores habilidosos e podem saltar longas distâncias para capturar suas presas. Infelizmente, muitas subespécies de tigres estão ameaçadas de extinção devido à caça ilegal e à destruição do seu habitat.',
    },
    {
        'nome': 'pinguim',
        'imagem': 'sprites/Penguim.png',
        'resumo': 'Os pinguins são aves marinhas que vivem principalmente no Hemisfério Sul, especialmente na Antártida. Eles são conhecidos por sua aparência distintiva, com corpos esbeltos, asas curtas e pernas adaptadas para nadar. Os pinguins passam a maior parte de suas vidas na água, onde são excelentes nadadores. Eles se alimentam principalmente de peixes e crustáceos. Os pinguins são animais sociais e vivem em grandes colônias. Eles enfrentam ameaças como a perda de habitat e as mudanças climáticas.'
    },
    {
        'nome': 'Baleia',
        'imagem': 'sprites/Baleia.png',
        'resumo': 'As baleias são mamíferos marinhos encontrados em todos os oceanos do mundo. Elas são os maiores animais vivos e podem atingir tamanhos impressionantes. Existem diferentes espécies de baleias, incluindo a baleia azul, que é a maior de todas. As baleias têm adaptações especiais para a vida no mar, como as nadadeiras em forma de remo e o sopro característico. Elas se alimentam principalmente de pequenos organismos marinhos, como o krill. As baleias são animais migratórios e enfrentam ameaças como a caça e a poluição',
    },
    {
        'nome': 'Crocodilo',
        'imagem': 'sprites/crocodilo.png',
        'resumo': 'Os crocodilos são répteis semiaquáticos encontrados em regiões tropicais e subtropicais de todo o mundo. Eles têm corpos alongados, focinhos longos e mandíbulas poderosas com dentes afiados. Os crocodilos passam a maior parte do tempo na água, onde são excelentes nadadores e caçadores. Eles se alimentam de peixes, aves, mamíferos e até mesmo de outros répteis. Os crocodilos têm uma história que remonta aos tempos pré-históricos e são considerados animais ancestrais.'
    },
    {
        'nome': 'Panda',
        'imagem': 'sprites/Panda.png',
        'resumo': 'O panda é um mamífero nativo das regiões montanhosas da China. É conhecido por sua aparência adorável, com pelagem preta e branca distintiva. Os pandas são herbívoros e se alimentam principalmente de bambu. Eles têm adaptações especiais, como um polegar oponível que os ajuda a segurar o bambu. Os pandas são animais solitários e têm um território amplo. Eles estão ameaçados de extinção devido à perda de habitat e à baixa taxa de reprodução.'
    },
    {
        'nome': 'ornitorrinco',
        'imagem': 'sprites/ornitorrinco.png',
        'resumo': 'O ornitorrinco é um animal semiaquático nativo da Austrália. É um dos mamíferos mais incomuns do mundo devido às suas características únicas. O ornitorrinco tem um bico semelhante ao de um pato, patas com membranas semelhantes às de um castor e espinhos venenosos nas pernas traseiras. Eles são conhecidos por sua habilidade de nadar e cavar em busca de alimento. Os ornitorrincos são animais monotremados, o que significa que são mamíferos que põem ovos.'
    },
    {
        'nome': 'Golfinho',
        'imagem': 'sprites/golfinho.png',
        'resumo': 'Os golfinhos são mamíferos marinhos conhecidos por sua inteligência e comportamento brincalhão. Eles são encontrados em todos os oceanos do mundo e têm uma aparência distinta, com corpos alongados, barbatanas dorsais e um bico característico. Os golfinhos vivem em grupos sociais chamados de "cardumes" e se comunicam por meio de sons, como cliques e assobios. Eles são nadadores rápidos e ágeis, capazes de realizar acrobacias impressionantes. Os golfinhos têm um papel importante no ecossistema marinho e enfrentam ameaças como a pesca predatória e a poluição.'
    },
    {
        'nome': 'Coala',
        'imagem': 'sprites/Koala.png',
        'resumo': 'O coala é um marsupial arborícola encontrado na Austrália. Eles são conhecidos por sua aparência fofa, com pelagem densa e orelhas redondas. Os coalas são especializados em se alimentar de folhas de eucalipto, que fornecem a maior parte de sua dieta. Eles têm adaptações especiais, como garras afiadas e uma estrutura única no intestino, que lhes permite digerir as folhas tóxicas do eucalipto. Os coalas são animais solitários e têm um metabolismo lento. Eles estão ameaçados de extinção devido à perda de habitat e às doenças.'
    },
    {
        'nome': 'Gorila',
        'imagem': 'sprites/Gorila.png',
        'resumo': 'O gorila é um dos primatas mais conhecidos e é encontrado nas florestas tropicais da África Central. Eles são os maiores primatas vivos e têm uma aparência imponente, com um corpo musculoso e pelos escuros. Os gorilas vivem em grupos sociais chamados de troopas e são liderados por um macho dominante, conhecido como silverback. Os gorilas são herbívoros e se alimentam principalmente de folhas, frutas e brotos. Eles têm uma grande importância na dispersão de sementes e na manutenção da biodiversidade nas florestas.'
    },
    {
        'nome': 'Suricato',
        'imagem': 'sprites/suricato.png',
        'resumo': 'A suricata, também conhecida como "meerkat", é um pequeno mamífero encontrado nas regiões desérticas do sul da África. Elas são conhecidas por sua aparência fofa e por seu comportamento social complexo. As suricatas vivem em colônias e têm uma estrutura social bem definida, com indivíduos desempenhando diferentes papéis, como sentinela, caçador e cuidador dos filhotes. Elas se alimentam principalmente de insetos e pequenos vertebrados. As suricatas são animais muito ativos e têm uma comunicação vocal variada.'
    },
    {
        'nome': 'Papagaio',
        'imagem': 'sprites/papagaio.png',
        'resumo': 'Os papagaios são aves coloridas e inteligentes encontradas em várias partes do mundo, especialmente nas regiões tropicais. Eles são conhecidos por sua habilidade de imitar sons e vozes humanas. Os papagaios têm um bico curvo e forte, que é usado para quebrar sementes e se alimentar de frutas. Eles vivem em bandos sociais e se comunicam uns com os outros por meio de vocalizações. Os papagaios são animais ameaçados devido à captura ilegal para o comércio de animais de estimação e à destruição do habitat.'
    },
    {
        'nome': 'Jaguar',
        'imagem': 'sprites/jaguar.png',
        'resumo': 'O jaguar é um felino de grande porte encontrado nas florestas tropicais e subtropicais das Américas. É um dos predadores mais fortes e ágeis do continente. Os jaguares têm uma pelagem manchada e um corpo robusto. Eles são excelentes nadadores e caçadores, alimentando-se de uma variedade de presas, como capivaras, veados e peixes. Os jaguares têm um papel crucial na regulação das populações de presas e na manutenção do equilíbrio ecológico das florestas.'
    },
    {
        'nome': 'Urso_polar',
        'imagem': 'sprites/urso_polar.png',
        'resumo': 'O urso polar é uma espécie de urso encontrada nas regiões árticas do Hemisfério Norte. É o maior carnívoro terrestre e tem uma adaptação única para o frio extremo, com uma espessa camada de gordura e uma pelagem branca isolante. Os ursos polares são excelentes nadadores e passam a maior parte do tempo no gelo marinho em busca de presas, como focas. Infelizmente, o aquecimento global e o derretimento do gelo marinho estão ameaçando o habitat dos ursos polares.'
    },
    {
        'nome': 'Cobra',
        'imagem': 'sprites/cobra.png',
        'resumo': 'As cobras são répteis encontrados em todos os continentes, exceto na Antártida. Elas têm corpos alongados, sem patas, e se movem rastejando. Existem milhares de espécies de cobras, algumas venenosas e outras não. Elas têm mandíbulas flexíveis e podem engolir presas inteiras. As cobras desempenham um papel importante no controle de populações de roedores e outros animais. Algumas cobras têm venenos poderosos que são usados para caçar e se defender.'
    },
    {
        'nome': 'Águia',
        'imagem': 'sprites/aguia.png',
        'resumo': 'As águias são aves de rapina encontradas em várias partes do mundo. Elas são conhecidas por sua visão aguçada e por sua habilidade de voar em altas altitudes. As águias têm garras afiadas, bicos curvos e asas largas. Elas se alimentam principalmente de peixes, aves e pequenos mamíferos. As águias são símbolos de força e poder em muitas culturas e desempenham um papel importante no controle de populações de presas.'
    },
    {
        'nome': 'Búfalo',
        'imagem': 'sprites/bufalo.png',
        'resumo': 'O búfalo é um grande mamífero encontrado em várias partes do mundo, incluindo a África e a Ásia. Existem diferentes espécies de búfalos, como o búfalo-africano e o búfalo-asiático. Eles têm corpos robustos, chifres curvos e uma pelagem densa. Os búfalos são animais sociais e vivem em grupos chamados de manadas. Eles são herbívoros e se alimentam de capim e vegetação aquática. Os búfalos têm um papel importante no ecossistema, ajudando na dispersão de sementes e na criação de clareiras na vegetação.'
    },
    {
        'nome': 'Hipopótamo',
        'imagem': 'sprites/hipo.png',
        'resumo': 'O hipopótamo é um dos maiores mamíferos semiaquáticos e é encontrado em várias partes da África. Eles têm corpos volumosos, patas curtas e uma boca larga com dentes afiados. Os hipopótamos passam a maior parte do tempo em rios e lagos, onde se alimentam de vegetação aquática. Eles são animais sociais e vivem em grupos chamados de manadas. Os hipopótamos são considerados um dos animais mais perigosos da África e são responsáveis por um número significativo de mortes humanas todos os anos.'
    },
    {
        'nome': 'Rinoceronte',
        'imagem': 'sprites/rinoceronte.png',
        'resumo': 'O rinoceronte é um mamífero de grande porte encontrado em várias partes da África e da Ásia. Existem diferentes espécies de rinocerontes, como o rinoceronte-branco e o rinoceronte-negro. Eles têm corpos robustos, pele espessa e chifres distintivos. Os rinocerontes são herbívoros e se alimentam de vegetação. Infelizmente, eles estão ameaçados de extinção devido à caça ilegal por causa de seus chifres, que são valorizados na medicina tradicional e no mercado negro.'
    },
    {
        'nome': 'Lobo',
        'imagem': 'sprites/lobo.png',
        'resumo': 'O lobo é um mamífero carnívoro encontrado em várias partes do mundo, incluindo América do Norte, Europa e Ásia. Eles são conhecidos por sua inteligência e por sua estrutura social complexa, vivendo em grupos chamados de alcateias. Os lobos têm corpos ágeis, patas poderosas e mandíbulas fortes. Eles são excelentes caçadores e se alimentam principalmente de presas como veados e alces. Os lobos são animais muito vocais, usando uivos para se comunicar com outros membros da alcateia.'
    },
    {
        'nome': 'Zebra',
        'imagem': 'sprites/zebra.png',
        'resumo': 'A zebra é um mamífero herbívoro encontrado nas regiões da África. Ela é conhecida por sua pelagem listrada, que é única para cada indivíduo. As zebras vivem em grupos sociais chamados de manadas e têm um comportamento gregário. Elas se alimentam principalmente de capim e têm adaptações especiais, como dentes grandes e fortes, que são usados para pastar. As zebras têm um papel importante na manutenção do ecossistema das savanas, ajudando na dispersão de sementes e na criação de clareiras na vegetação.'
    },
    {
        'nome': 'Esquilo',
        'imagem': 'sprites/esquilo.png',
        'resumo': 'O esquilo é um pequeno roedor encontrado em várias partes do mundo, incluindo América do Norte, Europa e Ásia. Eles têm corpos ágeis, caudas longas e pelagem espessa. Os esquilos são conhecidos por sua habilidade de escalar árvores e por armazenar alimentos para o inverno. Eles se alimentam de uma variedade de alimentos, incluindo nozes, sementes e frutas. Os esquilos têm um comportamento territorial e são animais muito ágeis e rápidos.'
    },
    {
        'nome': 'Camelo',
        'imagem': 'sprites/camelo.png',
        'resumo': 'O camelo é um mamífero encontrado nas regiões áridas da África e da Ásia. Ele tem adaptações especiais para sobreviver em ambientes desérticos, como corcova e pés largos. Os camelos são conhecidos por sua habilidade de armazenar água e passar longos períodos sem beber. Eles são animais sociais e têm uma longa história de domesticação pelos seres humanos. Os camelos são usados como meio de transporte e para a produção de leite e carne.'
    },
]
        


# Variáveis do jogo
animais =  [   
        {'nome' : "Elefante" , "nivel": 1 , "dicas" : [
            "É um dos maiores animais terrestres.",
            "Possui uma tromba longa e flexível.",
            "Tem presas proeminentes."
        ]},
        {'nome' : "Leao" , "nivel": 2 , "dicas" :[
            'É conhecido como o "rei da selva".',
            'Possui uma juba ao redor do pescoço.',
            'É um felino que em sua maioria vive em grupos grandes.'
        ]},
        {'nome' : "Girafa" , "nivel": 3 , "dicas" :[
            'Tem um pescoço longo e pernas altas.',
            'Possui manchas em sua pelagem.',
            'Alimenta-se principalmente de folhas das árvores.'
        ]},
        {'nome' : "Tigre" , "nivel": 4 , "dicas" : [
            'É um felino de grande porte.',
            'Possui listras em sua pelagem.',
            'É um predador ágil e poderoso.'
        ]},
        {'nome' : "Pinguim" , "nivel": 5 , "dicas" : [
            'É uma ave que não voa.',
            'Vive principalmente nas regiões polares.',
            'Possui uma plumagem densa e impermeável.'
        ]},
        {'nome' : "Baleia" , "nivel": 6 , "dicas" : [
            'É um mamífero marinho de grande porte.',
            'Alimenta-se de plâncton e pequenos peixes.',
            'Pode emitir sons que são utilizados para se comunicar.'
        ]},
        {'nome' : "Crocodilo" , "nivel": 7 , "dicas" : [
            'É um réptil semiaquático.',
            'Possui um corpo alongado e mandíbulas fortes.',
            'Vive tanto em água doce como em água salgada.'
        ]},
        {'nome' : "Panda" , "nivel": 8 , "dicas" : [
            'É um mamífero de porte médio.',
            'Possui uma pelagem preta e branca característica.',
            'Alimenta-se principalmente de bambu.'
        ]},
        {'nome' : "Ornitorrinco" , "nivel": 9 , "dicas" : [
            'É um mamífero semiaquático.',
            'Possui bico similar ao de um pato.',
            'É conhecido por ser venenoso.'
        ]},
       
        {'nome' : "Golfinho" , "nivel": 10 , "dicas" : [
            'É um mamífero marinho conhecido por sua inteligência.',
            'Possui um corpo hidrodinâmico e nadadeiras.',
            'Emite sons por meio de um sistema chamado "ecolocalização".'
        ]},
        {'nome' : "Coala" , "nivel": 11 , "dicas" : [
            'É um marsupial arborícola.',
            'Alimenta-se principalmente de folhas de eucalipto.',
            'É nativo da Austrália.'
        ]},
        {'nome' : "Gorila" , "nivel": 12 , "dicas" : [
            'É um primata de grande porte.',
            'Possui uma musculatura robusta.',
            'Vive em grupos familiares.'
        ]},
        {'nome' : "Suricato" , "nivel": 13 , "dicas" : [
            'É um pequeno mamífero que vive em colônias.',
            'Possui uma pelagem acinzentada e listrada.',
            'É conhecido por sua postura ereta de vigilância.'
        ]},
        {'nome' : "Papagaio" , "nivel": 14 , "dicas" : [
            'É uma ave conhecida por sua capacidade de imitar sons.',
            'Possui penas coloridas e bico forte.',
            'É comumente mantido como animal de estimação.'
        ]},
        {'nome' : "Jaguar" , "nivel": 15 , "dicas" : [
            'É um felino encontrado nas Américas.',
            'Possui uma pelagem com manchas escuras em formato de roseta.',
            'É um excelente nadador.'
        ]},
        {'nome' : "Urso_polar" , "nivel": 16 , "dicas" : [
            'É um mamífero que vive no Ártico.',
            'Possui uma pelagem branca e densa.',
            'É adaptado para viver em climas frios.'
        ]},
        {'nome' : "Cobra" , "nivel": 17 , "dicas" :[
            'É um réptil sem patas.',
            'Movimenta-se rastejando.',
            'Algumas espécies são venenosas.'
        ]},
        {'nome' : "Aguia" , "nivel": 18 , "dicas" : [
            'É uma ave de rapina de grande porte.',
            'Possui visão aguçada e garras afiadas.',
            'É conhecida por seu voo majestoso.'
        ]},
        {'nome' : "Bufalo" , "nivel": 19 , "dicas" : [
            'É um mamífero de porte grande.',
            'Possui chifres curvos e robustos.',
            'Vive em grupos chamados de "manadas".'
        ]},
        {'nome' : "Hipopotamo" , "nivel": 20 , "dicas" : [
            'É um mamífero herbívoro semiaquático.',
            'Possui um corpo volumoso e boca larga.',
            'É conhecido por sua agressividade.'
        ]},
        {'nome' : "Rinoceronte" , "nivel": 21 , "dicas" : [
            'É um mamífero de grande porte.',
            'Possui um chifre na parte frontal do crânio.',
            'Vive principalmente em regiões de savana e floresta.'
        ]},
        {'nome' : "Lobo" , "nivel": 22 , "dicas" : [
            'É um mamífero carnívoro que vive em grupos sociais.',
            'Possui uma audição aguçada e olfato apurado.',
            'É conhecido por sua habilidade de comunicação vocal.'
        ]},
        {'nome' : "Zebra" , "nivel": 23 , "dicas" : [
            'É um mamífero herbívoro.',
            'Possui uma crina ereta e cauda comprida.',
            'Vive em grandes grupos chamados de manadas.'
        ]},
        {'nome' : "Esquilo" , "nivel": 24 , "dicas" : [
            'É um pequeno roedor.',
            'Possui cauda longa e peluda.',
            'Armazena alimentos em esconderijos para o inverno.'
        ]},
        {'nome' : "Camelo" , "nivel": 25 , "dicas" : [
            'É um mamífero adaptado para viver em desertos.',
            'Possui corcunda e patas largas.',
            'Pode passar longos períodos sem água.'
        ]
    }
    ]

nivel_atual = 1
pontuacao = 0
resposta = ""
recorde = 0


# Carregar imagens de plano de fundo
fundo_tela_inicial = pygame.image.load("sprites/Animalia.jpg")
fundo_tela_jogo = pygame.image.load("sprites/fundo2.jpg")
fundo_tela_acerto = pygame.image.load("sprites/Plano.jpeg")
#imagem_acerto = pygame.image.load(acertos['imagem']).convert_alpha()
# Função para exibir texto na tela
def exibir_texto(texto, fonte, cor, posicao):
    superficie_texto = fonte.render(texto, True, cor)
    janela.blit(superficie_texto, posicao)

# Função para exibir as dicas do animal
def exibir_dicas(animal, pontuacao):
    dicas = animal['dicas'][:2]  # Exibe apenas as duas primeiras dicas

    if nivel_atual <= animal['nivel']:
        dicas.append(animal['dicas'][2])  # Adiciona a terceira dica
        pontuacao_extra = float(pontuacao * 0.5)  # Pontuação extra para a terceira dica
        pontuacao -= pontuacao_extra

    posicao_dicas = (20, 140)
    for dica in dicas:
        exibir_texto("- " + dica, fonte_dicas, cor_branca, posicao_dicas)
        posicao_dicas = (posicao_dicas[0], posicao_dicas[1] + 30)
 
# Função para exibir a tela inicial
def exibir_tela_inicial():
    janela.blit(fundo_tela_inicial, (0, 0))
    pygame.display.update()
    

# Função para exibir a tela de jogo
def exibir_tela_jogo(animal):
    janela.blit(fundo_tela_jogo, (0, 0))
    

    exibir_texto("Nível: " + str(nivel_atual), fonte_dicas, cor_verde, (20, 20))
    exibir_texto("Pontuação: " + str(pontuacao), fonte_dicas, cor_branca, (20, 50))
    exibir_texto("Recorde: " + str(recorde), fonte_dicas, cor_branca, (20, 80))

    exibir_texto("Dicas:", fonte_dicas, cor_branca, (20, 120))
    exibir_dicas(animal, pontuacao)

    exibir_texto("Qual é o animal?", fonte_resposta, cor_branca, (20, 300))
    exibir_texto(resposta, fonte_resposta, cor_branca, (20, 340))

    pygame.display.update()

# Função para exibir a tela de acerto
exibindo_tela_acerto = False

def exibir_tela_acerto():
    janela.blit(fundo_tela_acerto, (0, 0))

    # Exibir a imagem de acerto sobreposta ao plano de fundo
    animal_correto = acertos[nivel_atual - 1]  # Obter o animal correto com base no nível atual

    imagem_acerto = pygame.image.load(animal_correto['imagem']).convert_alpha()  # Carregar a imagem correta
    janela.blit(imagem_acerto, (690, 0))  # Exibir a imagem correta

    exibir_texto("Você acertou!", fonte_titulo, cor_branca, (10, 50))
    exibir_texto("Pontuação: " + str(pontuacao), fonte_dicas, cor_branca, (20, 122))
    exibir_texto("Pressione ENTER para continuar", fonte_dicas, cor_verde, (20, 500))

    # Exibir o resumo do animal
    resumo = animal_correto['resumo']
    cor_resumo = cor_branca
    posicao_texto_resumo = (20, 200)  # Posição inicial para o resumo

    linhas_resumo = resumo.split('\n \n')  # Dividir o resumo em linhas

    for linha in linhas_resumo:
        if posicao_texto_resumo[0] + fonte_resumo.size(linha.strip())[0] > largura_janela / 2:
            # Se a linha exceder o limite horizontal da metade da tela, quebrar em mais linhas
            palavras = linha.strip().split()  # Dividir a linha em palavras

            nova_linha = ''
            linhas_adicionais = []

            for palavra in palavras:
                nova_linha_teste = nova_linha + palavra + ' '

                if posicao_texto_resumo[0] + fonte_resumo.size(nova_linha_teste)[0] <= largura_janela / 2:
                    nova_linha = nova_linha_teste
                else:
                    linhas_adicionais.append(nova_linha.strip())
                    nova_linha = palavra + ' '

            linhas_adicionais.append(nova_linha.strip())

            for linha_adicional in linhas_adicionais:
                exibir_texto(linha_adicional, fonte_resumo, cor_resumo, posicao_texto_resumo)
                posicao_texto_resumo = (posicao_texto_resumo[0], posicao_texto_resumo[1] + 30)  # Espaçamento vertical de 30 pixels entre as linhas

        else:
            exibir_texto(linha.strip(), fonte_resumo, cor_resumo, posicao_texto_resumo)
            posicao_texto_resumo = (posicao_texto_resumo[0], posicao_texto_resumo[1] + 30)  # Espaçamento vertical de 30 pixels entre as linhas

    pygame.display.update()

# Função para exibir a tela de fim de jogo
def exibir_tela_fim():
    janela.fill(cor_preta)

    exibir_texto("GAME OVER", fonte_titulo, cor_branca, (250, 200))
    exibir_texto("Pontuação: " + str(pontuacao), fonte_dicas, cor_branca, (320, 300))
    exibir_texto("Pressione ESPAÇO para jogar novamente", fonte_dicas, cor_verde, (150, 400))

    pygame.display.update()

# Loop principal do jogo
jogo_em_execucao = True
jogo_iniciado = False


while jogo_em_execucao:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_em_execucao = False

        if evento.type == pygame.KEYDOWN:
            som_tecla.play()
            if evento.key == pygame.K_SPACE:
                som_space.play
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/Carnaval.mp3')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
                if jogo_iniciado:
                    # Reiniciar o jogo
                    nivel_atual = 1
                    pontuacao = 0
                    resposta = ""
                    jogo_iniciado = True
                else:
                    # Iniciar o jogo
                    jogo_iniciado = True

            if evento.key == pygame.K_RETURN and exibindo_tela_acerto:
                enter.play()
                nivel_atual += 1
                resposta = ""
                exibindo_tela_acerto = False

            if jogo_iniciado and not exibindo_tela_acerto:
                if evento.key == pygame.K_BACKSPACE:
                    resposta = resposta[:-1]
                else:
                    resposta += evento.unicode

    #janela.fill(cor_preta)

    if jogo_iniciado:
        if nivel_atual <= len(animais):
            animal_atual = animais[nivel_atual - 1]
     

            if resposta.lower() == animal_atual['nome'].lower():
                if nivel_atual == animal_atual['nivel']:
                    pontuacao += 100
                else:
                    pontuacao += 50

                if pontuacao > recorde:
                    recorde = pontuacao

                exibindo_tela_acerto = True
                
                exibir_tela_acerto()
                win.play()
                resposta = ""

            if not exibindo_tela_acerto:
                exibir_tela_jogo(animal_atual)

        else:
            exibir_tela_fim()
            jogo_iniciado = False

    else:
        exibir_tela_inicial()

    pygame.display.update()

pygame.quit()