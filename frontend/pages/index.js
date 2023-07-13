import dynamic from "next/dynamic";
import Seo from "../components/utils/Seo";
import Home from "../components/home";

const index = () => {
    return (
        <>
            <Seo pageTitle="Home" />
            <Home />
            
        </>
    );
};



export default dynamic(() => Promise.resolve(index), { ssr: false });
