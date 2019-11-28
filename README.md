# minicurso-testes
Minicurso sobre testes ministrado no IFTech 2019

Configurando o ambiente
Checar se o appium está instalado
<code>which appium</code>
Se não tiver instalado 
<code>npm install -g appium</code>

Checar se o appium-doctor está instalado
<code>which appium-doctor</code>
Se não tiver instalado
<code>npm install -g appium-doctor</code>

Checar se o java está instalado
<code>which java</code>
Se não tiver senta e chora

Checar se o andoid está instalado
<code>which android</code>

Roda o appium doctor pra ver se as variáveis estão configuradas corretamente
<code>appium-doctor</code>

Configuração das variáveis de ambiente
<code>nano .bash_profile</code>

<code>
export ANDROID_HOME=/seu caminho para /Android/sdk 
export PATH=$ANDROID_HOME/platform-tools:$PATH 
export PATH=$ANDROID_HOME/tools:$PATH 
export PATH=$ANDROID_HOME/build-tools:$PATH 
export JAVA_HOME=/seu caminho para/jdk1.8.0_112.jdk
export PATH=$JAVA_HOME/bin:$PATH 
</code>

Depois execute o arquivo para configurar as variáveis e rode o appium-doctor para checar se funcionou
<code>source .bash_profile</code>
<code>appium-doctor</code>

<code>which android</code>