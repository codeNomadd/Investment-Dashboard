from app.services.stock_service import StockService

def update_stock_data(symbol):
    """Update data for a single stock"""
    if not symbol:
        return None
    service = StockService()
    return service.update_stock_data(symbol)

def update_all_stocks(symbols):
    """Update data for provided stock symbols"""
    if not symbols:
        return {}
        
    service = StockService()
    results = {}
    
    for symbol in symbols:
        if symbol.strip():
            stocks = service.update_stock_data(symbol.strip())
            if stocks:
                results[symbol] = len(stocks)
    
    return results 