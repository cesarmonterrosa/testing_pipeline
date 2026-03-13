from google.cloud import storage

#gcloud auth application-default login

def create_bucket(bucket_name, location="US-CENTRAL1", storage_class="STANDARD"):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    new_bucket = storage_client.create_bucket(bucket, location=location)
    print(f" Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}")


#define bucket name here
if __name__ == "__main__":
    create_bucket("my-test-bucket-daniel")