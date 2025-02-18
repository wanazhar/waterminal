# utilities/validator.py
from pydantic import BaseModel, validator
from typing import Dict, Any

class FinancialStatementSchema(BaseModel):
    period: str
    revenue: float
    gross_profit: float
    net_income: float
    eps: float
    total_assets: float
    
    @validator('*', pre=True)
    def replace_none(cls, value):
        return value or 0.0

class DataValidator:
    SCHEMAS = {
        'income_statement': FinancialStatementSchema,
        'balance_sheet': FinancialStatementSchema,
        'cash_flow': FinancialStatementSchema
    }
    
    @classmethod
    def validate(cls, data_type: str, raw_data: Dict[str, Any]):
        schema = cls.SCHEMAS.get(data_type)
        if not schema:
            raise ValidationError(f"No schema for {data_type}")
            
        return schema(**raw_data).dict()