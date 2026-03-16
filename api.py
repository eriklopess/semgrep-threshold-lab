import pickle
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
