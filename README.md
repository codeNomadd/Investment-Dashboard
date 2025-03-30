# Stock Data Visualization Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

A streamlined platform for visualizing stock market data with ease. This project focuses on making stock data accessible and visually intuitive, perfect for quick market analysis and trend visualization.

## Dashboard Preview

![Investment Dashboard](dashboard/Tableau%20Dashboard.png)

## Dashboard Components

### 1. Portfolio Performance Timeline
- **Interactive time series visualization** tracking total portfolio value (2022-2024)
- Milestone annotations highlight key events and decisions
- Helps identify long-term trends and pattern recognition
- **Value Add**: Enables investors to correlate market events with portfolio performance

### 2. Asset Allocation Overview
- **Dynamic pie chart** displaying current portfolio composition
- Color-coded segments with percentage breakdowns
- Hover tooltips reveal detailed asset information
- **Value Add**: Quick assessment of portfolio diversification and rebalancing needs

### 3. Relative Performance Index
- **Normalized performance chart** comparing top 5 holdings
- Baseline-adjusted growth trajectories
- Custom date range selection
- **Value Add**: Easily identify outperforming and underperforming assets

### 4. Monthly Performance Analysis
- **Waterfall chart** showing month-over-month gains/losses
- Color-coded bars (green for gains, red for losses)
- Cumulative trend line overlay
- **Value Add**: Track investment momentum and identify seasonal patterns

### 5. Smart Asset Legend
- Interactive sidebar with asset details
- Real-time price updates and daily changes
- Brand logos for quick visual recognition
- **Value Add**: Consolidated view of key metrics for each holding

### 6. Advanced Filtering
- Flexible date range selection
- Asset-specific filtering capabilities
- Market cap and sector filters
- **Value Add**: Focused analysis of specific time periods or asset groups

## Dashboard Insights

The dashboard is designed to answer critical investment questions:
- How is my portfolio performing over time?
- Am I properly diversified across assets?
- Which holdings are driving returns?
- What are my monthly investment patterns?
- Where should I consider rebalancing?

## Visualization Enhancements

### Current Features
- Real-time stock price charts
- Price trend indicators
- Volume analysis
- Simple moving averages
- Basic technical indicators

### Recommended Improvements
1. **Technical Analysis**
   - Add RSI (Relative Strength Index) overlay
   - Include MACD (Moving Average Convergence Divergence)
   - Bollinger Bands for volatility tracking

2. **Risk Metrics**
   - Value at Risk (VaR) calculations
   - Beta coefficients for each asset
   - Correlation matrix heatmap

3. **UX Enhancements**
   - Dark/Light theme toggle
   - Customizable chart layouts
   - Export functionality for reports
   - Mobile-responsive design

4. **Advanced Analytics**
   - Monte Carlo simulations
   - Automated trend detection
   - Custom alert thresholds

## Alternative Implementation

This dashboard can be recreated using modern Python tools:

### Plotly Implementation
```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create interactive dashboard
fig = make_subplots(
    rows=3, cols=2,
    specs=[[{"type": "scatter"}, {"type": "pie"}],
           [{"type": "scatter"}, {"type": "bar"}],
           [{"colspan": 2}, None]],
    subplot_titles=("Portfolio Timeline", "Asset Allocation",
                   "Performance Index", "Monthly Analysis",
                   "Technical Indicators")
)
```

### Streamlit Alternative
```python
import streamlit as st
import plotly.express as px

# Create interactive components
st.title("Investment Dashboard")
date_range = st.date_input("Select Date Range")
selected_assets = st.multiselect("Select Assets")

# Dynamic visualizations
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(timeline_chart)
with col2:
    st.plotly_chart(allocation_chart)
```

## Dependencies

Core packages:
- Pandas & NumPy: Data processing
- Plotly/Streamlit: Interactive visualizations
- SQLAlchemy: Database management
- Alpha Vantage API: Real-time data

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