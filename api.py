import json
import yaml

def deserialize_user_data(data):
    # CORRIGIDO: usar JSON em vez de pickle
    return json.loads(data)

def get_config():
    # CORRIGIDO: yaml.safe_load — nunca executa código
    with open("config.yaml") as f:
        return yaml.safe_load(f.read())
