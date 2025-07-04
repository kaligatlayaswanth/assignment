import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DemoDataSerializer

class DemoDataView(APIView):
    def get(self, request):
        try:
            data = {}

            # Financial Data Processing
            # Modify the following block to change how financial data is processed (e.g., change year, metrics, or aggregations)
            df_financial = pd.read_csv('wayne_financial_data.csv')
            revenue_2024 = df_financial[df_financial['Year'] == 2024][['Division', 'Revenue_M']].groupby('Division').sum().reset_index()
            bar_data_financial = {
                'labels': revenue_2024['Division'].tolist(),
                'data': revenue_2024['Revenue_M'].tolist(),
                'description': 'Bar chart showing total revenue by division for 2024 (in millions USD)'
            }
            profit_2024 = df_financial[df_financial['Year'] == 2024][['Division', 'Net_Profit_M']].groupby('Division').sum().reset_index()
            pie_data_financial = {
                'labels': profit_2024['Division'].tolist(),
                'data': profit_2024['Net_Profit_M'].tolist(),
                'description': 'Pie chart showing net profit share by division for 2024 (in millions USD)'
            }
            cards_financial = [
                {'metric': 'Total Revenue (2024)', 'value': float(df_financial[df_financial['Year'] == 2024]['Revenue_M'].sum())},
                {'metric': 'Total Net Profit (2024)', 'value': float(df_financial[df_financial['Year'] == 2024]['Net_Profit_M'].sum())},
                {'metric': 'Avg Customer Satisfaction', 'value': float(df_financial['Customer_Satisfaction_Score'].mean())}
            ]
            data['financial'] = {'bar': bar_data_financial, 'pie': pie_data_financial, 'cards': cards_financial}

            # HR Data Processing
            # Modify the following block to change how HR data is processed (e.g., change year, department, or metrics)
            df_hr = pd.read_csv('wayne_hr_analytics.csv')
            satisfaction_2024 = df_hr[df_hr['Date'].str.startswith('2024')][['Department', 'Employee_Satisfaction_Score']].groupby('Department').mean().reset_index()
            bar_data_hr = {
                'labels': satisfaction_2024['Department'].tolist(),
                'data': satisfaction_2024['Employee_Satisfaction_Score'].round(2).tolist(),
                'description': 'Bar chart showing average employee satisfaction score by department for 2024'
            }
            training_2024 = df_hr[df_hr['Date'].str.startswith('2024')][['Employee_Level', 'Training_Hours_Annual']].groupby('Employee_Level').sum().reset_index()
            pie_data_hr = {
                'labels': training_2024['Employee_Level'].tolist(),
                'data': training_2024['Training_Hours_Annual'].tolist(),
                'description': 'Pie chart showing total training hours by employee level for 2024'
            }
            cards_hr = [
                {'metric': 'Avg Satisfaction (2024)', 'value': float(df_hr[df_hr['Date'].str.startswith('2024')]['Employee_Satisfaction_Score'].mean())},
                {'metric': 'Avg Retention Rate', 'value': float(df_hr['Retention_Rate_Pct'].mean())},
                {'metric': 'Total Training Hours', 'value': float(df_hr['Training_Hours_Annual'].sum())}
            ]
            data['hr'] = {'bar': bar_data_hr, 'pie': pie_data_hr, 'cards': cards_hr}

            # R&D Data Processing
            # Modify the following block to change how R&D data is processed (e.g., change division or metrics)
            df_rd = pd.read_csv('wayne_rd_portfolio.csv')
            budget = df_rd[['Division', 'Budget_Allocated_M']].groupby('Division').sum().reset_index()
            bar_data_rd = {
                'labels': budget['Division'].tolist(),
                'data': budget['Budget_Allocated_M'].tolist(),
                'description': 'Bar chart showing total R&D budget allocated by division (in millions USD)'
            }
            patents = df_rd[['Division', 'Patent_Applications']].groupby('Division').sum().reset_index()
            pie_data_rd = {
                'labels': patents['Division'].tolist(),
                'data': patents['Patent_Applications'].tolist(),
                'description': 'Pie chart showing total patent applications by division'
            }
            cards_rd = [
                {'metric': 'Total Budget (M)', 'value': float(df_rd['Budget_Allocated_M'].sum())},
                {'metric': 'Avg Timeline Adherence', 'value': float(df_rd['Timeline_Adherence_Pct'].mean())},
                {'metric': 'Total Patents', 'value': float(df_rd['Patent_Applications'].sum())}
            ]
            data['rd'] = {'bar': bar_data_rd, 'pie': pie_data_rd, 'cards': cards_rd}

            # Security Data Processing
            # Modify the following block to change how Security data is processed (e.g., change year, district, or metrics)
            df_security = pd.read_csv('wayne_security_data.csv')
            safety_2024 = df_security[df_security['Date'].str.startswith('2024')][['District', 'Public_Safety_Score']].groupby('District').mean().reset_index()
            bar_data_security = {
                'labels': safety_2024['District'].tolist(),
                'data': safety_2024['Public_Safety_Score'].round(2).tolist(),
                'description': 'Bar chart showing average public safety score by district for 2024'
            }
            investments_2024 = df_security[df_security['Date'].str.startswith('2024')][['District', 'Infrastructure_Investments_M']].groupby('District').sum().reset_index()
            pie_data_security = {
                'labels': investments_2024['District'].tolist(),
                'data': investments_2024['Infrastructure_Investments_M'].tolist(),
                'description': 'Pie chart showing infrastructure investments by district for 2024 (in millions USD)'
            }
            cards_security = [
                {'metric': 'Avg Safety Score (2024)', 'value': float(df_security[df_security['Date'].str.startswith('2024')]['Public_Safety_Score'].mean())},
                {'metric': 'Total Incidents', 'value': float(df_security['Security_Incidents'].sum())},
                {'metric': 'Total Investments (M)', 'value': float(df_security['Infrastructure_Investments_M'].sum())}
            ]
            data['security'] = {'bar': bar_data_security, 'pie': pie_data_security, 'cards': cards_security}

            # Supply Chain Data Processing
            # Modify the following block to change how Supply Chain data is processed (e.g., change year, facility, or metrics)
            df_supply = pd.read_csv('wayne_supply_chain.csv')
            carbon_2024 = df_supply[df_supply['Date'].str.startswith('2024')][['Facility_Location', 'Carbon_Footprint_MT']].groupby('Facility_Location').mean().reset_index()
            bar_data_supply = {
                'labels': carbon_2024['Facility_Location'].tolist(),
                'data': carbon_2024['Carbon_Footprint_MT'].round(2).tolist(),
                'description': 'Bar chart showing average carbon footprint by facility for 2024 (in metric tons)'
            }
            vendors_2024 = df_supply[df_supply['Date'].str.startswith('2024')][['Facility_Location', 'Vendor_Count']].groupby('Facility_Location').sum().reset_index()
            pie_data_supply = {
                'labels': vendors_2024['Facility_Location'].tolist(),
                'data': vendors_2024['Vendor_Count'].tolist(),
                'description': 'Pie chart showing total vendor count by facility for 2024'
            }
            cards_supply = [
                {'metric': 'Avg Carbon Footprint (MT)', 'value': float(df_supply[df_supply['Date'].str.startswith('2024')]['Carbon_Footprint_MT'].mean())},
                {'metric': 'Total Production Volume', 'value': float(df_supply['Monthly_Production_Volume'].sum())},
                {'metric': 'Total Vendors', 'value': float(df_supply['Vendor_Count'].sum())}
            ]
            data['supply'] = {'bar': bar_data_supply, 'pie': pie_data_supply, 'cards': cards_supply}

            serializer = DemoDataSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': f'Error reading data: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)