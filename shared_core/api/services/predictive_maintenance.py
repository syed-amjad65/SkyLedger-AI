from datetime import date, timedelta
from typing import List

from app.schemas.predictive_maintenance import DailyRiskPoint


def generate_dummy_risk_curve(start_date: date, end_date: date) -> List[DailyRiskPoint]:
    """
    Generate a simple increasing risk curve between two dates.
    This is a placeholder for a real predictive maintenance model.
    """
    days = (end_date - start_date).days + 1
    points: List[DailyRiskPoint] = []

    if days <= 0:
        return points

    for i in range(days):
        current_date = start_date + timedelta(days=i)
        # simple dummy logic: risk increases over time from 0.1 to 0.9
        risk_score = 0.1 + (0.8 * (i / max(days - 1, 1)))
        if risk_score < 0.3:
            risk_level = "low"
        elif risk_score < 0.7:
            risk_level = "medium"
        else:
            risk_level = "high"

        points.append(
            DailyRiskPoint(
                date=current_date,
                risk_score=round(risk_score, 2),
                risk_level=risk_level,
            )
        )

    return points