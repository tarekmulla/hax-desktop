"""different methods to support payloads files"""
from classes.attacks.attack import Attack


def load_payloads(placeholder_text, file_path) -> list:
  """Load the attack payloads from a file"""
  with open(file_path, "r", encoding="UTF-8") as payloads_file:
    return [payload.strip("\n").replace("{{PLACEHOLDER}}", placeholder_text) for payload in payloads_file.readlines()]


def summarize_response(payload: str, attack: Attack):
  """get attack response text"""
  response_result = ""
  response_result += f"PAYLOAD: {payload}\n"
  response_result += f"REQUEST URL: {attack.response.request.url}\n"
  response_result += f"REQUEST HEADERS: {attack.response.request.headers}\n"
  req_body = str(attack.response.request.body)
  response_result += f"REQUEST BODY: {req_body}\n"
  if attack.is_success:
    response_result += "The attack has succeded\n"
  else:
    response_result += "The attack has failed\n"
  response_result += "-" * 50
  response_result += "\n" * 2
  return response_result
