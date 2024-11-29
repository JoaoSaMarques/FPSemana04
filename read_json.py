import json
import sys

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            print(data)
    except UnicodeDecodeError:
        print("Erro de decodificação! O arquivo pode não estar em UTF-8.")
    except Exception:
        print("Ocorreu um erro!")
    finally:
        print("Processo concluído!")

if len(sys.argv) != 2:
    print("Uso: python read_json.py <caminho_para_o_arquivo_json>")
else:
    read_json(sys.argv[1])