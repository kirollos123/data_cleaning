# NYC 311 — Business Questions to Columns Mapping

## 1. Purpose

This document maps the business questions defined for the NYC 311 project to the dataset columns required to answer them.

The mapping helps identify:
- Required columns.
- Relationships between columns.
- Potential data quality issues.
- Analytical limitations.

## 2. Business Questions Mapping

### A. Request Volume & Problem Types

**Q1. What are the most common reported problems in NYC?**

Required columns:
- Problem
- Problem Detail
- Additional Details
- Unique Key

Potential checks:
- Missing problem classifications.
- Inconsistent category names.
- Duplicate service request identifiers.
- Changes in category values over time.

**Q2. How does request volume change over time?**

Required columns:
- Unique Key
- Created Date
- Problem

Potential checks:
- Invalid dates.
- Missing creation dates.
- Unexpected date ranges.
- Duplicate records.

### B. Agency Workload

**Q3. Which agencies receive the highest number of service requests?**

Required columns:
- Agency
- Agency Name
- Unique Key
- Created Date

Potential checks:
- Missing agency values.
- Inconsistent agency codes and names.
- Unexpected agency categories.
- Duplicate requests.

**Q4. How does workload vary by agency over time?**

Required columns:
- Agency
- Agency Name
- Created Date
- Unique Key

Potential checks:
- Agency naming consistency.
- Date validity.
- Missing values.

### C. Resolution & Response Time

**Q5. How long does it take to close a service request?**

Required columns:
- Created Date
- Closed Date
- Unique Key
- Status

Potential checks:
- Missing closing dates.
- Closing date earlier than creation date.
- Invalid date formats.
- Requests that are not closed.

Derived metric:
Resolution Time = Closed Date - Created Date.

**Q6. Which problem types take the longest to resolve?**

Required columns:
- Problem
- Problem Detail
- Created Date
- Closed Date
- Status
- Unique Key

Potential checks:
- Invalid resolution durations.
- Missing problem classifications.
- Inconsistent problem categories.

**Q7. How does resolution time vary across agencies?**

Required columns:
- Agency
- Agency Name
- Created Date
- Closed Date
- Status
- Unique Key

Potential checks:
- Missing agency information.
- Invalid timestamps.
- Unusually long resolution durations.

### D. Geographic Distribution

**Q8. Which boroughs have the highest number of service requests?**

Required columns:
- Borough
- Unique Key
- Problem

Potential checks:
- Missing borough values.
- Inconsistent borough names.
- Unexpected geographic values.

**Q9. Which ZIP codes or community districts have the highest request volume?**

Required columns:
- Incident Zip
- Community Board
- Borough
- Unique Key

Potential checks:
- Invalid ZIP code formats.
- Missing geographic identifiers.
- Inconsistent community board formats.

**Q10. Where are service requests geographically concentrated?**

Required columns:
- Latitude
- Longitude
- Location
- Borough
- Unique Key

Potential checks:
- Missing coordinates.
- Invalid latitude and longitude ranges.
- Inconsistent location information.
- Coordinates outside the expected NYC geographic area.

### E. Request Characteristics

**Q11. Which channels are most commonly used to submit requests?**

Required columns:
- Open Data Channel Type
- Created Date
- Unique Key

Potential checks:
- Missing channel values.
- Unexpected channel categories.
- Inconsistent category formatting.

**Q12. What is the distribution of request statuses?**

Required columns:
- Status
- Agency
- Problem
- Unique Key

Potential checks:
- Missing status values.
- Unexpected status categories.
- Inconsistent status formatting.

## 3. Column Priority

### High Priority

These columns support the main analytical questions:

- Unique Key
- Created Date
- Closed Date
- Agency
- Agency Name
- Problem
- Problem Detail
- Status
- Borough
- Incident Zip
- Community Board
- Latitude
- Longitude
- Open Data Channel Type

### Medium Priority

These columns provide additional analytical detail:

- Additional Details
- Due Date
- Resolution Action Updated Date
- Resolution Description
- Council District
- Police Precinct
- Location Type
- City
- Location

### Specialized Fields

These fields may be relevant to specific problem categories:

- Facility Type
- Park Facility Name
- Park Borough
- Vehicle Type
- Taxi Company Borough
- Taxi Pick Up Location
- Bridge Highway Name
- Bridge Highway Direction
- Road Ramp
- Bridge Highway Segment

Other address-related fields should also be retained until their usefulness and quality are investigated.

## 4. Important Analytical Considerations

1. Request volume represents reported service requests, not an objective measurement of problem severity.
2. Resolution time can only be calculated when valid creation and closing timestamps are available.
3. Open or canceled requests should not automatically be treated as completed requests.
4. Geographic comparisons require consistent and sufficiently complete location information.
5. Agency workload comparisons should account for differences in agency responsibilities and request types.
6. A high-priority column is not automatically a clean or reliable column.

## 5. Validation Status

This mapping is preliminary.

The following must be verified before analysis:

- Actual technical column names.
- Actual data types.
- Missing-value patterns.
- Uniqueness of Unique Key.
- Validity of date fields.
- Relationships between Problem and Problem Detail.
- Geographic consistency.
- Availability of required columns in the downloaded dataset.