export const Footer = () => {
    return (
      <footer className="text-white py-6 mt-10 border-t border-white">
        <div className="container mx-auto flex flex-col items-center">
          <p className="text-lg font-semibold">Metashield</p>
          <p className="text-gray-400">Your trusted AI-powered document classifier</p>
  
          <div className="flex gap-8 mt-4">
            <a href="/" className="hover:text-[#12b18b] transition">Home</a>
            <a href="/#features" className="hover:text-[#12b18b] transition">Features</a>
            <a href="/#help" className="hover:text-[#12b18b] transition">Help</a>
          </div>
  
          <div className="mt-4 text-gray-500">&copy; {new Date().getFullYear()} Metashield. All rights reserved.</div>
        </div>
      </footer>
    );
  };
  