# CONTROL ID

Este documento tem como finalidade apresentar a cli para integração com controladoras de modelo controlid

## REQUISITOS

* python => 3


```yaml
python3 controlid.py <URL> <USERNAME> <SENHA> <ACTION> <PARAMETERS>

```

- **URL**:  Endereço da controladora 172.18.2.3 
- **USERNAME**: Usuario da controladora
- **SENHA**: Senha da controladora
- **ACTION**: Modo da ação, a usada ao a `door` porÃ©m existem outras opções (`door`,`sec_box`,`open_collector`,`catra`) 
- **PARAMETERS**: Configuração que define qual o ponto de acesso que vai ser usado, veja exemplos em [docs api](https://www.controlid.com.br/docs/access-api-pt/acoes/abertura-remota-porta-e-catraca/#exemplo-abrir-rele-idaccessidfitidbox)

