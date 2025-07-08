Organização do Código
1. MotorDeVoz
Responsável por controlar o motor de síntese de voz:

Inicializa o motor pyttsx3.

Configura voz (masculina ou feminina).

Ajusta a velocidade da fala.

Converte texto em arquivo de áudio (.mp3 ou .wav).

Salva o arquivo no caminho escolhido pelo usuário.

2. Interface
Construída com tkinter para interação com o usuário:

Caixa de texto para digitar ou carregar texto.

Botão para carregar arquivos .txt.

Opções para escolher voz (feminina/masculina).

Opções para velocidade (normal/lenta).

Opções para formato do áudio (.mp3/.wav).

Botão para converter texto em áudio e salvar.

3. main.py
Arquivo principal que une a interface e o motor de voz:

Inicializa a interface.

Chama as funções do motor para converter o texto.

Controla o fluxo do programa.