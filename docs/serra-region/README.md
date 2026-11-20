# Serra Region — plano de expansão

## Estado desta entrega

Esta branch adiciona o **pacote de criação da região**: catálogo de 80 espécies, estrutura da Liga, direção de arte e um validador dos dados. Os arquivos estão em formato de autoria e ainda **não estão ligados às tabelas C nem aos recursos gráficos do jogo**. Não há ROM compilada nesta etapa.

## Conceito

A Serra Region é uma região montanhosa de clima frio, com florestas de pinheiros, cidades costeiras congeladas, minas de prata, fontes termais, ruínas soterradas e uma cadeia de montanhas que termina no Cume Dracônico. A campanha investiga o desaparecimento gradual das auroras: uma organização de exploradores, a **Ordem do Degelo**, está perfurando geleiras para extrair energia térmica antiga e ameaça desequilibrar o clima.

O jogador começa em **Vila Flocos**, recebe seu primeiro parceiro e segue por rotas que alternam áreas abertas, florestas, cavernas e passagens de montanha. A região tem oito ginásios, uma Elite Four e o Campeão Rowan.

## Estrutura da campanha

| Ordem | Local | Líder | Especialidade | Insígnia |
|---:|---|---|---|---|
| 1 | Vila Flocos | Runa | Gelo | Floco |
| 2 | Pedrafria | Dario | Rocha | Granito |
| 3 | Pinhal Alto | Maia | Gelo/Voador | Rajada |
| 4 | Porto Boreal | Nereu | Água | Maré |
| 5 | Minas de Prata | Kora | Aço | Prata |
| 6 | Vila Sombria | Vesper | Fantasma | Eco |
| 7 | Caldeira Invernal | Pyra | Fogo | Brasa |
| 8 | Cume Dracônico | Draven | Dragão | Aurora |

### Elite Four

1. **Eira — Guardiã da Geada:** equipes de gelo e controle de velocidade.
2. **Magnus — Mestre da Forja:** aço e rocha, defesa alta e ataques de contato.
3. **Nox — Vigia do Crepúsculo:** fantasma e psíquico, estados e alterações de ritmo.
4. **Aster — Domador do Céu:** dragão e voador, cobertura e pressão ofensiva.

**Campeão Rowan:** equipe equilibrada de seis integrantes, com Boreas como destaque. A Liga deve exigir cobertura de tipos, não apenas vantagem de gelo.

## Locais principais

- **Vila Flocos:** cidade inicial, laboratório regional e trilha de treinamento.
- **Pedrafria:** povoado de pedreiras, túneis e primeiro grande desafio de navegação.
- **Pinhal Alto:** cidade construída entre pinheiros e passarelas elevadas.
- **Porto Boreal:** porto pesqueiro parcialmente congelado e acesso ao Mar de Serra.
- **Minas de Prata:** complexo industrial antigo, trilhos e forja.
- **Vila Sombria:** vila isolada perto de ruínas e de um antigo observatório.
- **Caldeira Invernal:** fontes termais, vapor e atividade vulcânica sob o gelo.
- **Cume Dracônico:** último povoado antes da Liga, com trilha de altitude.
- **Observatório da Aurora:** local de pesquisa e ponto central da história.
- **Santuário da Aurora:** área lendária acessível após a campanha principal.

## Desafios e mecânicas

- **Nevasca:** visibilidade limitada em rotas específicas; marcos e placas ajudam a orientar o jogador.
- **Gelo deslizante:** puzzles com direção de movimento, evitando becos sem saída e preservando caminhos de retorno.
- **Avalanches:** eventos de cenário avisados por sinais visuais e sonoros, com rotas alternativas.
- **Correntes marítimas:** canais e comportas no Porto Boreal e no Mar de Serra.
- **Vagonetes:** desvios de trilhos nas Minas de Prata.
- **Vapor e fontes termais:** válvulas abrem caminhos; fontes termais funcionam como pontos de recuperação.
- **Expedição Branca:** desafio opcional pós-Liga com acampamentos limitados.
- **Torneio das Estações:** torneio pós-jogo com regras temáticas rotativas.

Os obstáculos devem ser anunciados antes de exigir uma ação irreversível. Mapas de gelo e avalanche precisam sempre permitir um caminho de recuperação, evitando softlocks.

## Pokédex de Serra

O arquivo [`data/serra_region/species.json`](../../data/serra_region/species.json) contém **80 espécies originais**, em 26 famílias evolutivas e dois lendários. Cada entrada possui tipos compatíveis com a base Gen III, atributos-base, habilidade existente como referência de design, evolução, habitat, descrição e conceito visual.

Os nomes foram mantidos com até 10 caracteres para respeitar o limite tradicional dos nomes de Pokémon nesta base.

## Direção de arte

O arquivo [`data/serra_region/tileset_palette_plan.json`](../../data/serra_region/tileset_palette_plan.json) define paletas frias, tratamentos de tilesets e regras para sprites. O objetivo é neve estilizada GBA, sem transformar tudo em azul: regiões vulcânicas, fogo e espécies de outros tipos preservam suas cores de identidade.

## Próximas etapas de integração ao motor

1. Expandir `include/constants/species.h` e ajustar contadores e limites de espécies com cuidado.
2. Integrar nomes, dados-base, evoluções, learnsets, TM/HM, egg moves, Pokédex, cries e tabelas de gráficos.
3. Criar os 80 conjuntos de sprites front/back, ícones, paletas e footprints.
4. Registrar mapas, layouts, scripts, textos e conexões em `data/maps/`, `data/layouts/` e `data/maps.s`.
5. Criar encontros selvagens e distribuição progressiva das novas espécies.
6. Adaptar equipes de treinadores, oito ginásios, Elite Four, Campeão e eventos da Ordem do Degelo.
7. Testar compilação, colisões, transições, salvamento, evolução, Pokédex e batalhas em emulador.

A integração deve acontecer em commits pequenos e compiláveis. Não se deve aumentar `NUM_SPECIES` antes de preparar as tabelas dependentes, pois sprites, learnsets e dados de batalha indexam o mesmo conjunto de espécies.
