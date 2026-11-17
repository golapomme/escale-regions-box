# Escale Régions Box

*Every month, a region on your table.*

Academic business project: an e-commerce prototype for a monthly subscription box of authentic French regional food products, sourced through short supply chains.

**Live site:** open `index.html` in a browser (it needs no server), or enable GitHub Pages on this repository.

## What's inside

| Path | Content |
|---|---|
| `index.html` | The complete website in one self-contained file (images and map included) |
| `src/template.html` | Editable source: styles, data, logic and pages |
| `src/build.py` | Rebuilds `index.html` from the template and assets (`python3 src/build.py`) |
| `src/*.png, *.jpg` | Provisional brand visuals |
| `src/map-paths.json` | Simplified outlines of the 13 regions of metropolitan France |

## Features

- Box sizes S / M / L, or a custom budget (€20–€150)
- One-time purchase or 3, 6 and 12-month subscriptions with automatic price calculation
- Configurator: payment mode, dietary preferences, live summary
- Interactive map and regional calendar
- Special editions and gift cards
- Cart, simulated checkout and demo customer account
- **Presenter mode:** press `D` (or open `index.html#demo`) for a guided 7-step tour; `←` `→` or a clicker to move, `Esc` to exit

## Prototype status

This is a front-end prototype. Payments, orders, accounts and notifications are **simulated**; data is stored only in the visitor's browser. Prices, product selections, the calendar and commercial conditions are **provisional**. See the "About this prototype" page in the site for the full list, and for what a production launch would require.

## Editing

All business settings (prices, plans, discounts, delivery fees, regions, editions) are data at the top of the script in `src/template.html`. All colours, fonts and spacing are CSS variables at the top of its stylesheet. Edit, then run `python3 src/build.py`.

## Credits

Region outlines derived from [france-geojson](https://github.com/gregoiredavid/france-geojson) (data from IGN / INSEE, Licence Ouverte).
