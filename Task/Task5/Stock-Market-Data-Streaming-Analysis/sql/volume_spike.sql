--this test code works well
--amd program behaves correctly 
--you may proceed to remove the LIMIT

WITH volume_spike_table AS (
    SELECT
        Symbol,
        Volume,
        ROW_NUMBER() OVER (
            PARTITION BY Symbol
            ORDER BY "$path"
        ) AS "row_number"
    
    FROM "dp-stock-db"."dp-stock-glue-table"
),

prev_volumes AS (
    SELECT
        curr.symbol,
        curr.row_number,
        curr.volume AS current_volume,
        AVG(prev.volume) AS avg_prev_volume
        
    FROM volume_spike_table curr
    JOIN volume_spike_table prev
      ON curr.symbol = prev.symbol
     AND prev.row_number BETWEEN curr.row_number - 3 AND curr.row_number - 1
    GROUP BY curr.symbol, curr.row_number, curr.volume
)

SELECT *,
       CASE 
         WHEN current_volume > 2 * avg_prev_volume THEN 'SPIKE'
         ELSE 'normal'
       END AS volume_spike_flag
FROM prev_volumes
ORDER BY symbol, row_number

LIMIT 10;