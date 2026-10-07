# Crypto dashboard

A single self-contained HTML file. Open `index.html` by double-clicking it, or
host it anywhere static — there is no build step, no server requirement and no
dependencies beyond two CDN scripts (d3 and Observable Plot).

Three tabs:

- **Market** — top assets by market cap with day / month / 12-month / 5-year
  changes, all-time high and distance from it, plus a separate stablecoin
  section showing peg deviation.
- **On-chain** — stablecoin issuance, TVL, DEX volumes, active addresses,
  transaction counts and chain fees.
- **Rates** — perpetual funding rates for the most liquid coins, and USDT/USDC
  money-market yields.

Data is fetched live in the browser from CoinGecko, Binance, DefiLlama and
Coin Metrics — all keyless. An optional Dune panel asks for an API key at
runtime and keeps it in `localStorage`, so no credential is ever stored in
this file.

## Running it locally

`python3 serve.py` serves the dashboard on your network (default port 8777) so
you can reach it from a phone. It deliberately serves only a dedicated
directory, and sends `Cache-Control: no-store` so edits show up immediately.
