pm = PortfolioManager()

# Add positions
pm.add_position("AAPL", 100, 150.25)
pm.add_position("TSLA", 50, 700.00)

# Update prices (in async context)
await pm.update_prices()

# View portfolio
console.print(pm.get_portfolio_view())

# Generate performance report
console.print(pm.performance_report())