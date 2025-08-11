# Database Design Using ArcGIS Pro and Python

This project demonstrates how to design and automate a spatial database using **ArcGIS Pro**, **ArcPy**, and custom **Python toolboxes**. It includes:

- Creating a File Geodatabase
- Defining Feature Classes and Schemas
- Writing Scripts to Automate Tasks
- Creating and Using Python Script Tools in ArcGIS Pro Toolbox

## 🧰 Tools & Technologies
- ArcGIS Pro (2.8+)
- Python 3.x with ArcPy
- ArcGIS Python Toolbox (.pyt or .tbx)

## 📁 Folder Structure

- `data/` – Sample or dummy datasets
- `toolbox/` – Custom toolbox and scripts
- `scripts/` – Standalone automation scripts
- `docs/` – Screenshots and workflow explanation

## 🚀 Getting Started

1. Clone the repo.
2. Open ArcGIS Pro.
3. Load `toolbox/CustomToolbox.tbx`.
4. Run tools with provided scripts.

# Sample Inputs for "Change Domain Names in a Folder" Toolbox

This folder contains example input files for use with the ArcGIS Python toolbox that manages geodatabase domains.

## Included Files

- `domain_to_create.csv`: Defines new domains to be created.
- `assign_domains.csv`: Maps feature class fields to domain names.
- `delete_domains.csv`: Lists domain names to delete.
- `coded_values.json`: Contains coded values to populate domains.

## 🧠 Notes

- Ensure ArcPy is accessible in your Python environment.
- Scripts are designed for educational/demo purposes.

## 📄 License

MIT (or your preferred license)
