# Recupera o código do telefone. Não mude
# O arquivo deve permanecer completamente inalterado

def retrieve_phone_code(driver) -> str:
    """Este código recupera o número de confirmação do telefone e o retorna como uma string.
    Use-o quando o aplicativo espera o código de confirmação para passá-lo para seus testes.
    O código de confirmação do telefone só pode ser obtido após ser solicitado no aplicativo."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
