from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import os

chrome_options= Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'download.default_directory': r' ', # default_directory C:\Exemple\exemple\exemple...\relatorios
    'profile.default_content_setting_values.automatic_downloads': 1,
})
driver= webdriver.Chrome(options=chrome_options)
driver.get('https://consulta-empresa.netlify.app/')

sleep(5)

campo_usuario= driver.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
campo_usuario.click()
campo_usuario.send_keys('jhonatan')
campo_senha= driver.find_element(By.XPATH, "//input[@id='password']")
campo_senha.click()
campo_senha.send_keys('12345678')
sleep(1)
botao_entrar= driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg']")
botao_entrar.click()
sleep(5)

def baixar_relatorios_das_empreas(driver):


    nomes_empresas= driver.find_elements(By.XPATH, "//td[@name='nome_empresa']")
    sleep(2)
    botoes_download_pdf= driver.find_elements(By.XPATH, "//button[@class='download-btn']")
    sleep(2)

    for nome, botao_pdf in zip(nomes_empresas, botoes_download_pdf):
        botao_pdf.click()
        sleep(2)
        diretorio= #directory 
        nome_antigo= 'perfil_empresa.pdf'
        novo_nome= f'{nome.text}.pdf'

        caminho_completo_antigo= os.path.join(diretorio, nome_antigo)
        caminho_completo_novo= os.path.join(diretorio, novo_nome)

        os.rename(caminho_completo_antigo, caminho_completo_novo)

baixar_relatorios_das_empreas(driver=driver)

botao_proxima_pagina= driver.find_element(By.XPATH, "//button[@id='nextBtn']")

while botao_proxima_pagina.get_attribute('disabled') == None:
    botao_proxima_pagina.click()
    baixar_relatorios_das_empreas(driver=driver)

input('Aperte ENTER para fechar')




