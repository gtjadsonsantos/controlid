# CONTROL ID

Este documento tem como finalidade apresentar a cli para integração com controladoras de modelo controlid

## REQUISITOS

* python => 3


```yaml
python3 /config/scripts/controlid/controlid.py <URL> <USERNAME> <SENHA> <ACTION> <PARAMETERS>

```

- **URL**:  EndereÃ§o da controladora 172.18.2.3 
- **USERNAME**: UsuÃ¡rio da controladora
- **SENHA**: Senha da controladora
- **ACTION**: Modo da aÃ§Ã£o, a usada Ã© a `door` porÃ©m existem outras opÃ§Ãµes (`door`,`sec_box`,`open_collector`,`catra`) 
- **PARAMETERS**: Configuração que define qual o ponto de acesso que vai ser usado, veja exemplos em [docs api](https://www.controlid.com.br/docs/access-api-pt/acoes/abertura-remota-porta-e-catraca/#exemplo-abrir-rele-idaccessidfitidbox)

