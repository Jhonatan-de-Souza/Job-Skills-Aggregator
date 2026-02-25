import sys
from PySide6.QtWidgets import QApplication
from ui.gui import JobSearchWindow
from scrapers.indeed_scraper import start_indeed_scraper

def handle_job_search(job_title):
    start_indeed_scraper(job_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = JobSearchWindow(callback=handle_job_search)
    window.show()
    sys.exit(app.exec())