# Minicurso Automação
Minicurso sobre automação de testes em dispositivos móveis ministrado no IFTech 2019

## Configurando o ambiente
Checar se o appium está instalado 
```
which appium
```

O output deve ser 
```
/usr/local/bin/appium
```

Para instalar: 
```
npm install -g appium
```

Checar se o appium-doctor está instalado 
```
which appium-doctor
```

Para instalar:
```
npm install -g appium-doctor
```

Checar se o java está instalado
```
which java
```

Para instalar:\
https://www.bonusbits.com/wiki/HowTo:Install_Java_Development_Kit

Checar se o andoid está instalado
```
which android
```
Para instalar:\
https://developer.android.com/studio/index.html

Roda o appium doctor pra ver se as variáveis estão configuradas corretamente
```
appium-doctor
```

Configuração das variáveis de ambiente
```
nano .bash_profile
```

```
export ANDROID_HOME=/seu caminho para /Android/sdk 
export PATH=$ANDROID_HOME/platform-tools:$PATH 
export PATH=$ANDROID_HOME/tools:$PATH 
export PATH=$ANDROID_HOME/build-tools:$PATH 
export JAVA_HOME=/seu caminho para/jdk1.8.0_112.jdk
export PATH=$JAVA_HOME/bin:$PATH 
````

Depois execute o arquivo para configurar as variáveis e rode o appium-doctor de novo para checar se funcionou
``` 
source .bash_profile
appium-doctor
```
As dependências obrigatórias devem aparecer desse jeito\
![appium-doctor]
(tentativas/imagens/appium-doctor.png)

Agora vamos instalar o Python Client do Appium\
Primeiro checamos se o pip3 está instalado\
``` 
pip3 --version 
```
Para instalar:
```
sudo apt install python3-pip
```
Instalar o Appium Pyhton Client
```
pip3 install Appium-Python-Client
```
## Construindo capabilities
Vamos criar uma classe chamada Driver, que vai ter as configurações de capabilities e do driver

As capabilities no python vem em forma de Json. As obrigatórias são:
* PlatformName
* App
* DeviceName

Optamos por colocar a udid do dispositivo, que especifica o dispositivo no qual o teste será executado\
Para isso, vamos executar o comando 
```
adb devices
```
Se o retorno for 
```
List of devices attached
seu udid    unauthorized
```
Você precisa ativar a depuração usb do seu celular
```
Configurações > Sistema > Opções de desenvolvedor > Depuração USB
```
Rode o comando de novo, e o retorno deve ser:
```
List of devices attached
seu udid	device
```
Quando setamos as capabilities, elas devem ficar assim:
```
desired_caps = {
    "platformName": "Android",
    "deviceName": "Nome do seu dispositivo",
    "udid": "udid do dispositivo"
    "app": "local do aplicativo"
}
```

## Construindo o driver
O driver é onde o servidor do appium vai ser startado, onde os testes vão rodar\
Por padrão, ele inicia na porta 4723, localmente
```
$ appium
[Appium] Welcome to Appium v1.15.1
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```
Então é pra lá que vamos mandar nosso teste
```
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
```
Note que quando configuramos o driver, passamos pra ele as informações configuradas nas capabilities

## Achando elementos na tela
Usando o driver, vamos executar todas as ações dentro da tela (achar e clicar nos elementos, avaliar o retorno das ações, etc...) 
Hoje vamos utilizar principalmente as funções: Wait, Expected Conditions e find by

Crie uma classe para mapear os elementos da tela e importe as seguintes funções:

```
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
```
Algumas dessas funções são do Selenium, mas o que se refere a mobile vem do Appium 

Primeiro precisamos saber quais elementos estão na tela do aplicativo, e dizer que ações vamos realizar com eles

Vamos abrir o uiautomatorViewer e pegar o id dos elementos
```
cd Android/Sdk/tools/bin
./uiautomatorviewer
```
Na classe criada para o mapeamento de tela, passamos como construtor o driver e o wait, uma propriedade do driver que diz o tempo de espera do driver em milisegundos antes de procurar pelo elemento
```
def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver.instance, 10)
```

Agora vamos começar a descrever os elementos que encontramos na inspeção de tela e criar funções com ações a serem realizadas neles
```
    def click_btn_one(self):
        # espere até o elemento de id "one" ser clicável e depois clique nele
        self.btn_one = self.wait.until(EC.element_to_be_clickable((By.ID, "one")))
        self.btn_one.click()
        return self
```
Agora que finalmente configuramos tudo que é necessário para a execução do teste, vamos construí-lo!!

![finalmente](https://media.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif)

## Construindo o teste
Em Python, a lib de teste unitário é a *unittest*, vamos criar uma classe que importe essa lib e as outras classes já criadas

A classe tem que ter o driver como parâmetro no construtor, porque ele precisa ser iniciado quando o teste rodar

```
from Pages.page_popup import PagePopUp
from Pages.page_calculator import Calculator # página mapeada anteriormente
from Driver.driver_local import Driver
import unittest

class Testes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
```
No unittest, todas as funções a serem executadas começam com **test**, nessa função vamos chamar as classes de mapeamento e suas funções
```
def test_calcular_soma(self):
    calculator = Calculator(self.driver)

    calculator.click_btn_two() # 2
    calculator.click_btn_plus() # +
    calculator.click_btn_two() # 2
    calculator.click_btn_equal() # =
    
    resultado = calculator.get_value_display # resultado
```
O valor esperado dessa soma é 4, certo? Então vamos checar se o valor retornado corresponde ao esperado usando *assert*

```
        assert(4, resultado)
```
Tudo certo! Agora é só rodar e ver a mágica acontecendo!!

![magic](https://media.giphy.com/media/12NUbkX6p4xOO4/giphy.gif)
