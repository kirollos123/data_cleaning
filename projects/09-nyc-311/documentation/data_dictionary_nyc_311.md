# NYC 311 — Data Dictionary

## 1. Dataset Information

| Attribute | Description |
|---|---|
| Dataset Name | 311 Service Requests from 2020 to Present |
| Data Provider | NYC 311 |
| Unit of Analysis | One 311 Service Request per row |
| Publishing Frequency | Daily |
| Data Change Frequency | Daily |
| Update Schedule | Overnight, with approximately a one-day buffer |
| Dataset Type | Non-emergency, agency-directed service requests |

### Dataset Description

The dataset contains non-emergency service requests submitted by customers across New York City. Requests cover topics including noise, sanitation, and street quality. Each record includes information about the service request, such as its problem type, responding agency, and geographic location.

The publisher states that the dataset does not expose personally identifying information about the customer who submitted the request.

### Data Collection

The dataset describes site-specific, non-emergency complaints (service requests) submitted by customers across NYC. It includes requests that can be directed to specific agencies.

### Update Frequency

The dataset is updated daily, with an approximately one-day publication buffer. For example, data available on Thursday morning may include requests through Tuesday and early Wednesday morning.

### Dataset Limitations

1. The dataset does not include all 311 inquiries.
2. Some inquiries are available in a separate 311 Call Center Inquiry dataset.
3. Requests handled through independent agency customer-service systems may not be included, including certain NYCHA and DOC requests.
4. Complaint counts represent reported complaints, not objective measurements of actual neighborhood conditions.
5. Expected values for many fields may change over time.
6. Published lists of expected values are not necessarily exhaustive.
7. Geographic information has been added through geocoding using GeoSupport and the original street address.
8. The publisher could not verify the complete list of geocoded fields.

### Official Business Use Cases

The publisher suggests exploring:
- Most common problem types by ZIP code or community district.
- Changes in complaints over time.
- Geographic distribution of complaints across NYC.

## 2. Column Inventory and Definitions

**Total columns listed in the supplied dictionary: 44.**

> The names below are the public-facing column labels supplied in the dictionary. Technical API field names must be verified against the live dataset schema before writing queries or code. Data types are not included here because they were not provided in the supplied section.

| # | Column Name | Description | Expected / Allowed Values |
|---:|---|---|---|
| 1 | Unique Key | Unique identifier of a Service Request in the open dataset. Each request is assigned a number that distinguishes it as a separate case. | No allowed-value list supplied. Expected to identify a separate request; uniqueness must be tested. |
| 2 | Created Date | Date and time when a customer submits a Service Request. | `MM/DD/YY HH:MM:SS AM/PM` |
| 3 | Closed Date | Date and time when an agency closes a Service Request. | `MM/DD/YY HH:MM:SS AM/PM` |
| 4 | Agency | Acronym of the responding City Government agency or entity. | Non-exhaustive examples: 311, ACS, AJC, CHALL, DCA, DCP, DEP, DFTA, DHS, DOB, DOE, DOF, DOHMH, DOITT, DOP, DOT, DPR, DSNY, DYCD, EDC, FDNY, HPD, HRA, MOIA, NYCEM, NYCHA, NYPD, OATH, OPS, TLC. |
| 5 | Agency Name | Full name of the responding City Government agency or entity. | Non-exhaustive examples: NYC311; Administration for Children Services; Administrative Justice Coordinator; City Hall; Department of Consumer Affairs; Department of City Planning; Department of Environmental Protection; Department for the Aging; Department of Homeless Services; Department of Buildings; Department of Education; Department of Finance; Department of Health and Mental Hygiene; Department of Information Technology and Telecommunications; Department of Probation; Department of Transportation; Department of Parks and Recreation; Department of Sanitation; Department of Youth and Community Development; Economic Development Corporation; Fire Department of New York; Department of Housing Preservation and Development; Human Resources Administration; Mayor's Office of Immigrant Affairs; NYC Emergency Management; New York City Housing Authority; New York City Police Department; Office of Administrative Trials and Hearings; Mayor's Office of Operations; Taxi and Limousine Commission. |
| 6 | Problem | First level of the hierarchy identifying the topic of the incident or condition. Formerly labelled Complaint Type. Problems are defined by responding agencies, and new ones may be added as customer demand changes. | Requests may be categorized by Problem and Problem Detail, or Problem may stand alone. |
| 7 | Problem Detail | Second level of detail about the Problem; formerly Descriptor. Values depend on Problem and are not always required. | Depends on Problem. May be further explained by Additional Details; not always required. |
| 8 | Additional Details | Third level of detail about the Problem, beyond Problem Detail. Not used by every issue category. | No specific list supplied. |
| 9 | Status | Current status of the submitted service request. | Examples: Assigned, Canceled, Closed, Pending, and additional values (`+`). |
| 10 | Due Date | Date when the responding agency is expected to update the service request, based on the problem type and internal Service Level Agreements (SLAs) between 311 and the agency. | `MM/DD/YY HH:MM:SS AM/PM` |
| 11 | Resolution Action Updated Date | Date when the responding agency last updated the service request. | `MM/DD/YY HH:MM:SS AM/PM` |
| 12 | Resolution Description | Describes the last action taken by the responding agency. May describe next or future steps. | No specific list supplied. |
| 13 | Location Type | Describes the type of location used in the address information. | Non-exhaustive examples: 1-2 Family Dwelling; 1-, 2- and 3-Family Home; 3+ Family Apartment Building; 3+ Family Apt. Building; 3+ Family Mixed Use Building; Above Address; Address; Address Outside of NYC; Address Unknown; Apartment Building; Beach; Bridge; Bridge/Underpass; Bus Stop Shelter; Caller Address; Club/Bar/Restaurant; Co-Op Unit; Commercial; Commercial Building; Common Area; Condo Unit; Construction Site; Crosswalk; Curb; DRIE Tenant's Address; Government/Not-for Profit; Highway; Hospital; House of Worship; Lot; Mixed Use; NYC Street Address; Other; P.O. Box; Park; Park/Playground; Parking Lot/Garage; Pool; Private House; Property Address; Public Park/Garden; Public/Unfenced Area; Recreation Center; Residence; Residential; RESIDENTIAL BUILDING; Residential Building/House; Residential Property; Restaurant/Bar/Deli/Bakery; Roof; School; Senior Address; Sidewalk; Store; Store/Commercial; Street; Street and Sidewalk; Street/Curbside; Street/Sidewalk; Tanning Salon; Tattoo Parlor; Terminal; Vacant Building; Vacant Lot; Vehicle Lane. |
| 14 | Incident Zip | ZIP code of the incident address. | No allowed-value list supplied. |
| 15 | Incident Address | House number and street name of the incident address. | No allowed-value list supplied. |
| 16 | Street Name | Street name of the incident address. | No allowed-value list supplied. |
| 17 | Cross Street 1 | First cross street based on the geo-validated incident location. | No allowed-value list supplied. |
| 18 | Cross Street 2 | Second cross street based on the geo-validated incident location. | No allowed-value list supplied. |
| 19 | Intersection Street 1 | First intersecting street based on the geo-validated incident location. | No allowed-value list supplied. |
| 20 | Intersection Street 2 | Second intersecting street based on the geo-validated incident location. | No allowed-value list supplied. |
| 21 | Address Type | Type of information available about the incident location. | Address; Block face; Intersection; LatLong; Placename. |
| 22 | City | City or locality of the incident location. In this dataset, City may refer to a borough or a neighborhood. | Manhattan, Brooklyn, Bronx, Staten Island, or (in Queens) a specific neighborhood name. |
| 23 | Landmark | If the incident location is identified as a landmark, its name appears here. | May refer to parks, hospitals, airports, sports facilities, performance spaces, and other noteworthy locations. |
| 24 | Facility Type | If applicable, describes the type of city facility associated with the service request. | Blank; DSNY Garage; Precinct; School; School District; N/A. |
| 25 | Community Board | Local representative body. NYC has 59 community boards, each representing a distinct geography. | No allowed-value list supplied in the provided dictionary section. |
| 26 | Council District | City Council district where the service request is located. | No allowed-value list supplied. |
| 27 | Police Precinct | NYPD precinct where the service request is located. | No allowed-value list supplied. |
| 28 | BBL | Parcel identifier for the building or property associated with the request. The block is within a borough; the lot is unique within its borough and block. | Borough number: 1 = Manhattan (New York County); 2 = Bronx (Bronx County); 3 = Brooklyn (Kings County); 4 = Queens (Queens County); 5 = Staten Island (Richmond County). |
| 29 | Borough | One of New York City's five boroughs. | BRONX; BROOKLYN; MANHATTAN; QUEENS; STATEN ISLAND. |
| 30 | X Coordinate (State Plane) | Geo-validated X coordinate of the incident location, in the State Plane coordinate system. | Coordinate system information is referenced by the publisher; no numeric range supplied in this section. |
| 31 | Y Coordinate (State Plane) | Geo-validated Y coordinate of the incident location, in the State Plane coordinate system. | Coordinate system information is referenced by the publisher; no numeric range supplied in this section. |
| 32 | Open Data Channel Type | Indicates how the service request was submitted to 311. | Phone; Online; Other; Unknown. Phone means submitted by a 311 call-center agent on behalf of a customer. Online means submitted through the 311 mobile app. Other means submitted by another city agency or source. Unknown means the source could not be determined. |
| 33 | Latitude | Geo-based latitude of the incident location, in decimal degrees. | No numeric range supplied in this section. |
| 34 | Longitude | Geo-based longitude of the incident location, in decimal degrees. | No numeric range supplied in this section. |
| 35 | Location | Combined geo-based latitude and longitude of the incident location. | No specific format supplied in this section. |
| 36 | Park Facility Name | If a request concerns a NYC Parks Department facility, the facility name appears here. | No allowed-value list supplied. |
| 37 | Park Borough | Borough of the incident when the request concerns a NYC Parks Department facility. | No allowed-value list supplied. |
| 38 | Vehicle Type | Provided when a request concerns a vehicle managed by the Taxi and Limousine Commission (TLC). | Ambulette / Paratransit; Car Service; Commuter Van; Green Taxi. |
| 39 | Taxi Company Borough | Provided when a request concerns a vehicle managed by the TLC. | No allowed-value list supplied. |
| 40 | Taxi Pick Up Location | For a TLC-managed vehicle incident, identifies the taxi pickup location. | Grand Central Station; Intersection; JFK Airport (shown as “JKF Airport” in the supplied dictionary); La Guardia Airport; New York-Penn Station; Other; Port Authority Bus Terminal. |
| 41 | Bridge Highway Name | Name displayed when the incident is identified as a bridge or highway. | No allowed-value list supplied. |
| 42 | Bridge Highway Direction | Direction where the issue occurred when the incident is identified as a bridge or highway. | No allowed-value list supplied. |
| 43 | Road Ramp | Distinguishes whether a bridge/highway issue occurred on the road or ramp. | Roadway; Ramp. |
| 44 | Bridge Highway Segment | Additional information about the section of the bridge/highway where the incident occurred. | No allowed-value list supplied. |

## 3. Preliminary Functional Categories

The following categories are an initial organizational aid, not official dataset classifications.

| Category | Columns |
|---|---|
| Identifier | Unique Key |
| Dates and lifecycle | Created Date; Closed Date; Due Date; Resolution Action Updated Date |
| Agency | Agency; Agency Name |
| Problem classification | Problem; Problem Detail; Additional Details |
| Status and resolution | Status; Resolution Description |
| Address and location description | Location Type; Incident Zip; Incident Address; Street Name; Cross Street 1; Cross Street 2; Intersection Street 1; Intersection Street 2; Address Type; City; Landmark |
| Administrative geography | Community Board; Council District; Police Precinct; BBL; Borough |
| Coordinates | X Coordinate (State Plane); Y Coordinate (State Plane); Latitude; Longitude; Location |
| Request channel | Open Data Channel Type |
| Facility / specialized location | Facility Type; Park Facility Name; Park Borough; Vehicle Type; Taxi Company Borough; Taxi Pick Up Location; Bridge Highway Name; Bridge Highway Direction; Road Ramp; Bridge Highway Segment |

## 4. Initial Data Quality Questions

These are hypotheses to investigate during profiling, not confirmed defects.

1. Is `Unique Key` populated and unique across all records?
2. Are `Created Date`, `Closed Date`, `Due Date`, and `Resolution Action Updated Date` parseable?
3. Does `Closed Date` ever occur before `Created Date`?
4. Are open requests missing `Closed Date`, and are there exceptions?
5. Are `Agency` and `Agency Name` consistent with each other?
6. Do `Problem Detail` values belong to the corresponding `Problem`?
7. Are `Additional Details` missing for categories where they are optional?
8. Are status values consistent with the documented examples, while allowing for new values?
9. Are ZIP codes stored consistently and do they represent valid NYC incident locations?
10. Are `Borough`, `Community Board`, `Council District`, and `Police Precinct` populated and plausible?
11. Do latitude/longitude values fall within plausible NYC geographic bounds?
12. Are X/Y coordinates consistent with the documented State Plane coordinate reference system?
13. Are `Location` and the separate latitude/longitude fields consistent?
14. Are specialized fields populated only for relevant request types, or are there legitimate exceptions?
15. Have field labels, definitions, or category values changed over time?

## 5. Important Interpretation Notes

- The lists of expected values are explicitly non-exhaustive. A new value is not automatically invalid.
- `Problem Detail` depends on `Problem`; validate the relationship, not just each column independently.
- `Closed Date` is a lifecycle timestamp and should not be assumed to exist for every request.
- `Due Date` represents an expected agency update under an SLA; it is not necessarily the actual closure deadline.
- `Resolution Action Updated Date` means the last update date described by the dictionary; it should not automatically be treated as the closure date.
- `City` may represent a neighborhood in Queens, not only a city or borough.
- `BBL` is a structured parcel identifier; do not treat it as an ordinary numeric measure.
- Latitude/longitude and State Plane X/Y are different coordinate representations and require the correct coordinate reference system for conversion or mapping.
- Blank values may be legitimate for optional or specialized fields. Investigate field meaning and request type before imputing or deleting them.
- Complaint counts measure reported service requests, not the objective prevalence or severity of a condition.

## 6. Documentation Status

- [x] Dataset overview documented.
- [x] Data provider and row-level meaning documented.
- [x] Update frequency documented.
- [x] Collection method documented.
- [x] Dataset limitations documented.
- [x] Public-facing column names recorded.
- [x] Column descriptions recorded from the supplied dictionary.
- [x] Expected/allowed values recorded where supplied.
- [ ] Technical API field names verified.
- [ ] Actual data types verified from the dataset schema.
- [ ] Actual observed values profiled.
- [ ] Data quality rules tested against records.

## 7. Source

NYC Open Data — 311 Service Requests from 2020 to Present.

Dataset page:
https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data

The column descriptions and expected values in this document were transcribed and organized from the data dictionary material supplied for this project. Re-check the live source because the dataset is updated and expected values may change.
