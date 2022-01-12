from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class seleniumbusca():
    def __init__(self):
        driver = webdriver.Chrome('H:/StudySpace/Python/CEP-UF/chromedriver.exe')
        driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
        self.driver = driver
    def buscaCep(self,cep):
        driver =  self.driver
        
        element = driver.find_element_by_xpath('//*[@id="endereco"]')
        element.send_keys(str(cep))
        confirm = driver.find_element_by_xpath('//*[@id="btn_pesquisar"]')
        confirm.click()
        time.sleep(1)
        try:
            cep = driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
            logradouro = driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
            bairro = driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
            localidade_uf = driver.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

            init = localidade_uf.find('/') + 1 

            #result = {'logradouro':logradouro,'bairro':bairro,'localidade':localidade_uf[0:init - 1],'uf':localidade_uf[init:len(localidade_uf)]}
            dadosCep = {'cep': cep.replace('-',''), 'logradouro': logradouro, 'complemento': '', 'bairro': bairro, 'localidade': localidade_uf[0:init - 1],
                        'uf': localidade_uf[init:len(localidade_uf)], 'ibge': '', 'gia': '', 'ddd': '', 'siafi': ''}
        except:
            dadosCep = {'cep': 'null', 'logradouro': 'null', 'complemento': '', 'bairro': 'null',
                        'localidade': 'null', 'uf': 'null', 'ibge': 'null', 'gia': 'null', 'ddd': 'null', 'siafi': 'null'}

        newSearch = driver.find_element_by_xpath('//*[@id="btn_voltar"]').click()
        return dadosCep

if __name__ == '__main__':  
    main = seleniumbusca()
    main.buscaCep('06029-900')



