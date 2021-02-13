# CONTROL ID


## GETTER STARTED

Poste this propety `controlid:` in your configuration file

## SERVICES AVAILABLE

* **controlid.open_remote_door**: Open doors Remote


```yaml
ip: 192.168.0.1
username: admin
password: admin
actions:
  - action: door
    parameters: door=1
  - action: sec_box
    parameters: 'id=65793, reason=3'
  - action: open_collector
    parameters: ''
  - action: catra
    parameters: allow=clockwise or allow=both
```


[docs api](https://www.controlid.com.br/docs/access-api-pt/acoes/abertura-remota-porta-e-catraca/#exemplo-abrir-rele-idaccessidfitidbox)

