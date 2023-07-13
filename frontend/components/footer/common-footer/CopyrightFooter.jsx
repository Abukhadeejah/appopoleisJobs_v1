import Link from "next/link";
import Social from "../footer/common-footer/Social";

const CopyrightFooter = () => {
  return (
    <div className="footer-bottom">
      <div className="auto-container">
        <div className="outer-box">
          <div className="bottom-left">
            <div className="logo">
              <Link href="/">
                <img src="images/logo.svg" alt="brand" />
              </Link>
            </div>
            <div className="copyright-text">
            © {new Date().getFullYear()} Appopoleis. All Rights Reserved.
            </div>
          </div>

          <div className="social-links">
            <Social />
          </div>
        </div>
      </div>
    </div>
  );
};

export default CopyrightFooter;
