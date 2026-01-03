# app/schemas/__init__.py

# Forecast (ensure app/schemas/forecast.py exists)
from .forecast import ForecastRequest, ForecastResponse

# Predictive maintenance
from .predictive_maintenance import (
    MaintenanceForecastRequest,
    MaintenanceForecastResponse,
    DailyRiskPoint,
)
 # Inventory
from .inventory import InventoryRequest, InventoryResponse

# Existing modules (keep only if files exist)
from .activity_dashboard import *
from .asset_metadata import *
from .audit_logs import *
from .auth import *
from .cx_analytics import *
from .dashboard_metrics import *
from .ingestion import *
from .system_health import *
from .user import *
from .user_management import *
from .anomaly import AnomalyRequest, AnomalyResponse
