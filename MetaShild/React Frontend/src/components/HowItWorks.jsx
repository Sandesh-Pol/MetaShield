import { Link } from "react-router-dom";
export const HowItWorks = () => {
  return (
    <div id='help' className="min-h-screen text-white p-12">
      <h1 className="text-4xl font-bold text-center mb-12">How It Works</h1>
      <div className="flex justify-center">
        <div className="flex flex-col items-start gap-16">
          <div className="flex items-center gap-8">
            <div className="text-6xl">🗂️</div>
            <div>
              <h2 className="text-2xl font-semibold">Upload Your Files</h2>
              <p className="text-gray-400">
                Drag and drop or select files you want to classify securely and
                easily.
              </p>
            </div>
          </div>

          <div className="flex items-center gap-8">
            <div className="text-6xl">🧠</div>
            <div>
              <h2 className="text-2xl font-semibold">AI-Powered Analysis</h2>
              <p className="text-gray-400">
                Our model uses file metadata to determine sensitivity without
                exposing content.
              </p>
            </div>
          </div>

          <div className="flex items-center gap-8">
            <div className="text-6xl">📊</div>
            <div>
              <h2 className="text-2xl font-semibold">Get Instant Results</h2>
              <p className="text-gray-400">
                View sensitivity classification and confidence scores in a clean
                dashboard.
              </p>
            </div>
          </div>
          <Link  to='/upload'>
            <button className="bg-[#12b18b] px-8 py-4 rounded-full font-semibold text-white hover:bg-[#0A8B6C] cursor-pointer">
              Upload Files Now
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};
