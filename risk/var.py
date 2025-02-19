# risk/var.py
import numpy as np
from scipy.stats import norm

class ValueAtRisk:
    def __init__(self, confidence_level=0.95):
        self.confidence = confidence_level
        
    def historical_var(self, returns: pd.Series) -> float:
        """Calculate Value-at-Risk using historical simulation"""
        return np.percentile(returns, 100*(1-self.confidence))
    
    def parametric_var(self, returns: pd.Series) -> float:
        """Calculate VaR using variance-covariance method"""
        mu = returns.mean()
        sigma = returns.std()
        return mu - sigma * norm.ppf(self.confidence)