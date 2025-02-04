Conventions for the Workbook
--------------------------------

Because the "Concessionary Loans Assessment Template" workbook is complex (with multiple sections, sub‐sections, and embedded formulas) and will eventually be read programmatically, it will be helpful to agree on a set of design conventions. We want to ensure that the data is structured, consistent, and accompanied by clear metadata so that software can reliably parse and interpret it.

At present, for Non-fuel OPEX, the workbook is laid out as follows:

|  | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| **1** | **Line Item** | 2021 | 2022 | 2023 | 2024 |
| **2** | Operations | 100 | 110 | 120 | 130 |
| **3** | Maintenance | 200 | 210 | 220 | 230 |

In order to be ingested into our data warehouse, the above table will need to be “unpivoted” (or “melted”) into a tidy format like this:

| Line Item | Year | Cost |
| --- | --- | --- |
| Operations | 2021 | 100 |
| Operations | 2022 | 110 |
| Operations | 2023 | 120 |
| Operations | 2024 | 130 |
| Maintenance | 2021 | 200 |
| Maintenance | 2022 | 210 |
| Maintenance | 2023 | 220 |
| Maintenance | 2024 | 230 |

At present the user can choose to enter data in either real or nominal terms. The table we would like to ingest should be in real terms and pegged to a selected base year, and this basis year should be included in the table. We can do the unpivoting transformation outside the spreadseet, but it would be convenient if the spreadsheet can handle economic calculations and assemble the data to be ingested into a single place.

To facilitate this, can we please organize the workbook as follows:

* First convert all dollar values into real terms (if they are not already).
* Similarly convert all fuel consumption values into standard units (e.g., MWh).
* Convert each (real terms) “section” (and its sub‑sections) into an Excel Table. This will be the data that is ingested into our data warehouse.

Tables have several advantages:
*   **Named Ranges:** Each table gets a unique name.
*   **Automatic Expansion:** When more rows are added, the table automatically adjusts.
*   **Consistent Headers:** Tables require a header row, which ensures consistent labeling.

In terms of table layout, can we please adopt the conventions described in the following sections.


1\. One **Excel Table** per Section/Sub‐Section that should be ingestible into our data warehouse
-----------------------------------------------

1.  **Named Tables:**
    
    *   Convert the data range into an **Excel Table** (via _Insert > Table_ in Excel), and give it a descriptive name (e.g., `CAPEX_PP`, `OPEX_NonFuel_BC`, etc.).
    *   Avoid using spaces or special characters in table names.
2.  **Separate Tables for “Proposed Project (PP)” and “Base Case (BC):**
    
    *   For instance, “CAPEX\_PP” and “CAPEX\_BC” are two distinct tables on the same sheet, rather than one long table with intermixed rows.
    *   Similarly for OPEX, Fuel Costs, Finance Costs, Revenue, etc.
3.  **Consistent Placement of Tables:**
    
    *   Place each table so that its header row begins on a **clear row** (i.e., there are no labels or notes in the cells directly above that header row).
    *   Keep at least **one blank row** after each table to delineate the end of the table area.

4.  **All Relevant Variables Presented within Table:**

    *   For instance, if the basis year is a variable, include it as a column in the table.

* * *

2\. Minimal table structure: Single Header Row with Fixed Columns
----------------------------------------

1.  **Dedicated Header Row:**
    
    *   The **first row** of each table must be the header row, containing descriptive column labels.
    *   No merged cells or multiple header rows within the same table.
2.  **Dollar Value Columns (for CAPEX and OPEX):**
    
    1.  **Capex Item**
    2.  **Real Basis Year** (e.g., 2025)
    3.  **Applicant Comment** (for free‐form text)
    4.  **Year Columns** (e.g., 2025, 2026, …, 2050)
    
    *   If a “Total” column is needed, keep it outside of the table area.
3.  **Identical Columns for Proposed Project vs. Base Case:**
    
    *   Ensure the column structure (headings, order) is identical between “PP” and “BC” tables for the same section. For example, `CAPEX_PP` and `CAPEX_BC` should have the same columns in the same order.
4.  **No Sub‐Headers Inside the Table:**
    
    *   If you want to label subtotals or group certain line items, do so with an additional “Line item” or “Category” column, not by inserting extra rows of merged headers.

* * *

3\. One Row per Line Item (or Fuel Type, etc.)
----------------------------------------------

1.  **Atomic Rows:**
    
    *   Each row corresponds to a discrete item, e.g., a single CAPEX line item, OPEX cost item, or single fuel type.
2.  **Totals and Differences:**

    *   Exclude the “Total” row from the table (e.g., “Total capex in current dollars,” “Increase/(decrease) in capex”).
3.  **Data Types:**

    *   Keep numeric data in numeric cells (i.e., no text strings like “1,000,000.00 USD”).
    *   Use Excel’s built‐in number formatting for currency or thousands separators.
4.  **No “Expand if more items” Rows within the Table:**

    *   If you want to prompt users to add more rows, place that note **above or below** the table boundary.
    *   The Excel Table itself should contain only the header row and the data rows.

* * *

4\. Column Conventions for Years
--------------------------------

1.  **Consecutive Year Columns:**
    
    *   For clarity, list the year columns **from left to right**, in ascending order (e.g., 2025, 2026, …, 2050).
    *   Do not insert unrelated columns between year columns (or anywhere in the table).
2.  **Consistent Year Ranges:**
    
    *   Use the **same set of year columns** across all PP/BC tables for a given section, even if some years are zeros.
3.  **No Merging of Cells or Columns:**
    
    *   Do not merge the year cells or place extra labels in the year row.
    *   Keep each (year, row) cell as a single numeric figure.

* * *

5\. Data Validation and Comments
--------------------------------

1.  **Data Validation:**
    
    *   Add validation rules where-ever possible to ensure data integrity.
    *   Ensure year columns are numeric cells (no text).
    *   If possible, highlight negative numbers if they are not allowed.

* * *

*   **Naming Conventions:**  
    Define a naming scheme that clearly reflects both the section and the scenario. For example:
    
    *   **CAPEX Section:**
        *   Proposed Project table: `CAPEX_PP`
        *   Base Case table: `CAPEX_BC`
    *   **OPEX (and its sub‐sections):**
        *   For non‑fuel OPEX: `OPEX_NonFuel_PP` and `OPEX_NonFuel_BC`
        *   For fuel consumption: `OPEX_Fuel_PP` and `OPEX_Fuel_BC`
        *   Etc.
    
    This naming convention would allow our extraction tool to identify the section and scenario immediately.
    
*   **Avoid Merged Cells & Inconsistent Formatting:**
    The data region within each table must not include merged cells or multi‐line headers. Every cell in the table should contain a single, atomic piece of data.

*   **Data Validation:**
    Can we please implement data validation rules (for example, ensuring that cost figures are numeric and positive) and, if possible, to include a brief data dictionary (perhaps on a “Metadata” or “Instructions” sheet) that documents:
    
    *   Each section’s purpose.
    *   Expected columns and their data types.
    *   Any assumptions or notes about formula logic.