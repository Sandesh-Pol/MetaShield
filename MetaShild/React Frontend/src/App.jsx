import { Routes, Route } from "react-router-dom";
import { HeroSect } from "./components/HeroSect";
import { KeyFeatures } from "./components/KeyFeatures";
import { HowItWorks } from "./components/HowItWorks";
import { Footer } from "./components/Footer";
import { UploadPage } from "./components/UploadPage";
function App() {
  return (
    <>
      <Routes>
        <Route
          path="/"
          element={
            <>
              <HeroSect />
              <KeyFeatures />
              <HowItWorks />
              <Footer />
            </>
          }
        />
        <Route path="/upload" element={<UploadPage/>} />
      </Routes>
    </>
  );
}

export default App;
