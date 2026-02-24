# Job Board Skill Aggregator

# Why?

I want to answer a simple but important question of: "What skills do I need for this job?"

# Goals

* Scrape job boards for multiple jobs
* Collect the most common skills listed
* Create a dashboard that shows this in an easy-to-understand way
* Allow results to be exported as PDF
* Showcase web scraping best practices

# Is this going to be perfect?

No. Sometimes job listings are more of a "wish list" than actual requirements for the job.

# Job boards

| Job Board | Status |
|-----------|--------|
| Indeed | 🚀 In Progress |
| Hiring Cafe | ❌ Not Implemented Yet |
| Y Combinator | ❌ Not Implemented Yet |
| hnhiring | ❌ Not Implemented Yet |
| LinkedIn Jobs | ❌ Not Implemented Yet |
| Wellfound | ❌ Not Implemented Yet |

# How to run the project(currently work in progress/beta)

1. Clone repo
```bash
git clone https://github.com/Jhonatan-de-Souza/Job-Skills-Aggregator.git
```

2. Install requirements
```python
pip install requirements.txt
```
3. run src/main.py file
```python
python .\src\main.py
```

# Tech stack

**Language & Framework:**
- Python 3.12
- PySide6 - Qt framework for GUI

**Web Scraping:**
- Playwright - Modern browser automation (synchronous API)
- SeleniumBase - Undetected Chrome for anti-detection

**Database:**
- SQLite3 - Lightweight database for storing job data

**Visualization**
- Seaborn - Data visualization(not yet implemented)

