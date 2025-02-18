# config/menu_config.py
MENU_STRUCTURE = [
    {
        'id': 1,
        'label': 'Market Data Tools',
        'children': [
            {'id': 11, 'label': 'Historical Prices', 'module': 'data_sources.yfinance.historical'},
            {'id': 12, 'label': 'Real-time Quotes', 'module': 'data_sources.alpha_vantage.realtime'},
            {'id': 13, 'label': 'Crypto Data', 'module': 'data_sources.coingecko.crypto'}
        ]
    },
    {
        'id': 2,
        'label': 'Financial Analysis',
        'children': [
            {'id': 21, 'label': 'Valuation Ratios', 'module': 'financials.ratios.valuation'},
            {'id': 22, 'label': 'DCF Analysis', 'module': 'financials.advanced.dcf'}
        ]
    },
    {
        'id': 3,
        'label': 'AI Financial Assistant',
        'module': 'ai.assistant'
    }
]