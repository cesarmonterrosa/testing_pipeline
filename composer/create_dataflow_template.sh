python movefile.py \
    --runner DataflowRunner \
    --project gcp-testing-env2003 \
    --region us-central1 \
    --staging_location gs://my_maincesars-0bucket-200325/staging \
    --temp_location gs://my_maincesars-0bucket-200325/temp \
    --template_location gs://my_maincesars-0bucket-200325/templates/movefile