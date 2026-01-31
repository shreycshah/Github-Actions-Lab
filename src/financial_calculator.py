def simple_interest(principal, rate, time):
    """
    Calculate Simple Interest
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Inputs must be non-negative")
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, frequency=1):
    """
    Calculate Compound Interest
    frequency = number of times interest is compounded per year
    """
    if principal < 0 or rate < 0 or time < 0 or frequency <= 0:
        raise ValueError("Invalid input values")

    amount = principal * (1 + rate / (100 * frequency)) ** (frequency * time)
    return amount - principal


def calculate_emi(principal, annual_rate, tenure_months):
    """
    Calculate EMI (Equated Monthly Installment)
    """
    if principal <= 0 or annual_rate < 0 or tenure_months <= 0:
        raise ValueError("Invalid input values")

    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        return principal / tenure_months

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)
    return emi


def profit_or_loss_percentage(cost_price, selling_price):
    """
    Calculate profit or loss percentage
    Positive value = profit, Negative value = loss
    """
    if cost_price <= 0:
        raise ValueError("Cost price must be greater than zero")

    return ((selling_price - cost_price) / cost_price) * 100


def discounted_price(original_price, discount_percent):
    """
    Calculate final price after discount
    """
    if original_price < 0 or not (0 <= discount_percent <= 100):
        raise ValueError("Invalid input values")

    return original_price - (original_price * discount_percent / 100)