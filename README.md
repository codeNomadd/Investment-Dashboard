# Investment Dashboard Project

![Investment Dashboard](tableau_dashboard/Tableau%20Dashboard.png "Investment Dashboard")

## Overview

Welcome to the Investment Dashboard Project, an interactive platform designed to provide a comprehensive view of stock market investments. This project integrates Python-based data extraction and storage with Tableau's powerful visualization capabilities. It is perfect for investors and financial analysts seeking actionable insights into their portfolios.

### Why This Project?

In today's financial world, data is the foundation of informed decisions. The Investment Dashboard Project simplifies data collection, management, and visualization, offering users a streamlined tool to analyze their investments and make data-driven choices.

### Key Features

- **Automated Data Extraction**: Fetch daily stock data (high prices and volumes) for multiple symbols using the Alpha Vantage API.
- **Database Management**: Store and update stock data in a MySQL database with table creation and automatic data updates.
- **Portfolio Analytics**: Use Tableau to track and analyze portfolio performance and visualize key metrics.
- **Customizability**: Add your own stock symbols to the project for personalized insights.

## Getting Started

### Prerequisites

You will need:
- **Python 3.x**: Download Python [here](https://www.python.org/downloads/).
- **Tableau**: Either Tableau Desktop or Tableau Public ([Download Tableau](https://www.tableau.com/products/desktop/download)).
- **MySQL Server**: Install and configure MySQL on your system.
- **Alpha Vantage API Key**: Get your API key [here](https://www.alphavantage.co/support/#api-key).

### Installation

```bash
# 1. Clone the Repository
git clone https://github.com/irmuun8881/Investment-Dashboard.git
cd Investment-Dashboard
```

# 2. Install Dependencies
```bash
pip install -r requirements.txt
```

# 3. Configure Environment Variables

Create a .env file in the project directory with the following content:
```bash
# API_KEY=your_alpha_vantage_api_key
# DB_HOST=localhost
# DB_USER=your_mysql_username
# DB_PASSWORD=your_mysql_password
# DB_NAME=investment
```

# 4. Run the Data Extraction Script
```bash
python fetch_portfolio_data.py
```

# 5. Launch Tableau Dashboard
Open the Tableau workbook in the `tableau_dashboard` folder.

# 6. Usage
### Once you have the dashboard open in Tableau, you can:

- Use filters to adjust the time frame and view data for specific periods.
- Hover over charts to get detailed insights.
- Analyze individual stock performance and portfolio growth trends.
## Contributing
We welcome contributions to improve this project! Feel free to: irmuun8881@gmail.com

# 7. Fork the repository.
- Create a new branch
```bash
git checkout -b feature/YourFeature
```
- Commit your changes 
```bash
git commit -m "Add YourFeature"
```
- Push to the branch 
```bash
git push origin feature/YourFeature
```
- Open a pull request.
# 8. License
This project is licensed under the MIT License. See the LICENSE file for details.

# 9. Support
If this project helps you, consider starring the repository on GitHub!# Investment-Dashboard
