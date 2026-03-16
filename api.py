import json
import yaml

def deserialize_user_data(data):
    # CORRIGIDO: usar JSON em vez de pickle
    return json.loads(data)

def get_config():
    # CORRIGIDO: yaml.safe_load — nunca executa código
    with open("config.yaml") as f:
        return yaml.safe_load(f.read())import pickle
import base64

def deserialize_user_data(data):
    # VULNERABILIDADE: pickle.loads com dados do usuário — Remote Code Execution
    decoded = base64.b64decode(data)
    return pickle.loads(decoded)

def get_config():
    import yaml
    # VULNERABILIDADE: yaml.load sem Loader (unsafe por padrão)
    with open("config.yaml") as f:
        return yaml.load(f.read())
