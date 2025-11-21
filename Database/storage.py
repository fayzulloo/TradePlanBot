import json, os
from config import DB_PATH

def load_user_data(user_id):
    if not os.path.exists(DB_PATH): return {}
    with open(DB_PATH,'r') as f: d=json.load(f)
    return d.get(str(user_id),{})

def save_user_data(user_id,data):
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))
    d={}
    if os.path.exists(DB_PATH): d=json.load(open(DB_PATH))
    d[str(user_id)]=data
    json.dump(d,open(DB_PATH,'w'),indent=4)
