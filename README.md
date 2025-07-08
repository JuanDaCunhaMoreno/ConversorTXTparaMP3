Conversor de Texto para Áudio
Este projeto é um aplicativo simples em Python que converte textos em arquivos de áudio usando a biblioteca pyttsx3 para síntese de voz e tkinter para a interface gráfica.

Estrutura do Projeto
1. MotorDeVoz
Este módulo é responsável pela funcionalidade de conversão do texto em áudio. Ele utiliza a biblioteca pyttsx3, que é um motor de texto para fala offline.

Inicializa o motor de voz (pyttsx3.init()).

Define parâmetros de voz, como gênero (feminina ou masculina).

Ajusta a velocidade da fala.

Converte o texto em áudio e salva no formato desejado (.mp3, .wav).

2. Interface (Interface Tkinter)
Este módulo é responsável por criar a interface gráfica do usuário usando tkinter.

Um campo de texto para digitar ou carregar o texto a ser convertido.

Botão para carregar arquivos .txt.

Opções para escolher o gênero da voz (feminina ou masculina).

Opções para selecionar a velocidade da fala (normal ou lenta).

Opções para escolher o formato do arquivo de áudio (mp3 ou wav).

Botão para converter e salvar o áudio.

3. main.py
O arquivo principal que integra o MotorDeVoz com a Interface.

Cria a janela principal.

Liga os botões e as ações às funções do MotorDeVoz.

Executa o loop da interface gráfica para interação com o usuário.

Como usar
Execute o arquivo main.py para abrir a interface gráfica.

Digite um texto no campo ou carregue um arquivo .txt.

Escolha a voz, velocidade e formato desejados.

Clique em "Converter e Salvar Áudio".

Escolha o local e o nome do arquivo para salvar o áudio gerado.

Uma mensagem de sucesso aparecerá ao final.
