# NYC 311 Service Requests — Business Questions

## 1. Business Context

New York City receives service requests from residents through its 311 system. These requests cover a wide range of problems and are handled by different agencies.

This project will use the **311 Service Requests from 2020 to Present** dataset to understand the types of problems being reported, how requests are handled, how long they take to close, and how patterns vary across time and geography.

## 2. Main Business Objective

**Analyze NYC 311 service requests to identify the most frequently reported problems, understand agency workload and request-resolution performance, and explore how service requests vary across time and geographic areas.**

The analysis should produce reliable, clearly documented data that can support operational insights and further analytics.

## 3. Business Questions

### A. Request Volume and Problem Types

1. What are the most frequently reported problems in New York City?
2. What proportion of all requests does each problem type represent?
3. Which problem types have increased or decreased over time?
4. Are there problem types that occur more frequently during particular months or seasons?

### B. Agency Workload

5. Which agencies receive the highest number of service requests?
6. What types of problems are most commonly assigned to each agency?
7. Are some agencies responsible for a wide variety of problem types while others handle a narrower set?
8. How does the volume of requests assigned to each agency change over time?

### C. Request Resolution and Response Time

9. What is the typical time required to close a service request?
10. How does closure time vary by problem type?
11. How does closure time vary by agency?
12. What percentage of requests are still open or have no recorded closure date?
13. Are there problem types or agencies associated with unusually long closure times?

### D. Geographic Distribution

14. Which ZIP codes or geographic areas generate the highest number of service requests?
15. Which problem types are most common in different areas?
16. Do some areas experience a higher concentration of particular problems?
17. How does the geographic distribution of requests change over time?

### E. Data Reliability and Quality

18. Are request identifiers unique and populated?
19. Are creation and closure dates valid and logically consistent?
20. Are there missing or inconsistent values in important fields such as agency, problem type, ZIP code, and status?
21. Are there duplicate or potentially duplicated service requests?
22. Do category values and agency names remain consistent over time, or have their labels and definitions changed?

## 4. Initial Analysis Priorities

The project will not necessarily answer every question in the first analysis. The initial priorities are:

1. Understand the dataset structure, fields, and limitations.
2. Measure request volume by problem type and agency.
3. examine creation and closure dates and calculate closure duration where valid.
4. Explore geographic coverage using available location fields.
5. Assess data quality before drawing conclusions.

## 5. Important Definitions and Rules

- **Service request:** One record representing a request submitted through the NYC 311 system.
- **Request identifier:** The `unique_key` field, which is expected to identify a request.
- **Creation time:** The `created_date` field.
- **Closure time:** The `closed_date` field, when available.
- **Closure duration:** The elapsed time between `created_date` and `closed_date`, calculated only when both timestamps are valid and the result is logically consistent.
- **Problem type:** The `complaint_type` field in the dataset's technical schema. The public-facing label may appear as **Problem**.
- **Problem detail:** The `descriptor` field in the technical schema. The public-facing label may appear as **Problem Detail**.

## 6. Analytical Cautions

- A high number of requests does not automatically mean an area is less safe or that an agency performs poorly. Request volume may be affected by population, awareness of 311, reporting behavior, and other factors.
- Average closure time can be distorted by unusually long cases. Use the median and inspect the distribution as well.
- Open requests must not be treated as completed requests when calculating closure duration.
- Missing values should not be filled automatically. First investigate why values are missing and whether the field is required for the intended analysis.
- Category labels and dataset fields may change over time. Check the current data dictionary and document any changes that affect comparisons.
- Geographic analysis depends on the completeness and accuracy of the available location fields.
- Findings describe the available 311 records; they do not necessarily represent every problem experienced by NYC residents.

## 7. Scope and Future Extensions

After the initial analysis and data-quality assessment, the project may be extended to:

- Compare request patterns across community districts or other geographic boundaries, if reliable geographic fields are available.
- Build a time-series view of request volume and closure duration.
- Create agency and problem-type performance summaries.
- Develop a repeatable data pipeline that retrieves, profiles, cleans, validates, and stores updated data.

## 8. Source

**Dataset:** NYC Open Data — 311 Service Requests from 2020 to Present  
**Dataset page:** https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data

The dataset and its data dictionary should be checked again during implementation because the source is updated and its fields or category values may change.
