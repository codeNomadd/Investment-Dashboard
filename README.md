# Stock Data Visualization Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)](https://flask.palletsprojects.com/)

A streamlined platform for visualizing stock market data with ease. This project focuses on making stock data accessible and visually intuitive, perfect for quick market analysis and trend visualization.

## Dashboard Preview

![Investment Dashboard](dashboard/Tableau%20Dashboard.png)

## Overview

This platform simplifies stock market data visualization by:
- Providing clean, interactive charts for stock price trends
- Offering easy-to-understand market indicators
- Enabling quick comparison between different stocks
- Supporting real-time data updates from Alpha Vantage API

## Features

- **Simple Data Visualization**: Clean, interactive charts showing stock price movements
- **Real-time Updates**: Live data fetching from Alpha Vantage
- **Easy Comparison**: Compare multiple stocks side by side
- **Key Metrics Display**: View important stock metrics at a glance
- **User-friendly Interface**: Intuitive dashboard for easy navigation

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/codeNomadd/Investment-Dashboard.git
cd Investment-Dashboard
```

2. Set up your environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure your environment variables in `.env`:
```
ALPHA_VANTAGE_API_KEY=your_api_key_here
FLASK_APP=run.py
FLASK_ENV=development
```

4. Run the application:
```bash
python run.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Environment Setup

Required environment variables:
- `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key
- `FLASK_APP`: Application entry point
- `FLASK_ENV`: Application environment (development/production)

## Dependencies

Core packages:
- Flask: Web framework
- Pandas & NumPy: Data processing
- Celery & Redis: Background task processing
- SQLAlchemy: Database management

## Dashboard Features

The dashboard provides:
- Real-time stock price charts
- Price trend indicators
- Volume analysis
- Simple moving averages
- Basic technical indicators

## 📅 Upcoming Features

- [ ] Interactive candlestick charts with technical indicators
- [ ] Portfolio tracking and performance analytics
- [ ] Custom watchlist creation
- [ ] Export data to CSV/Excel
- [ ] Mobile-responsive design
- [ ] Dark/Light theme toggle
- [ ] Email alerts for price movements
- [ ] Social sharing capabilities

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License

This project is licensed under the MIT License - see LICENSE.txt for details.

## Acknowledgments

- Data provided by Alpha Vantage API
- Built with Flask and modern Python libraries
- Visualization powered by modern charting libraries 