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
3. Install google chrome(not needs for playwright but seleniumbase needs it)

4. run src/main.py file
```python
python .\src\main.py
```
## Project architecture

This project follows a simple layered (clean) architecture so each part is easy to understand, test and replace.

Structure (compact):

```
src/
├─ scrapers/        # site-specific scrapers and automation (Playwright + SeleniumBase)
├─ data/            # domain models (dataclasses) e.g. Job
├─ database/        # sqlite helpers, schema creation, save functions
├─ ui/              # PySide6 GUI components (windows, widgets)
├─ utils/           # small reusable helpers (sleep_random, formatters)
└─ visualization/   # plotting/dashboard code (seaborn, charts)
└─ tests/           # application tests
└─ html/            # static HTML fixtures used during development and tests

.env/                # virtual environment (not committed)
readme.md            # this file — overview and run instructions
requirements.txt     # Python dependencies (Playwright, PySide6, etc.)
```

Why this layout? Each folder maps to a single responsibility (UI, scraping, data, persistence, helpers). That makes it easier to test units in isolation and update a single concern when requirements change.

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

## FAQ

<details>
<summary>The scraper stopped working on X site</summary>

html on mordern website changes fast, if you don't see a recent commit, there a chance the locators are used are not longer valid and need to be updated.

</details>

<details>
<summary>I want to contribute, how can I do that?</summary>
Just open a PR and I'll review it when i get a chance. Please make sure you don't try to push AI slop into the codebase:
<br>
<br>
I use AI too, but try to review the code you push and avoid 3000 lines of comments in your code(llms love this)

</details>