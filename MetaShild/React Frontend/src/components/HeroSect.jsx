import { Navbar } from "./Navbar";
import { HeroContent } from "./HeroContent"
export const HeroSect = () => {
  return (
    <>
      <div className="px-28 py-5">
        <Navbar />
        <HeroContent/>
      </div>
    </>
  );
};
