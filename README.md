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
- [x] Definir estrutura que suporte multiplayer ou vincular cada partida ao _socket_.
- [x] Por enquanto não haverá níveis dificuldades para 1° entrega.
- [x] 6 Operações por partida.
- [x] Temporizador para a partida.
- [x] Terá um temporizador por partida.
- [x] Mostrar no final da partida lista das operações corretas/ erradas e quantidade de acerto/erro
- [x] Opção de sair ou começar uma partida.
- [x] Quando conectar perguntar se quer começar a partida.

## TO DO NOW

- [ ] Multiplus clientes (socket) (conexão e desconexão)
- Quando o cliente conectar:
- [ ] Perguntar se quer iniciar uma partida ou logo após digitar o nome
- [ ] Enviar para o cliente a partida
- No servidor:
- [ ] Fazer a lógica da partida
- [ ] quando o cliente inicia uma partida, o servidor envia a equação da partida
- [x] Função de equaçoes randomicas
- [ ] servidor envia as operações e esperar o cliente responder
- [ ] pegar a resposta e guardar na estrutura de resposta (array simples)
- [ ] a cada operação gerado, guardar na estrutura daquele cliente as operações e respostas e comparar com a estrutura das respostas do cliente
- [ ] Serão duas estruturas perguntas x respostas, a primeira estrutura (array) irá conter a operação e a resposta, e a segunda estrutura a resposta de cada operação
-[ ] criar uma variavel de acerto  e erro,




-------------------------TO US---------------------
git add . : adiciona todos os arquivos
git add caminho/nome_arquivo: para adicionar somente um arquivo especifico (pega o caminho e o nome no git status)

git commit -m "digitar mensagem aqui" (Fazer commit local)

git push origin nome_branch (enviar commit para a branch remota)

Abrir Pull no git (clicar em pull request, geralmente o novo commit ele pergunta se quer abrir um pull request)

Colcoar os revisores e o assignee para você que criou

Comando para criar nova branch:

git checkout -b nome_da_branch (nao precisa ser com aspas) 

Comando para mudar de branch:

git checkout nome_da_branch


Comando para saber o status dos arquivos:

git status

Comando saber em que branch estou

git branch (a sua é a verdinha)

-----------Atualizar a branch -----------

Todo dia ver se tem alguma atualização 

git pull origin master --rebase

resolve os conflitos se tiver

------- caso no Pull request indique conflito---
