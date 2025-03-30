from app import db
from datetime import datetime

class Stock(db.Model):
    __tablename__ = 'stocks'
    
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False)
    high_price = db.Column(db.Float, nullable=False)
    volume = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.UniqueConstraint('symbol', 'date', name='unique_stock_date'),
    )
    
    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'date': self.date.isoformat(),
            'high_price': self.high_price,
            'volume': self.volume,
            'created_at': self.created_at.isoformat()
        } 