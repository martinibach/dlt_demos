import os
import dlt
import requests

API_BASE = os.environ.get("ACTIVE_CAMPAIGN_BASE_URL")
API_KEY = os.environ.get("ACTIVE_CAMPAIGN_API_KEY")

headers = {"Api-Token": API_KEY}

@dlt.resource(write_disposition="replace")
def contacts(limit: int = 100):
    offset = 0
    while True:
        params = {"limit": limit, "offset": offset}
        resp = requests.get(f"{API_BASE}/api/3/contacts", params=params, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("contacts") or data.get("data") or []
        if not items:
            break
        for contact in items:
            yield contact
        offset += limit

@dlt.source
def activecampaign_source():
    yield contacts()


def run_pipeline() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="activecampaign_pipeline",
        destination="postgres",
        dataset_name="activecampaign_data",
        full_refresh=True,
    )
    load_info = pipeline.run(activecampaign_source())
    print(load_info)


if __name__ == "__main__":
    run_pipeline()
