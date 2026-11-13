import requests
from openpyxl import load_workbook

# NYC 311 dataset API endpoint
API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
METADATA_URL = "https://data.cityofnewyork.us/api/views/erm2-nwe9.json"
# Send a GET request to NYC Open Data API
response = requests.get(API_URL, timeout=30)

# Check the HTTP response status
print("HTTP Status Code:", response.status_code)
# Inspect response headers
print("Content-Type:", response.headers.get("Content-Type"))
print("Content-Length:", response.headers.get("Content-Length"))
# Convert JSON response into Python objects
data = response.json()

# Inspect the response structure
print("Response Type:", type(data))
print("Number of Records:", len(data))
print("First Record:", data[0])
# Request dataset metadata
metadata_response = requests.get(METADATA_URL, timeout=30)

print("Metadata Status Code:", metadata_response.status_code)
# Convert metadata JSON into a Python dictionary
metadata = metadata_response.json()

# Inspect metadata structure
print("Metadata Type:", type(metadata))
print("Metadata Keys:", metadata.keys())

# Extract column definitions
columns = metadata["columns"]

print("Number of Columns:", len(columns))
print("First Column Definition:", columns[0])
# Display all dataset columns
print("\n========== DATASET SCHEMA ==========")

for column in columns:
    print(
        f"Position: {column.get('position')} | "
        f"Name: {column.get('name')} | "
        f"Field: {column.get('fieldName')} | "
        f"Type: {column.get('dataTypeName')}"
    )
# Extract expected field names from metadata
expected_fields = {
    column["fieldName"]
    for column in columns
}

# Extract fields returned across all sample records
observed_fields = {
    field
    for record in data
    for field in record.keys()
}

# Compare expected and observed fields
print("\n========== SCHEMA COMPARISON ==========")

print("Expected Fields:", len(expected_fields))
print("Observed Fields:", len(observed_fields))

print("\nFields not observed in sample:")
print(sorted(expected_fields - observed_fields))

print("\nFields not defined in metadata:")
print(sorted(observed_fields - expected_fields))
# Inspect the official Excel Data Dictionary
EXCEL_PATH = (
    "documentation/"
    "311_ServiceRequest_2020-present_DataDictionary_Updated_2025.xlsx"
)

workbook = load_workbook(
    EXCEL_PATH,
    read_only=True,
    data_only=True
)

print("\n========== DATA DICTIONARY STRUCTURE ==========")

print("Sheet Names:", workbook.sheetnames)

for sheet in workbook.worksheets:
    print(
        f"Sheet: {sheet.title} | "
        f"Rows: {sheet.max_row} | "
        f"Columns: {sheet.max_column}"
    )

workbook.close()
# Reopen the workbook to inspect sheet contents
workbook = load_workbook(
    EXCEL_PATH,
    read_only=True,
    data_only=True
)

sheets_to_inspect = [
    "Dataset Information",
    "Column Information",
    "Dataset Revision History"
]
print("\n========== DATA DICTIONARY CONTENTS ==========")

for sheet_name in sheets_to_inspect:
    sheet = workbook[sheet_name]

    print(f"\n--- Sheet: {sheet_name} ---")

    for row in sheet.iter_rows(
        min_row=1,
        max_row=12,
        values_only=True
    ):
        print(row)

workbook.close()
# Reopen workbook to extract documented column names
workbook = load_workbook(
    EXCEL_PATH,
    read_only=True,
    data_only=True
)

sheet = workbook["Column Information"]

print("\n========== DOCUMENTED COLUMNS ==========")

documented_columns = []

for row in sheet.iter_rows(
    min_row=4,
    max_row=60,
    min_col=1,
    max_col=1,
    values_only=True
):
    column_name = row[0]

    if column_name is not None:
        documented_columns.append(column_name)

for position, column_name in enumerate(documented_columns, start=1):
    print(f"{position}. {column_name}")

print("\nTotal Documented Columns:", len(documented_columns))

workbook.close()
# Normalize documented column names
documented_names = {
    name.strip().lower()
    for name in documented_columns
}

# Normalize API column names
api_names = {
    column["name"].strip().lower()
    for column in columns
    if not column["fieldName"].startswith(":@computed_region")
}

print("\n========== DOCUMENTED vs API ==========")

print("Documented Columns:", len(documented_names))
print("API Business Columns:", len(api_names))

print("\nColumns in Data Dictionary but missing from API:")
print(sorted(documented_names - api_names))

print("\nColumns in API but missing from Data Dictionary:")
print(sorted(api_names - documented_names))
# Map display names to API field names

display_to_api = {
    "problem": "complaint_type",
    "problem detail": "descriptor",
    "additional details": "descriptor_2",
    "x coordinate (state plane)": "x_coordinate_state_plane",
    "y coordinate (state plane)": "y_coordinate_state_plane",
}
# Normalize API field names
api_field_names = {
    column["fieldName"]
    for column in columns
    if not column["fieldName"].startswith(":@computed_region")
}

# Convert documented names to API field names
mapped_documented_fields = {
    display_to_api.get(name, name.lower().replace(" ", "_"))
    for name in documented_names
}

print("\n========== FINAL FIELD MATCH ==========")

print("Documented Fields:", len(mapped_documented_fields))
print("API Business Fields:", len(api_field_names))

print("\nDocumented fields missing from API:")
print(sorted(mapped_documented_fields - api_field_names))

print("\nAPI fields missing from documentation:")
print(sorted(api_field_names - mapped_documented_fields))

print("\nAll fields matched:", mapped_documented_fields == api_field_names)
