import { useState } from "react";
import uploadIcon from "../assets/svg/uploadIcon.svg";
import uploadIllustrtation from "../assets/images/uploadIllustrtation.png";

export const UploadSection = ({ onFileUpload, loading, message }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  const handleUpload = () => {
    if (selectedFile) {
      onFileUpload(selectedFile);
    }
  };

  return (
    <div className="flex mt-10">
      <div className="w-1/2 illustration">
        <img className="w-full" src={uploadIllustrtation} alt="" />
      </div>
      <div className="w-1/2 upload-section flex flex-col items-center justify-center gap-10">
        <div className="upload-container flex justify-center items-center relative size-80 overflow-hidden cursor-pointer border-dashed border-white border-2">
          <input
            className="z-20 absolute w-full h-full opacity-0"
            type="file"
            name="file"
            onChange={handleFileChange}
          />
          {selectedFile ? (
            <div className="text-white absolute text-center">
              <p>{selectedFile.name}</p>
              <p className="text-sm text-gray-400">
                {(selectedFile.size / 1024).toFixed(2)} KB
              </p>
            </div>
          ) : (
            <>
              <img className="w-20 z-10" src={uploadIcon} alt="Upload Icon" />
              <div className="text-white absolute bottom-20">
                Drag files here or click to upload
              </div>
            </>
          )}
        </div>
        <a href="#ClassificationDashboard">
          <button
            className="bg-[#12b18b] text-base w-40 h-10 rounded-full font-semibold text-white hover:bg-[#0A8B6C] cursor-pointer"
            onClick={handleUpload}
            disabled={loading}
          >
            {loading ? "Uploading..." : "Upload Now"}
          </button>
        </a>
        {message && (
          <p
            className={
              message.includes("❌") ? "text-red-400" : "text-green-400"
            }
          >
            {message}
          </p>
        )}
      </div>
    </div>
  );
};
