 

#case 1 

# instance_count=5,  hourly_rates=0.45 , budget_cap=1500 
# hours per month=720 ( assume 30 days X 24 hours = 720 hours of uptime total) 


def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    hours_per_month = 30 * 24

    total_monthly_cost = instance_count * hourly_rate * hours_per_month 


#check against the budget and return the message 

    if total_monthly_cost > budget_cap:
         exceeded_by = total_monthly_cost - budget_cap 
         return f"Rejected: Budget Exceeded by ${exceeded_by}!"

    else: 

        return f"Approved: Total Estimated Cost by ${exceeded_by}!"


print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
