clients = {
    "pizza_planet": {
    "COMPANY_NAME": "pizza_planet",
    "FIVETRAN_API_KEY": "pizza",
    "FIVETRAN_API_SECRET": "planet",
    "FIVETRAN_CONNECTOR_ID": "pizza_sync",
    "DBT_ACCOUNT_ID": "buzz",
    "DBT_API_KEY": "lightyear",
    "DBT_JOB_ID": "toinfinity",
    "TABLEAU_DATASOURCE_NAME": "forky",
    "TABLEAU_PASSWORD": "isnottrash",
    "TABLEAU_PROJECT_NAME": "toys_data",
    "TABLEAU_SERVER_URL": "https://toys.online.tableau.com/",
    "TABLEAU_SITE_ID": "toydevelopment",
    "TABLEAU_USERNAME": "andy"
},
    "dinoco": {
    "COMPANY_NAME": "dinoco",
    "FIVETRAN_API_KEY": "route",
    "FIVETRAN_API_SECRET": "sixty_six",
    "FIVETRAN_CONNECTOR_ID": "cars_sync",
    "DBT_ACCOUNT_ID": "lightning",
    "DBT_API_KEY": "mcqueen",
    "DBT_JOB_ID": "kachow",
    "TABLEAU_DATASOURCE_NAME": "piston",
    "TABLEAU_PASSWORD": "cozy_cone",
    "TABLEAU_PROJECT_NAME": "flos_cafe",
    "TABLEAU_SERVER_URL": "https://cars.online.tableau.com/",
    "TABLEAU_SITE_ID": "cardevelopment",
    "TABLEAU_USERNAME": "mater"
},
    "monsters_inc": {
    "COMPANY_NAME": "monsters_inc",
    "FIVETRAN_API_KEY": "monsters",
    "FIVETRAN_API_SECRET": "incorporated",
    "FIVETRAN_CONNECTOR_ID": "monsters_sync",
    "DBT_ACCOUNT_ID": "mike",
    "DBT_API_KEY": "sully",
    "DBT_JOB_ID": "roar",
    "TABLEAU_DATASOURCE_NAME": "wescare",
    "TABLEAU_PASSWORD": "becausewecare",
    "TABLEAU_PROJECT_NAME": "randall",
    "TABLEAU_SERVER_URL": "https://monsters.online.tableau.com/",
    "TABLEAU_SITE_ID": "monstersdevelopment",
    "TABLEAU_USERNAME": "boo"
}
}

org_id = 'YOUR_ORG_ID'
project_id = 'YOUR_PROJECT_ID'
shipyard_api_key = 'YOUR_API_KEY'
company_list = ['pizza_planet','dinoco','monsters_inc']
for company in company_list:
    with open('tutorial.yaml', 'r') as f:
        data = yaml.safe_load(f)
    fivetran_inputs = data['vessels']['Execute Fivetran Sync']['source']['inputs']
    dbt_inputs = data['vessels']['Execute dbt Cloud Job']['source']['inputs']
    tableau_inputs = data['vessels']['Trigger Tableau Datasource Refresh']['source']['inputs']
    data['name'] = f'{clients[company]["COMPANY_NAME"]} Fleet'
    fivetran_inputs['FIVETRAN_API_KEY'] = clients[company]['FIVETRAN_API_KEY']
    fivetran_inputs['FIVETRAN_API_SECRET'] = clients[company]['FIVETRAN_API_SECRET']
    fivetran_inputs['FIVETRAN_CONNECTOR_ID'] = clients[company]['FIVETRAN_CONNECTOR_ID']
    dbt_inputs['DBT_ACCOUNT_ID'] = clients[company]['DBT_ACCOUNT_ID']
    dbt_inputs['DBT_API_KEY'] = clients[company]['DBT_API_KEY']
    dbt_inputs['DBT_JOB_ID'] = clients[company]['DBT_JOB_ID']
    tableau_inputs['TABLEAU_DATASOURCE_NAME'] = clients[company]['TABLEAU_DATASOURCE_NAME']
    tableau_inputs['TABLEAU_PASSWORD'] = clients[company]['TABLEAU_PASSWORD']
    tableau_inputs['TABLEAU_PROJECT_NAME'] = clients[company]['TABLEAU_PROJECT_NAME']
    tableau_inputs['TABLEAU_SERVER_URL'] = clients[company]['TABLEAU_SERVER_URL']
    tableau_inputs['TABLEAU_SITE_ID'] = clients[company]['TABLEAU_SITE_ID']
    tableau_inputs['TABLEAU_USERNAME'] = clients[company]['TABLEAU_USERNAME']
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
