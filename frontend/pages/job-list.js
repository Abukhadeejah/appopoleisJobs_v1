import Seo from "../components/utils/Seo";
import axios from 'axios';

import Jobs from '../components/job-listing';

export default function Index({ data }) {
  return (
    <>
      <Seo pageTitle="Job List" />
      <Jobs data={data} />
    </>

  )
}

export async function getServerSideProps() {
  
  const res = await axios.get(`${process.env.API_URL}/api/jobs/`);
  const data = res.data;

  return {
    props: {
      data,
    }
  }
}