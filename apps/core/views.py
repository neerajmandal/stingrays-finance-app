from django.shortcuts import render
import json

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def free_tools(request):
    return render(request, 'core/free-tools.html')

def calculate_compound_interest(initial_investment, monthly_contribution, annual_return, years):
    """
    Calculate compound interest with monthly contributions
    Returns: dict with final value, total contributions, interest earned, growth multiple, and yearly data
    """
    pass

def investment_calculator(request):
    # Default values
    initial_investment = 10000
    monthly_contribution = 500
    annual_return = 10
    years = 30
    
    # Get values from request if provided
    if request.method == 'GET' and any(key in request.GET for key in ['initial', 'monthly', 'return', 'years']):
        try:
            initial_investment = float(request.GET.get('initial', initial_investment))
            monthly_contribution = float(request.GET.get('monthly', monthly_contribution))
            annual_return = float(request.GET.get('return', annual_return))
            years = int(request.GET.get('years', years))
        except (ValueError, TypeError):
            pass  # Use defaults if invalid values
    
    # Calculate investment growth
    results = calculate_compound_interest(
        initial_investment, 
        monthly_contribution, 
        annual_return, 
        years
    )
    
    context = {
        'initial_investment': initial_investment,
        'monthly_contribution': monthly_contribution,
        'annual_return': annual_return,
        'years': years,
        'final_value': results['final_value'],
        'total_contributions': results['total_contributions'],
        'interest_earned': results['interest_earned'],
        'growth_multiple': results['growth_multiple'],
        'yearly_data': results['yearly_data'],
        'yearly_data_json': json.dumps(results['yearly_data'])
    }
    
    return render(request, 'core/investment-calculator.html', context)