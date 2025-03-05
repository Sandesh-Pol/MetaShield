export const FeatureCard = ({icon,title,desc}) => {
  return (
    <>
      <div className="w-64 h-68 bg-[#2b2e35] text-white rounded-xl py-3 px-3 shadow-2xl">
        <div className="title text-lg font-bold flex gap-1"><img className="w-8" src={icon} alt="" />{title}</div>
        <div className="desc text-sm text-justify mt-3 px-2">
         {desc}
        </div>
      </div>
    </>
  );
};
