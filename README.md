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


## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
# AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/controlid/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
  <tr>
</table>
