  drop FOREIGN TABLE if exists stock_data;

  create foreign table stock_data (
  timestamp date,
  symbol text,
  open float,
  high float,
  low float,
  close float,
  volume float
)
server s3_server
  options (
    uri 's3://dp-transformed-data/2025/04/21/21/dp-stock-market-data-9-2025-04-21-21-35-01-93e1087f-7e8f-4959-8e33-998cb37c3e9b.parquet',
    format 'parquet'
  );
