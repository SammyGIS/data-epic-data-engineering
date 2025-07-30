--test code works and program behaves as expected 
--you may proceed to remove the LIMIT clause

WITH price_change_table AS (
    SELECT
        Symbol,
        Close,
        ROW_NUMBER()
            OVER(
                PARTITION BY Symbol
                ORDER BY "$path"
        ) AS "row_number"
    
    FROM "dp-stock-db"."dp-stock-glue-table" 
)

SELECT curr.Symbol, curr.Close,
       (curr.Close - prev.Close) AS price_change,
       ((curr.Close - prev.Close) / prev.Close)*100 AS pct_price_change
       
FROM price_change_table curr
JOIN price_change_table prev
    ON curr.Symbol = prev.Symbol
    AND curr.row_number = prev.row_number + 1

LIMIT 10;