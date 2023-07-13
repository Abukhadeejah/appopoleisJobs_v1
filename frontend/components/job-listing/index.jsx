import React from 'react'
import FooterDefault from "../footer/common-footer/";
import Breadcrumb from '../utils/Breadcrumb';

import JobItem from './JobItem';

const index = ({ data }) => {

    const { jobs, count, resPerPage } = data;
  return (
    <>
    <Breadcrumb title="Find Jobs" meta="Jobs" />
    {/* <-- End Breadcrumb --> */}

    <section className="ls-section">
        <div className="auto-container">
            <div className="row">
                <div
                    className="offcanvas offcanvas-start"
                    tabIndex="-1"
                    id="filter-sidebar"
                    aria-labelledby="offcanvasLabel"
                >
                    <div className="filters-column hide-left">
                        {/* <FilterSidebar /> */}
                    </div>
                </div>
                {/* End filter column for tablet and mobile devices */}

                <div className="filters-column hidden-1023 col-lg-4 col-md-12 col-sm-12">
                    {/* <FilterSidebar /> */}
                </div>
                {/* <!-- End Filters Column for desktop and laptop --> */}

                <div className="content-column col-lg-8 col-md-12 col-sm-12">
                    <div className="ls-outer">
                        {/* <FilterJobsBox /> */}
                        {jobs && jobs.map((job) => <JobItem key={job.id} job={job} />) }
                        {/* <!-- ls Switcher --> */}
                    </div>
                </div>
                {/* <!-- End Content Column --> */}
            </div>
            {/* End row */}
        </div>
        {/* End container */}
    </section>
    {/* <!--End Listing Page Section --> */}

    <FooterDefault footerStyle="alternate5" />
    {/* <!-- End Main Footer --> */}
    </>
  )
}

export default index;