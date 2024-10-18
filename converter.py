import requests
import base64

def fetch_subscription(url):
    """从订阅链接获取数据"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch subscription: {e}")
        return None

def decode_base64(content):
    """解码 Base64 数据"""
    try:
        return base64.b64decode(content).decode('utf-8')
    except Exception as e:
        print(f"Failed to decode base64: {e}")
        return None

def convert_to_clash(nodes):
    """将节点转换为 Clash 格式"""
    clash_format = {"proxies": []}
    for node in nodes:
        clash_format["proxies"].append({
            "name": node["name"],
            "type": "vmess",
            "server": node["server"],
            "port": node["port"],
            "uuid": node["uuid"],
            "alterId": node["alterId"],
            "cipher": "auto",
        })
    return clash_format

def convert_nodes(content, input_type, output_type):
    """根据输入和输出格式进行转换"""
    if input_type == "v2ray" and output_type == "clash":
        nodes = decode_base64(content).splitlines()
        return convert_to_clash([parse_v2ray(node) for node in nodes])
    return None

def parse_v2ray(line):
    """解析 V2Ray 节点信息"""
    parts = line.split(',')
    return {
        "name": parts[0],
        "server": parts[1],
        "port": parts[2],
        "uuid": parts[3],
        "alterId": parts[4],
    }
