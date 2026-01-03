def allocate_seats(total_seats: int) -> dict:
    """Basic seat allocation. Replace later with EMSR-b heuristic."""
    economy = int(total_seats * 0.66)
    business = int(total_seats * 0.28)
    first = total_seats - economy - business
    return {"economy": economy, "business": business, "first": first}
