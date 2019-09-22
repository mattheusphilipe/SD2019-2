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
- [ ] demonstração de funcionalidades: múltiplas partidas individuais ou em grupos.

## Capturas de tela:

- Ainda não se aplica.

## TO DO

- Definir estrutura que enviará os dados da partida ao usuário.
[x] Definir estrutura que suporte multiplayer ou vincular cada partida ao _socket_.
[x] Por enquanto não haverá níveis dificuldades para 1° entrega.
[x] 6 Operações por partida.
[x] Temporizador para a partida.
[x] Terá um temporizador por partida.
[x] Mostrar no final da partida lista das operações corretas/ erradas e quantidade de acerto/erro
[x] Opção de sair ou começar uma partida.
[x] Quando conectar perguntar se quer começar a partida.
