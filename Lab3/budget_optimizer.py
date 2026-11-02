 

#case 1 

# instance_count=5,  hourly_rates=0.45 , budget_cap=1500 
# hours per month=720 ( assume 30 days X 24 hours = 720 hours of uptime total) 


def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    hours_per_month = 30 * 24

    total_monthly_cost = instance_count * hourly_rate * hours_per_month 

    return total_monthly_cost

print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000))
