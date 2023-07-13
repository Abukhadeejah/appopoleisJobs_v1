import Link from 'next/link';
import moment from 'moment';

const JobItem = ({ job }) => {
    return (
        (<Link href={`/jobs/${job.id}`} className="job-block" passHref>

            <div className='inner-box'>
                <div className='content'>
                    <span className='company-logo'>
                        <img src="images/logo-2.svg" alt='item-brand' />
                    </span>
                    <h4>{job.title}</h4>
                    {/* <a href={`/jobs/${job.id}`}>{job.title}</a> */}

                    <ul className="job-info">
                            <li>
                                <span className="icon flaticon-briefcase" aria-hidden="true"></span>
                                {job.company}
                            </li>
                            {/* company info */}
                            <li>
                                <span className="fas fa-industry" aria-hidden="true"></span>
                                {job.industry}
                            </li>
                            {/* industry info */}
                            <li>
                                <span className="icon flaticon-map-locator" aria-hidden="true"></span>
                                {job.location}
                            </li>
                            {/* location info */}
                            <li>
                                <span className="icon flaticon-clock-3" aria-hidden="true"></span>{" "}
                                {moment.utc(job.createdAt).local().startOf("seconds").fromNow()}
                            </li>
                            {/* time info */}
                            <li>
                                <span className="icon flaticon-money" aria-hidden="true"></span>{" "}
                                {job.salary}
                            </li>
                            {/* salary info */}                         
                    </ul>
                    {/* End .job-info */}
                    <ul className="job-other-info">
                        <li>
                            {job.job_type}
                        </li>                        
                    </ul>
                    {/* End .job-other-info */}

                    <button className="bookmark-btn">
                        <span className="flaticon-bookmark"></span>
                    </button>
                </div>
            </div>
            {/* <-- End of all jobs --> */}
        </Link>)
    )
};

export default JobItem;