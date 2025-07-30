--remove LIMIT clause

WITH close_order AS (
    SELECT
        Symbol,
        close,
        ROW_NUMBER() OVER (
            PARTITION BY symbol
            ORDER BY "$path"
        ) AS row_number

    FROM "dp-stock-db"."dp-stock-glue-table"
),

moving_avg_table AS (
    SELECT
        curr.symbol,
        curr.row_number,
        curr.close AS current_close,
        AVG(prev.close) AS moving_avg_close

    FROM close_data curr
    JOIN close_data prev
      ON curr.symbol = prev.symbol
     AND prev.row_number BETWEEN curr.row_number - 4 AND curr.row_number  
    GROUP BY curr.symbol, curr.row_number, curr.close
)

SELECT *
FROM moving_avg_table
ORDER BY symbol, row_number;
LIMIT 10;