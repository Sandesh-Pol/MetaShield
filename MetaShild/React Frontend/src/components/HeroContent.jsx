import heroImage from "../assets/images/heroImage.png";
import { Link } from "react-router-dom";
export const HeroContent = () => {
  return (
    <>
      <div className="flex h-full w-full mt-28">
        <div className="text-section h-full w-1/2 gap-5 flex flex-col justify-center">
          <div className="hero-title anta text-white text-5xl leading-14">
            The Ultimate <br /> AI-Powered Document <br /> Security Platform
          </div>
          <div className="hero-subtitle subtitle text-lg">
            AI-driven metadata classification for faster, smarter, and more
            secure file management — no content exposure, just results.
          </div>
          <div className="buttons font-bold flex gap-5 mt-3">
            <Link to='/upload'>
              <button className="bg-[#12b18b] text-base w-40 h-10 rounded-full uppercase text-white hover:bg-[#0A8B6C] cursor-pointer">
                Get Started
              </button>
            </Link>
            <button className="border-2 border-[#12b18b] text-base text-[#12b18b] w-52 h-10 rounded-full uppercase hover:bg-[#12b18b] hover:text-white cursor-pointer">
              Explore Features
            </button>
          </div>
          <div className="btn-color blur-[100px] size-28 absolute bottom-0 left-0"></div>
        </div>
        <div className="illustration w-1/2">
          <img className="w-5/6" src={heroImage} alt="" />
          <div className="btn-color blur-[100px] size-32 absolute top-40 right-0"></div>
        </div>
      </div>
    </>
  );
};
