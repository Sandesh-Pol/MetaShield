export const ClassificationDashboard = ({ files }) => {
  return (
    <div className="min-h-screen text-white p-8 mt-20 flex items-center w-full">
      <div className="bg-[#2b2e35] p-6 rounded-2xl mb-8 border border-[#12b18b] border-2 w-full">
        <h2 className="text-2xl font-semibold mb-4">Classification Results </h2>
        {files.length === 0 ? (
          <p className="text-gray-400 text-center">No files uploaded yet.</p>
        ) : (
          <table className="w-full text-left">
            <thead>
              <tr>
                <th className="p-2">File Name</th>
                <th className="p-2">Sensitivity</th>
              </tr>
            </thead>
            <tbody>
              {files.map((file, index) => (
                <>
                  <tr key={index} className="border-t border-gray-700">
                    <td className="p-2">{file.Filename}</td>
                    <td
                      className={`p-2 ${
                        file.status ? "text-red-400" : "text-green-400"
                      }`}
                    >
                      {file.Predicted}
                    </td>
                  </tr>
                  <td colSpan="2" className="text-center py-5">
                    <div className={`text-3xl font-bold text-white mt-5 py-2 rounded-xl ${file.status ?" bg-red-400" : "bg-green-400"}`}>
                      File is {file.Predicted}
                    </div>
                  </td>
                </>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};
