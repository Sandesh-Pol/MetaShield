import { FeatureCard } from "./FeatureCard";
import icon1 from "../assets/svg/shield-lock.svg"
import icon2 from "../assets/svg/lightning-bolt.svg"
import icon3 from "../assets/svg/artificial-intelligence-assistant.svg"
import icon4 from "../assets/svg/security-shield.svg"
export const KeyFeatures = () => {
  return (
    <>
      <div id='features' className="mt-10 flex flex-col items-center w-full px-28 h-screen relative">
        <div className="title anta text-white text-5xl mt-10">Key Features</div>
        <div className="bg-[#12b18b] blur-[100px] size-28 absolute bottom-0 right-0 -z-10"></div>
        <div className="feature-cards w-full py-10 mt-20 flex gap-7">
          <FeatureCard
            icon={icon1}
            title={"Advanced Security"}
            desc={
              "Keep your data safe with state-of-the-art encryption and privacy measures. Our platform ensures no content exposure, so your sensitive information remains protected at all times. With robust security protocols, you can trust that your documents are in good hands."
            }
          />
          <FeatureCard
            icon={icon2}
            title={"Instant Classification"}
            desc={
              "Say goodbye to manual document sorting! Our AI-driven system automates and accelerates the classification process, reducing the time spent on organization and management. Boost productivity without sacrificing accuracy."
            }
          />
          <FeatureCard
            icon={icon3}
            title={"AI-Powered Accuracy"}
            desc={
              "Leverage the power of advanced machine learning to achieve high-confidence metadata classification. Our AI models are trained to understand and categorize documents with incredible precision, minimizing errors and optimizing your workflow."
            }
          />
          <FeatureCard
            icon={icon4}
            title={"Seamless Integration"}
            desc={
              "Easily connect our platform with your existing tools and workflows. Whether you’re using cloud storage, CRM systems, or custom databases, our flexible integration capabilities ensure a smooth and hassle-free experience."
            }
          />
        </div>
      </div>
    </>
  );
};
