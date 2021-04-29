# CONTROL ID

This custom integration permits Home Assistant to communicate with `controlid` controllers through  http requests.

**Whats does it do?**
- Allow opening the doors/access points

**Tested hardwares**:
- idFlex: https://www.controlid.com.br/docs/idbox-pt/
- idBox: https://www.controlid.com.br/docs/idbox-pt/

## GETTING STARTED

Paste this property `controlid:` in your configuration file
## Services

### controlid.open_remote_door

Allows open doors Remote


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

## Platforms

### Sensor

The controlid sensor platform allows you get current state door

To use your controlid sensor in your installation, add the following to your `configuration.yaml` file:



> **ip** string `required`
> 
> Define ip of your controller
> 
> **name** string `required`
> 
> Define name to your sensor
> 
> **icon** string `(optional)`
> 
> Define icon for your sensor. By default is `mdi:door`
> 
> **username** string `required`
> 
> Define username for connection with controller.
> 
> **passowrd** string `required`
> 
> Define password for connection with at controller.
> 
> **doorid** string `required`
> 
> Choose doorid for get current value 


Example ballow, get the current state of door 1

```yaml
sensor:
  - platform: controlid
    ip: 192.168.0.1
    name: "Your sensor name"
    username: admin
    password: admin
    doorid: "1"

```

[docs api](https://www.controlid.com.br/docs/access-api-pt/acoes/abertura-remota-porta-e-catraca/#exemplo-abrir-rele-idaccessidfitidbox)
 | [postman](https://documenter.getpostman.com/view/7260734/S1LvX9b1?version=latest#00155afb-f5aa-4615-b15b-ed43a57d5836)

## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
## AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/controlid/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
</table>

# CONTRIBUTORS



<table>
  <tr>
    <td align="center"><a href="https://github.com/pauloeduardodarosa"><img src="https://avatars.githubusercontent.com/u/3733250?s=460&u=1f62e3cd067caa8b9eb27ba64794f381e4cb5168&v=4" width="100px;" alt=""/><br /><sub><b>Paulo Eduardo da Rosa</b></sub></a><br /><a href="https://github.com/pauloeduardodarosa/controlid/commits?author=pauloeduardodarosa" title="Code">💻</a> <a href="https://github.com/pauloeduardodarosa" title="Design">🎨</a></td>
</table>




 

