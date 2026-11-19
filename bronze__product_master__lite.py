from pathlib import Path
import duckdb

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()
    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE bronze_bronze_product_master_lite AS
    SELECT
       sku,
       product_name,
       category,
       brand,
       unit_cost
    FROM raw_inventory_movements_lite;
    """)

    con.close()
    print("Created bronze_product_master_lite")

if __name__ == "__main__":
    main()