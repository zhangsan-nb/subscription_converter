import yaml
from converter import fetch_subscription, convert_nodes

def load_config(config_file='config/example_config.yml'):
    """加载配置文件，指定 UTF-8 编码"""
    with open(config_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def save_output(data, output_file):
    """保存输出到文件"""
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def main():
    config = load_config()
    for sub in config['subscriptions']:
        content = fetch_subscription(sub['url'])
        if content:
            result = convert_nodes(content, sub['type'], config['output_format'])
            if result:
                save_output(result, config['output_file'])
                print(f"转换完成！输出已保存到 {config['output_file']}")

if __name__ == '__main__':
    main()
