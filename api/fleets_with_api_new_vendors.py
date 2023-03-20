import yaml
import requests


with open('tutorial_new_vendor.yaml', 'r') as f:
    data = yaml.safe_load(f)

company_list = ['pizza_planet','gusteau','buy_n_large']
fivetran_inputs = data['vessels']['Execute Fivetran Sync']['source']['inputs']
dbt_inputs = data['vessels']['Execute dbt Cloud Job']['source']['inputs']




for company in company_list:
    with open('tutorial_new_vendor.yaml', 'r') as f:
        data = yaml.safe_load(f)

    company_list = ['pizza_planet','gusteau','buy_n_large']
    fivetran_inputs = data['vessels']['Execute Fivetran Sync']['source']['inputs']
    dbt_inputs = data['vessels']['Execute dbt Cloud Job']['source']['inputs']


    data['name'] = f'{clients[company]["COMPANY_NAME"]} Fleet'
    fivetran_inputs['FIVETRAN_API_KEY'] = clients[company]['FIVETRAN_API_KEY']
    fivetran_inputs['FIVETRAN_API_SECRET'] = clients[company]['FIVETRAN_API_SECRET']
    fivetran_inputs['FIVETRAN_CONNECTOR_ID'] = clients[company]['FIVETRAN_CONNECTOR_ID']
    dbt_inputs['DBT_ACCOUNT_ID'] = clients[company]['DBT_ACCOUNT_ID']
    dbt_inputs['DBT_API_KEY'] = clients[company]['DBT_API_KEY']
    dbt_inputs['DBT_JOB_ID'] = clients[company]['DBT_JOB_ID']

    bi_tool = clients[company]['BI_TOOL']
    if bi_tool == 'tableau':
        data['vessels'].update(tableau)
        data['connections'].update(tableau_connection)
        tableau_inputs = data['vessels']['Trigger Tableau Datasource Refresh']['source']['inputs']
        tableau_inputs['TABLEAU_DATASOURCE_NAME'] = clients[company]['TABLEAU_DATASOURCE_NAME']
        tableau_inputs['TABLEAU_PASSWORD'] = clients[company]['TABLEAU_PASSWORD']
        tableau_inputs['TABLEAU_PROJECT_NAME'] = clients[company]['TABLEAU_PROJECT_NAME']
        tableau_inputs['TABLEAU_SERVER_URL'] = clients[company]['TABLEAU_SERVER_URL']
        tableau_inputs['TABLEAU_SITE_ID'] = clients[company]['TABLEAU_SITE_ID']
        tableau_inputs['TABLEAU_USERNAME'] = clients[company]['TABLEAU_USERNAME']
    if bi_tool == 'domo':
        data['vessels'].update(domo)
        data['connections'].update(domo_connection)
        domo_inputs = data['vessels']['Refresh Domo Dataset']['source']['inputs']
        domo_inputs['DOMO_ACCESS_TOKEN'] = clients[company]['DOMO_ACCESS_TOKEN']
        domo_inputs['DOMO_CLIENT_ID'] = clients[company]['DOMO_CLIENT_ID']
        domo_inputs['DOMO_SECRET_KEY'] = clients[company]['DOMO_SECRET_KEY']
        domo_inputs['DOMO_INSTANCE'] = clients[company]['DOMO_INSTANCE']
        domo_inputs['DOMO_DATASET_ID'] = clients[company]['DOMO_DATASET_ID']
    if bi_tool == 'mode':
        data['vessels'].update(mode)
        data['connections'].update(mode_connection)
        mode_inputs = data['vessels']['Trigger Mode Report Refresh']['source']['inputs']
        mode_inputs['MODE_TOKEN_ID'] = clients[company]['MODE_TOKEN_ID']
        mode_inputs['MODE_TOKEN_PASSWORD'] = clients[company]['MODE_TOKEN_PASSWORD']
        mode_inputs['MODE_WORKSPACE_NAME'] = clients[company]['MODE_WORKSPACE_NAME']
        mode_inputs['MODE_REPORT_ID'] = clients[company]['MODE_REPORT_ID']

    with open(f'{clients[company]["COMPANY_NAME"]}_fleet.yaml', 'w') as f:
        data = yaml.dump(data, f, sort_keys=False, default_flow_style=False)


    headers = {
        'X-Shipyard-API-Key': f'{shipyard_api_key}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    with open(f'{clients[company]["COMPANY_NAME"]}_fleet.yaml', 'rb') as f:
        api_data = f.read()

    response = requests.put(
        f'https://api.app.shipyardapp.com/orgs/{org_id}/projects/{project_id}/fleets',
        headers=headers,
        data=api_data,
    )
