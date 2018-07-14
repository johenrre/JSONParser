from token_parser import json_tokens

def load_file(path):
    with open(path) as f:
        return f.read()

def write_file(path, content):
    with open(path) as f:
        f.write(content)

def main():
    pathLoad = 'codes.json'
    codes = load_file(pathLoad)
    ts = json_tokens(codes)
    print('test', ts)

if __name__ == '__main__':
    main()
