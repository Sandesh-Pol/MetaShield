import { useState } from "react";
import { Navbar } from "./Navbar";
import { UploadSection } from "./UploadSection";
import { ClassificationDashboard } from "./ClassificationDashboard";

export const UploadPage = () => {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleFileUpload = async (selectedFile) => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    setLoading(true);
    setMessage(""); 

    try {
      const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to upload file');
      }

      const data = await response.json();
      setFiles([data]);
      console.log(data)
      setMessage("File uploaded successfully! ✅");
      const dashboard = document.getElementById("classification-dashboard");
      if (dashboard) {
        dashboard.scrollIntoView({ behavior: "smooth" });
      }
    } catch (error) {
      console.error('Upload failed:', error);
      setMessage("Failed to upload file. ❌ Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="px-28 py-5">
      <Navbar />
      <UploadSection 
        onFileUpload={handleFileUpload} 
        loading={loading}
        message={message}
      />
      <div id="classification-dashboard">
        <ClassificationDashboard files={files} />
      </div>
    </div>
  );
};
