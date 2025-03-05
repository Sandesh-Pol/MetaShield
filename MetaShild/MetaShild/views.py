import os
import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from MetaShild.DetectionModel import testmodel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@csrf_exempt  # Correct way for function-based views
def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        print("Received file:", uploaded_file.name)  # Debugging

        # Save file temporarily
        try:
            file_path = default_storage.save(f"temp/{uploaded_file.name}", ContentFile(uploaded_file.read()))
            full_file_path = default_storage.path(file_path)
        except Exception as e:
            return JsonResponse({"error": f"File saving failed: {str(e)}"}, status=500)

        # Extract metadata
        try:
            metadata = get_metadata(full_file_path)
        except Exception as e:
            default_storage.delete(file_path)  # Cleanup
            return JsonResponse({"error": f"Metadata extraction failed: {str(e)}"}, status=500)

        # Delete file after processing
        default_storage.delete(file_path)

        print("Extracted Metadata:", metadata)  # Debugging

        result = testmodel.predict(metadata)
        if result.get("Predicted") == "Sensitive":
            result['status'] = True
        else:
            result['status'] = False
            
        print(result)
        
        response = JsonResponse(result)
        
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return JsonResponse({"error": "Invalid request. Please upload a file."}, status=400)


def get_metadata(file_path):
    """ Extract metadata from the file using ExifTool """
    try:
        result = subprocess.run(['exiftool', '-j', file_path], capture_output=True, text=True)
        metadata_list = json.loads(result.stdout) if result.stdout else []
        metadata = metadata_list[0] if metadata_list else {}

        file_extension = os.path.splitext(file_path)[1][1:] or "Unknown"
        filename = os.path.basename(file_path) or "Unknown"
        size_kb = round(os.path.getsize(file_path) / 1024, 2) if os.path.exists(file_path) else "Unknown"
        page_count = metadata.get('PageCount', 10)  # Default to 10 if not found
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
