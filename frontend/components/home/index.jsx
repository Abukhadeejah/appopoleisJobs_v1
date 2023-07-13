import Header from './Header';
import Hero from "../hero";
import Footer from './Footer';

import Link from 'next/link';

const index = () => {
    return (
        <>
            <Header />
            {/* <!-- End of Main Header --> */}

            <Hero />
            {/* <!-- End of Hero Section --> */}

            <Footer />
            {/* <!-- End Main Footer --> */}
        
        </>
        
    )
}

export default index;