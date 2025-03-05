import { Link } from "react-router-dom";
import logo from "../assets/images/logo.png";
export const Navbar = () => {
  return (
    <>
      <div className="Navbar-container flex justify-between items-center text-white sora">
        <div className="logo">
          <img className="w-60" src={logo} alt="" />
        </div>
        <div className="menu-items flex gap-[5rem]">
          <Link to="/" className="menu-item cursor-pointer hover:subtitle">
            Home
          </Link>
          <a
            href="/#features"
            className="menu-item cursor-pointer hover:subtitle"
          >
            Features
          </a>
          <a href="/#help" className="menu-item cursor-pointer hover:subtitle">
            Help
          </a>
        </div>
      </div>
    </>
  );
};
