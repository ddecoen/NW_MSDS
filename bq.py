def run_():
    import os
    import pandas as pd

    from google.cloud import bigquery
    from google.oauth2 import service_account

    key_path = "your_key_path_here" #enter your json key file here

    credentials =   service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    client = bigquery.Client(credentials=credentials)

    query = """
    SELECT Name, Pos, sum(predicted_Total_OPS) as predicted_ops
    FROM `finalprojectgcp-384519.dandecoentest2.predicted_ops_video`
    WHERE Age >= 23
    GROUP BY Name, Pos
    ORDER BY predicted_ops DESC
    LIMIT 20
    """
    query_job = client.query(query)
    
    counts = []
    names = [] 
    for row in query_job:
        names.append(row["Name"])
        counts.append(row["predicted_ops"])
    
    # put names and name counts in a dataframe and sort       #highest ops, to simulate operating on data with a model
    
    results = {'Names': names, 'Predicted OPS': counts}
    df = pd.DataFrame.from_dict(results) # convert to DataFrame
    df = df.sort_values(by=['Predicted OPS'], ascending=False) # sort by OPS
    df = df.to_dict(orient='list') # convert to dictionary format 
    
    return df
