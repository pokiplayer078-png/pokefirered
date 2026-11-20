# Pokémon FireRed — Serra Region

## Estado atual da implementação

A branch `serra-region-foundation` já contém integração inicial no código do FireRed:

- **101 espécies internas**: as 80 espécies originais de Serra mais 21 aves lendárias, formas de Galar e formas regionais de Serra/Calor.
- Constantes de espécies, atributos, nomes, evoluções e learnsets.
- Entradas nas tabelas de sprites front/back, coordenadas, paletas normal/shiny, ícones e pegadas.
- Tipo **Fada** registrado e uma camada inicial de efetividade de golpes.
- Habilidade **Glaciate**: para Lugia de Serra, golpes do tipo Normal são tratados como Gelo no cálculo de dano e tipo em batalha.
- IDs de flags e variáveis para registrar a captura das aves, o chamado de Lugia, a derrota das aves de Galar e o florescimento permanente de Calor.
- Primeiro mapa `VilaFlocos`, NPC pesquisador e entrega de **Snolet Lv. 5**; novos jogos começam nesse mapa.

Esta ainda é uma **integração de fundação**, não uma ROM final. Há assets e partes de campanha que ainda precisam ser criados e conectados. Consulte [INTEGRATION_STATUS.md](INTEGRATION_STATUS.md).

## História principal

O aquecimento anormal está descongelando a ilha de Serra. As três aves lendárias de Galar — Articuno, Zapdos e Moltres — estão alterando as correntes de ar e espalhando calor extremo pela região.

O jogador precisa localizar as três aves lendárias de Serra:

- **Articuno de Serra** — Santuário do Vento Branco.
- **Zapdos de Serra** — Pico do Trovão Azul.
- **Moltres de Serra** — Fornalha Azul.

Após reunir as três plumas, o jogador chama **Lugia de Serra**, do tipo **Gelo/Fada**. Sua habilidade exclusiva, **Glaciate**, converte golpes Normais de Lugia em golpes de Gelo.

Lugia ajuda o jogador a enfrentar as três aves de Galar. Quando elas são derrotadas, o aquecimento acelerado é interrompido, mas a história ainda não terminou: **Ho-Oh da Região de Calor** aparece. Esse Ho-Oh é do tipo **Fada/Fogo** e é extremamente poderoso.

Ao ser derrotado, Ho-Oh cai. O gelo não volta a cobrir a ilha. O clima estabiliza, as terras que já haviam descongelado florescem e revelam a beleza da **Região de Calor**. O pós-jogo permite explorar essa nova região.

A campanha e os eventos estão descritos em [story_and_postgame.json](../../data/serra_region/story_and_postgame.json).

## Pokédex de Serra e formas regionais

O arquivo [species.json](../../data/serra_region/species.json) mantém o catálogo de 101 entradas. A proposta evita transformar todos os Pokémon em tipos Gelo:

- Serra inclui Pokémon de Gelo, Água, Rocha, Elétrico, Fantasma, Dragão, Fogo, Planta, Lutador, Voador, Psíquico e outros tipos.
- As aves de Serra e as aves de Galar são entradas separadas para permitir encontros e batalhas distintas.
- As formas de Calor são adequadas a vales floridos e áreas quentes: incluem combinações Fogo/Planta, Planta/Terra e Planta/Fada.

As formas regionais são espécies internas próprias na implementação atual. Isso torna o registro e os atributos jogáveis no motor mais simples, mas não significa que a interface de Pokédex já apresente uma tela de formas regionais dedicada.

## Progressão de ginásios

### Serra — campanha principal

| Ordem | Cidade | Líder | Especialidade | Insígnia |
|---:|---|---|---|---|
| 1 | Vila Flocos | Runa | Gelo | Floco |
| 2 | Pedrafria | Dario | Rocha | Granito |
| 3 | Pinhal Alto | Maia | Gelo/Voador | Rajada |
| 4 | Porto Boreal | Nereu | Água | Maré |
| 5 | Minas de Prata | Kora | Aço | Prata |
| 6 | Vila Sombria | Vesper | Fantasma | Eco |
| 7 | Caldeira Invernal | Pyra | Fogo | Brasa |
| 8 | Cume Dracônico | Draven | Dragão | Aurora |

Elite Four: **Eira**, **Magnus**, **Nox** e **Aster**. Campeão: **Rowan**.

### Calor — pós-jogo planejado

| Ordem | Cidade | Líder | Especialidade | Insígnia |
|---:|---|---|---|---|
| 1 | Vila Pomar | Liora | Planta | Pétala |
| 2 | Forno Solar | Caio | Fogo | Brasa Solar |
| 3 | Baía das Flores | Marina | Água | Maré Clara |
| 4 | Mirante do Sol | Ícaro | Fada | Alvorada |

Campeã de Calor: **Solene**.

As equipes e níveis estão em [gyms_and_league.json](../../data/serra_region/gyms_and_league.json) e [story_and_postgame.json](../../data/serra_region/story_and_postgame.json).

## Vila Flocos — primeiro mapa integrado

O mapa `MAP_VILA_FLOCOS` está cadastrado em `data/maps/map_groups.json`, usa a seção `MAPSEC_SERRA_REGION` e é o ponto inicial de novos jogos. Um pesquisador entrega Snolet Lv. 5 uma única vez; a flag de entrega é persistida no save.

**Limitação visual atual:** Vila Flocos reutiliza o layout de One Island e suas tilesets existentes. O mapa ainda não possui casas, rotas conectadas, centro Pokémon, laboratório ou tilesets próprios de neve. O clima `WEATHER_SNOW` está definido na base como não utilizado, por isso o efeito visual de neve ainda precisa ser implementado/testado.

## Direção de arte

[tileset_palette_plan.json](../../data/serra_region/tileset_palette_plan.json) descreve as paletas e o estilo dos sprites. As tabelas gráficas atuais apontam para sprites existentes como placeholders válidos; os desenhos exclusivos das 101 espécies ainda precisam ser produzidos.

## Próximas etapas obrigatórias

1. Criar tilesets e paletas reais de Serra e Calor, e testar colisões.
2. Desenhar e importar sprites front/back, ícones, paletas normal/shiny, footprints e cries.
3. Completar a interface e a Pokédex para os novos IDs, inclusive apresentação do tipo Fada e das formas regionais.
4. Criar mapas conectados de Serra, os oito ginásios, Liga, santuários das três aves e mapas da Região de Calor.
5. Conectar a história a scripts de eventos: capturas, altar de Lugia, três batalhas contra as aves de Galar, batalha de Ho-Oh e transição permanente para o cenário florido.
6. Implementar encontros selvagens, treinadores, equipes e recompensas de campanha/pós-jogo.
7. Compilar a ROM, corrigir erros de build e testar uma campanha completa no mGBA.

Não declarar a ROM jogável até a compilação e os testes de transição, batalhas, save, Pokédex e progressão terem sido concluídos.
