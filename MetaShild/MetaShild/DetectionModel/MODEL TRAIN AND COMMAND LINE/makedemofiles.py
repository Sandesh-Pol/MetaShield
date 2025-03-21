import os
from random import choice
from datetime import datetime

os.makedirs('./test', exist_ok=True)

file_metadata = combined_records = [
    {'file_extension': 'pdf', 'filename': 'Aadhaar_Original.pdf', 'size_kb': 2577.32, 'page_count': 93, 'esign': 'Adobe.PPKLite'},
    {'file_extension': 'pdf', 'filename': 'PAN.pdf', 'size_kb': 4454.21, 'page_count': 66, 'esign': 'Adobe.PPKLite'},
    {'file_extension': 'png', 'filename': 'VoterID_Scan.png', 'size_kb': 1056.95, 'page_count': 381, 'esign': 'SignEasy'},
    {'file_extension': 'xlsx', 'filename': 'BankStatement_Original.xlsx', 'size_kb': 3717.58, 'page_count': 87, 'esign': 'Nitro Pro'},
    {'file_extension': 'xlsx', 'filename': 'Newsletter_Final.xlsx', 'size_kb': 1399.48, 'page_count': 256, 'esign': 'DocuSign'},
    {'file_extension': 'pdf', 'filename': 'Magazine_Final.pdf', 'size_kb': 2324.68, 'page_count': 500, 'esign': 'Adobe.PPKLite'},
    {'file_extension': 'docx', 'filename': 'Article_Draft.docx', 'size_kb': 1485.65, 'page_count': 315, 'esign': 'SignEasy'}
]

def create_file(file_path, size_kb, file_extension):
    target_size = size_kb * 1024
    with open(file_path, 'wb') as f:
        while f.tell() < target_size:
            f.write(choice([b"A", b"B", b"C", b"D", b"E"]))
        print(f"Created {file_path} with size {size_kb} KB")

for metadata in file_metadata:
    file_name = metadata["filename"]
    file_extension = metadata["file_extension"]
    file_size = metadata["size_kb"]
    page_count = metadata["page_count"]
    esign = metadata["esign"]
    file_path = os.path.join('./test', file_name)
    
    create_file(file_path, file_size, file_extension)
    
    with open(file_path, 'a') as f:
        f.write(f"\n--- Metadata ---\n")
        f.write(f"Filename: {file_name}\n")
        f.write(f"Size: {file_size} KB\n")
        f.write(f"Page Count: {page_count}\n")
        f.write(f"eSign Producer: {esign}\n")
        f.write(f"Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"Metadata added to {file_name}")

print("All files created successfully!")
