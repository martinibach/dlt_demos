# ActiveCampaign to Postgres with dlt

This example shows how to load data from the ActiveCampaign REST API into a PostgreSQL database using [dlt](https://github.com/dlt-hub/dlt).

## Prerequisites

- Python 3.10+
- Access to an ActiveCampaign account
- A Postgres database

Create a `.dlt/secrets.toml` file or export the following environment variables:

```
ACTIVE_CAMPAIGN_BASE_URL=<https://YOUR_ACCOUNT.api-us1.com>
ACTIVE_CAMPAIGN_API_KEY=<your api key>
```

The Postgres connection settings can also be provided via `secrets.toml`.

Install the requirements and run the pipeline:

```bash
pip install -r requirements.txt
python activecampaign_pipeline.py
```

The pipeline will fetch contacts from ActiveCampaign and store them in a table named `contacts` under the dataset `activecampaign_data`.
