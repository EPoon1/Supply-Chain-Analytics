from pathlib import Path
import duckdb

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()
    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE bronze_sales_transaction_lite AS
    SELECT
        transaction_id,
        transaction_ts,
        channel,
        location_id,
        sku,
        qty,
        unit_price
    FROM raw_inventory_movements_lite;
    """)

    con.close()
    print("Created bronze_sales_transaction_lite")

if __name__ == "__main__":
    main()