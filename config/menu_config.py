# config/menu_config.py
MENU_STRUCTURE = [
    {
        'id': 1,
        'label': 'Core Features',
        'children': [
            {'id': 11, 'label': 'Live Market Data', 'module': 'market.live_ticker'},
            {'id': 12, 'label': 'Historical Analysis', 'module': 'data_sources.source_router'},
            {'id': 13, 'label': 'Portfolio Manager', 'module': 'portfolio.manager'}
        ]
    },
    {
        'id': 2,
        'label': 'Advanced Tools',
        'children': [
            {'id': 21, 'label': 'Options Analysis', 'module': 'options.chain'},
            {'id': 22, 'label': 'Hedge Fund Replication', 'module': 'hedge_funds.replication'},
            {'id': 23, 'label': 'Backtesting Engine', 'module': 'backtesting.engine'}
        ]
    },
    {
        'id': 3,
        'label': 'AI Assistant',
        'module': 'ai.assistant'
    },
    {
        'id': 4,
        'label': 'Settings',
        'children': [
            {'id': 41, 'label': 'API Configuration', 'module': 'config.core'},
            {'id': 42, 'label': 'Data Sources', 'module': 'data_sources.base_source'}
        ]
    },
    {
        'id': 5,
        'label': 'Valuation Models',
        'children': [
            {'id': 51, 'label': 'DCF Analysis', 'module': 'financials.advanced.dcf.DCFAnalyzer'},
            {'id': 52, 'label': 'Comparables', 'module': 'financials.advanced.comps'}
        ]
    }
]