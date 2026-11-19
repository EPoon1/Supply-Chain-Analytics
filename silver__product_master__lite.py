from pathlib import Path
import duckdb

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()
    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE silver__product_master__lite AS
    SELECT
        UPPER(TRIM(sku) AS sku,
        TRIM(product_name) AS product_name,
        TRIM(category) AS category,
        TRIM(brand) AS brand,
        unit cost
     FROM bronze__location_master__lite;
    """)

    con.close()
    print("Created silver__product_master__lite")

if __name__ == "__main_":
    main()