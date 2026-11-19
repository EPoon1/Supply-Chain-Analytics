from pathlib import Path
import duckdb

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    db_path = (script_dir / ".." / ".." / "supply_chain_analytics.duckdb").resolve()
    con = duckdb.connect(str(db_path))

    con.execute("""
    CREATE OR REPLACE TABLE bronze_inventory_movements_lite AS
    SELECT
        movement_id,
        movement_ts,
        movement_date,
        movement_type,
        sku,
        from_location_id,
        to_location_id,
        qty,
    FROM raw_inventory_movements_lite;
    """)

    con.close()
    print("Created bronze_inventory_movements_lite")

if __name__ == "__main__":
    main()