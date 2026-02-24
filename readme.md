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

- Wellfound - http://wellfound.com/
- Y Combinator - https://www.ycombinator.com/jobs
- hnhiring - https://hnhiring.com/
- Hiring Cafe - https://hiring.cafe/
- Indeed - https://indeed.com/
- LinkedIn Jobs - https://www.linkedin.com/jobs/

# Credentials you need to provide for this to work

- You will need to log in to each of these websites using the provided browser.
- Many of these websites only allow access (scraping) when you are logged in (LinkedIn, for example).
- This is safe: data will be stored locally and the folder containing it won't be pushed to GitHub.
- OpenAI API key (to better rank the skills).