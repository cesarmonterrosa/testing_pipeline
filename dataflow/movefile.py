import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    options = PipelineOptions(
        runner="DataflowRunner", #antes DirectRunner | Activar API si usamos Dataflow y grant permission al service account en IAM
        project="gcp-testing-env2003",
        region="us-central1",
        temp_location="gs://my_maincesars-0bucket-200325/temp"
    )

    input_file = "gs://my_maincesars-0bucket-200325/archivo.csv"
    output_file = "gs://my_maincesars-0bucket-200325/copied_file/copied_csv"

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer CSV" >> beam.io.ReadFromText(input_file, skip_header_lines=0)
            | "Escribir CSV en bucket destino" >> beam.io.WriteToText(
                output_file,
                file_name_suffix=".csv",
                shard_name_template=""
            )
        )

    print("Done")


if __name__ == "__main__":
    run()