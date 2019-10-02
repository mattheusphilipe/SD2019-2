# FACOM SD2019-2
Repositório com a finalidade de apresentar os códigos fontes referentes aos trabalhos da disciplina de Sistemas Distribuídos da Universidade Federal de Uberlândia.

## Introdução e descrição

  MathQuiz este será o nome que irei intitular o projeto, é um jogo simples que consiste em responder o resultado de uma operação matemática, pretendo criar a opção que o usuário possa escolher a operação matemática desejada (multiplicação, soma, divisão e subtração), 3 níveis de dificuldade irei denominar de _easy_, _medium_ e _hard_,  cada uma com _timer_  para cada operação. Por final criar uma sessão onde 2 ou mais pessoas possam se conectar e jogar uma partida, ganha quem responde corretamente a maior quantidade de operações matemática da partida, se mais de uma pessoa respondeu a mesma quantidade corretamente, será levado em consideração o tempo médio que cada uma demorou para responder as operaçãoes. 
  Antes de inciar uma partida o jogador deverá preencher o seu nome.

## Tecnologias

- Implementação do projeto será na linguagem de programação Python com interface de linha de comando via um terminal do SO.
- Os valores das operações serão randômicos a cada partida.
- Os dados estarão "armazenados" estáticamente na memória do computador.
- Haverá um servidor com a lógica do jogo que irá prover as operações para cada partida individual ou em grupo e no final mostrará o resultado no final da quantidade de acerto e tempo médio de resposta de cada operação.
  
## Motivação e contexto

  Fomentar o aprendizado de se utlizar sistemas distribuídos com abordagens práticas e teóricas lecionadas nas aulas.
  
## Como deve ser testado?

- [ ] teste de concorrência: demonstrando que múltiplos jogadores podem acessar o serviço ao mesmo tempo em partidas individuais ou em grupos sem comportamentos estranhos.
- [ ] teste de recuperação de falhas: quando um componente falha e volta a executar, ele não leva o sistema a nenhum estado inesperado.
- [x] demonstração de funcionalidades: múltiplas partidas individuais ou em grupos.

## Integrantes
- Ivana Brito
- Matheus Felipe Araújo
- Bruno Torres
- Gabriel Victor

## Capturas de tela:

- Ainda não se aplica.

## Pré-requisito:

- Ter o Python instalado em seu sistema operacional, Windows ou Linux, sendo versão 3.7 ou acima

## Arquivos do projeto

_utils.py_
Arquivo que contém as funções utilizadas no projeto, sendo elas:
- def int_float(number, option)
- def encode_decode(data, option)
- def fun_equacao()

_client.py_
  Esse arquivo contém o menu inicial do jogo, é responsável pela conexão com o servidor, finaliza conexão com ele e encerra o jogo. Durante o jogo é responsável por capturar as respostas das equações. Também oferece para o usuário a opção de se conectar com o servidor externo, capturando do teclado o IP do mesmo. Além de ser responsável pelo timeout e pelo tratamento de entrada de dados.

_server.py_
  Responsável inicialmente por gerencias as conexões simultâneas, disponibiliza funções para receber mensagens, cria a estrutura para o armazenamento de dados(resposta do usuário, equação, resposta das equações, quantidade de acertos e erros) e identifica cada cliente e seus estados no jogo. Também envia as equações e recebe os resultados dos usuários, comparando-os com o resultado. Ao finalizar gera o placar e reinicia o jogo caso o usuário deseje. 

## Como jogar uma partida
  _Servidor executando na mesma máquina_
  - [1] Abra um terminal e acesse a pasta `services` (caminho completo: `SD2019-2\src\services`
  - [2] Execute o arquivo server.py  `Ex:(python server.py ou py -3.7 server.py)`
  - [3] Abra outro terminal e acesse a pasta anterior novamente
  - [4] Execute o arquivo client.py  `Ex:(python client.py ou py -3.7 client.py)`
  - [5] No terminal digite o nome desejado e aperte `ENTER`
  - [6] Na segunda linha, tecle `ENTER` novamente
  - [7] Digite `START` para começar a partida ou `EXIT` para sair
  - [8] Se escolheu a opção `START`, a primeira equação irá aparecer. São no total 7 operações
  - [9] Após responder todas as operações, será mostrado na tela as seguintes informações:
    - quais foram suas equações
    - respostas que você digitou,
    - respostas certas 
    - quantidade de operações que você acertou e errou
  - [10] Você pode começar o jogo novamente escolhendo `START` ou sair ao escolher `EXIT`

_Servidor executando em outro computador_
- Execute os 5 primeiros passos anteriores, exceto executar o servidor
  - Escolha `EXT`
  - Digite o _IP_ da máquina na qual o servidor está sendo executado
  - Execute os mesmos passos a partir do 7º passo anterior
