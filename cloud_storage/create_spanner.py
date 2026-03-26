from google.cloud import storage, bigquery, spanner


def create_bq_dataset(dataset_id, location):
    client = bigquery.Client()
    dataset = bigquery.Dataset(f"{client.project}.{dataset_id}")
    dataset.location = location
    client.create_dataset(dataset, exists_ok=True)
    print(f"Dataset Creado: {dataset.dataset_id}")

def create_spanner(
    instance_id,
    config_id="regional-us-central1",
    display_name=None,
    processing_units=1000,
):
    client = spanner.Client()

    configuration_name = f"projects/{client.project}/instanceConfigs/{config_id}"

    instance = client.instance(
        instance_id,
        configuration_name=configuration_name,
        display_name=display_name or instance_id,
        processing_units=processing_units,
    )

    operation = instance.create()
    operation.result()
    print()



if __name__ == "__main__":
    # Parámetros
    dataset_id = "mi_dataset_test200032510"
    location = "US"

    instance_id = "mi-spanner-instance"
    config_id = "regional-us-central1"
    display_name = "Mi instancia Spanner"
    processing_units = 1000

    # Llamadas
    create_bq_dataset(dataset_id, location)
    create_spanner(instance_id, config_id, display_name)