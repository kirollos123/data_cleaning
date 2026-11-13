# NYC 311 Schema Verification

## Objective

Verify that the official NYC 311 API schema matches
the published Excel Data Dictionary.

## Data Sources

- Dataset: 311 Service Requests from 2020 to Present
- Dataset ID: erm2-nwe9
- API Endpoint: https://data.cityofnewyork.us/resource/erm2-nwe9.json
- Metadata Endpoint: https://data.cityofnewyork.us/api/views/erm2-nwe9.json
- Data Dictionary: 311_ServiceRequest_2020-present_DataDictionary_Updated_2025.xlsx

## Verification Results

| Check | Result |
|---|---:|
| Documented business columns | 44 |
| API business columns | 44 |
| Additional computed fields | 4 |
| Documented fields missing from API | 0 |
| API fields missing from documentation | 0 |
| Final schema match | PASS |

## Schema Mapping

Some display names differ from their API field names.

| Display Name | API Field Name |
|---|---|
| Problem | complaint_type |
| Problem Detail | descriptor |
| Additional Details | descriptor_2 |
| X Coordinate (State Plane) | x_coordinate_state_plane |
| Y Coordinate (State Plane) | y_coordinate_state_plane |

## Additional Metadata Fields

The API metadata contains four computed geographic fields
that are not included in the 44 documented business columns.

## Important Notes

- The API metadata describes 48 fields.
- The Data Dictionary documents 44 business columns.
- The API returns 1000 records by default when no limit is specified.
- Fields absent from individual JSON records are not necessarily
  absent from the dataset.
- Schema verification does not prove data quality.

## Conclusion

The 44 documented business columns match the 44 API business
fields after applying explicit schema mapping.

Status: PASSED
