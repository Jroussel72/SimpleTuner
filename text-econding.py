import os
import chardet

def convert_to_utf8(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'rb') as f:
                        raw = f.read()
                        result = chardet.detect(raw)
                        encoding = result['encoding']
                    
                    if encoding.lower() != 'utf-8':
                        print(f"Converting {file} from {encoding} to utf-8")
                        text = raw.decode(encoding)
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(text)
                except Exception as e:
                    print(f"Failed to process {path}: {e}")

# Change this to your dataset folder path
convert_to_utf8("/home/jorgeroussel/SimpleTuner/datasets/my-dataset")
