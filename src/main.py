import sys
from PySide6.QtWidgets import QApplication
from ui.gui import JobSearchWindow
from scrapers.indeed_scraper import scrape_jobs

def handle_job_search(job_title):
    """Called when user clicks search in GUI"""
    print(f"🔍 Searching for: {job_title} jobs")
    
    try:
        # Call your backend scraper
        jobs = scrape_jobs(job_title)
        print('scraping done')
    except Exception as e:
        print(f"Automation failed, please check error logs")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = JobSearchWindow(callback=handle_job_search)
    window.show()
    sys.exit(app.exec())