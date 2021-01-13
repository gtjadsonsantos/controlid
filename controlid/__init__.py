from requests import post
import json
import argparse
arg_parser = argparse.ArgumentParser(description="UNISEC CLI <CONTROLID>")

arg_parser.add_argument("url")
arg_parser.add_argument("login")
arg_parser.add_argument("password")
arg_parser.add_argument("action")
arg_parser.add_argument("parameters")

arguments = arg_parser.parse_args()


def login(url: str, login: str, password: str):
    """Realiza o login na controladora, retornando o token da sessão logada

        @params url string                    http://172.18.2.3\n
        @params login string                  admin\n
        @params passowrd string               ******88\n
        @return session string                eifh47y34h6*#% 
    """

    response = post(url + "/login.fcgi",
                    data={"login": login, "password": password}).json()
    return response["session"]


def openDoor(url: str, session: str, action: str, parameters: str):
    """Realiza a abertura de ponto de acesso

        @params url string                    http://172.18.2.3\n
        @params session string                admin\n
        @params action string                 door  
        @params parameters string             door=1,reason=3
    """

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        'actions': [
            {
                "action": action,
                "parameters": parameters
            }
        ]
    }

    post(url + "/execute_actions.fcgi?session=" + session,
         data=json.dumps(payload), headers=headers)


openDoor(
    arguments.url,
    login(arguments.url, arguments.login, arguments.password),
    arguments.action,
    arguments.parameters
)
