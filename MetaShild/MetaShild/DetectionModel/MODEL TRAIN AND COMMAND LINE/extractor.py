import os
import subprocess
import json

def get_metadata(file_path):
    try:
        result = subprocess.run([
            'exiftool', '-j', file_path
        ], capture_output=True, text=True)
        
        metadata_list = json.loads(result.stdout) if result.stdout else []
        metadata = metadata_list[0] if metadata_list else {}
        
        file_extension = os.path.splitext(file_path)[1][1:] or "Unknown"
        filename = os.path.basename(file_path) or "Unknown"
        size_kb = round(os.path.getsize(file_path) / 1024, 2) if os.path.exists(file_path) else "Unknown"
        page_count = metadata.get('PageCount', 10)  # Set to 10 if not found
        esign = metadata.get('DigitalSignature', "Unknown")
        
        return {
            'file_extension': file_extension,
            'filename': filename,
            'size_kb': size_kb,
            'page_count': page_count,
            'esign': esign
        }
    except Exception as e:
        return {
            'file_extension': "Unknown",
            'filename': os.path.basename(file_path),
            'size_kb': 10,
            'page_count': 10,
            'esign': "Unknown"
        }

def process_files(directory):
    metadata_list = []
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            metadata_list.append(get_metadata(file_path))
    
    return metadata_list

if __name__ == "__main__":
    directory = "./test"
    metadata_results = process_files(directory)
    for metadata in metadata_results:
        print(metadata)
