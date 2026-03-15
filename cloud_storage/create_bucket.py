from google.cloud import storage

#gcloud auth application-default login

def create_bucket(bucket_name, project_id, location="US-CENTRAL1", storage_class="STANDARD"):
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    new_bucket = storage_client.create_bucket(bucket, location=location)
    print(f" Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}")


#define bucket name here
if __name__ == "__main__":
    create_bucket(bucket_name="my_maincesars-0bucket-200325", project_id="gcp-testing-env2003") #CHANGE PROJECT ID