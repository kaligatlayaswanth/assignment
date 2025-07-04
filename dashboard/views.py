import pandas as pd
from django.shortcuts import render
from django.core.paginator import Paginator
import json

def base_view(request):
    return render(request, 'dashboard/home.html')

def financial_view(request):
    df = pd.read_csv('wayne_financial_data.csv')
    # Bar: Revenue by Division (2024)
    revenue_2024 = df[df['Year'] == 2024][['Division', 'Revenue_M']].groupby('Division').sum().reset_index()
    bar_labels = revenue_2024['Division'].tolist()
    bar_data = revenue_2024['Revenue_M'].tolist()
    # Line: Revenue Trend (2024)
    revenue_trend = df[df['Year'] == 2024][['Quarter', 'Revenue_M']].groupby('Quarter').sum().reset_index()
    line_labels = revenue_trend['Quarter'].tolist()
    line_data = revenue_trend['Revenue_M'].tolist()
    # Pie: Net Profit Share by Division (2024)
    profit_2024 = df[df['Year'] == 2024][['Division', 'Net_Profit_M']].groupby('Division').sum().reset_index()
    pie_labels = profit_2024['Division'].tolist()
    pie_data = profit_2024['Net_Profit_M'].tolist()

    # Pagination
    paginator = Paginator(df.to_dict('records'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/financial.html', context)

def hr_view(request):
    df = pd.read_csv('wayne_hr_analytics.csv')
    # Bar: Average Satisfaction by Division (2024)
    satisfaction_2024 = df[df['Date'].str.startswith('2024')][['Department', 'Employee_Satisfaction_Score']].groupby('Department').mean().reset_index()
    bar_labels = satisfaction_2024['Department'].tolist()
    bar_data = satisfaction_2024['Employee_Satisfaction_Score'].round(2).tolist()
    # Line: Retention Rate Trend (2024, Entry Level)
    retention_trend = df[(df['Date'].str.startswith('2024')) & (df['Employee_Level'] == 'Entry Level')][['Date', 'Retention_Rate_Pct']].groupby('Date').mean().reset_index()
    line_labels = retention_trend['Date'].tolist()
    line_data = retention_trend['Retention_Rate_Pct'].round(2).tolist()
    # Pie: Training Hours by Employee Level (2024)
    training_2024 = df[df['Date'].str.startswith('2024')][['Employee_Level', 'Training_Hours_Annual']].groupby('Employee_Level').sum().reset_index()
    pie_labels = training_2024['Employee_Level'].tolist()
    pie_data = training_2024['Training_Hours_Annual'].tolist()

    # Pagination
    paginator = Paginator(df.to_dict('records'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/hr.html', context)

def rd_view(request):
    df = pd.read_csv('wayne_rd_portfolio.csv')
    # Bar: Budget Allocated by Division
    budget = df[['Division', 'Budget_Allocated_M']].groupby('Division').sum().reset_index()
    bar_labels = budget['Division'].tolist()
    bar_data = budget['Budget_Allocated_M'].tolist()
    # Line: Timeline Adherence by Division
    timeline = df[['Division', 'Timeline_Adherence_Pct']].groupby('Division').mean().reset_index()
    line_labels = timeline['Division'].tolist()
    line_data = timeline['Timeline_Adherence_Pct'].round(2).tolist()
    # Pie: Patent Applications by Division
    patents = df[['Division', 'Patent_Applications']].groupby('Division').sum().reset_index()
    pie_labels = patents['Division'].tolist()
    pie_data = patents['Patent_Applications'].tolist()

    # Pagination
    paginator = Paginator(df.to_dict('records'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/rd.html', context)

def security_view(request):
    df = pd.read_csv('wayne_security_data.csv')
    # Bar: Average Public Safety Score by District (2024)
    safety_2024 = df[df['Date'].str.startswith('2024')][['District', 'Public_Safety_Score']].groupby('District').mean().reset_index()
    bar_labels = safety_2024['District'].tolist()
    bar_data = safety_2024['Public_Safety_Score'].round(2).tolist()
    # Line: Security Incidents Trend (2024, Downtown)
    incidents_trend = df[(df['Date'].str.startswith('2024')) & (df['District'] == 'Downtown')][['Date', 'Security_Incidents']].groupby('Date').sum().reset_index()
    line_labels = incidents_trend['Date'].tolist()
    line_data = incidents_trend['Security_Incidents'].tolist()
    # Pie: Infrastructure Investments by District (2024)
    investments_2024 = df[df['Date'].str.startswith('2024')][['District', 'Infrastructure_Investments_M']].groupby('District').sum().reset_index()
    pie_labels = investments_2024['District'].tolist()
    pie_data = investments_2024['Infrastructure_Investments_M'].tolist()

    # Pagination
    paginator = Paginator(df.to_dict('records'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/security.html', context)

def supply_view(request):
    df = pd.read_csv('wayne_supply_chain.csv')
    # Bar: Average Carbon Footprint by Facility (2024)
    carbon_2024 = df[df['Date'].str.startswith('2024')][['Facility_Location', 'Carbon_Footprint_MT']].groupby('Facility_Location').mean().reset_index()
    bar_labels = carbon_2024['Facility_Location'].tolist()
    bar_data = carbon_2024['Carbon_Footprint_MT'].round(2).tolist()
    # Line: Production Volume Trend (2024, Gotham_Main)
    production_trend = df[(df['Date'].str.startswith('2024')) & (df['Facility_Location'] == 'Gotham_Main')][['Date', 'Monthly_Production_Volume']].groupby('Date').sum().reset_index()
    line_labels = production_trend['Date'].tolist()
    line_data = production_trend['Monthly_Production_Volume'].tolist()
    # Pie: Vendor Count by Facility (2024)
    vendors_2024 = df[df['Date'].str.startswith('2024')][['Facility_Location', 'Vendor_Count']].groupby('Facility_Location').sum().reset_index()
    pie_labels = vendors_2024['Facility_Location'].tolist()
    pie_data = vendors_2024['Vendor_Count'].tolist()

    # Pagination
    paginator = Paginator(df.to_dict('records'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/supply.html', context)

