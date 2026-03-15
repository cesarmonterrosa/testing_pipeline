import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

#pip install "apache-beam[gcp]"
def run():
    options = PipelineOptions (
        runner = "DirectRunner",
        project="gcp-testing-env2003",
        region="us-central1",
        temp_location="gs://my_maincesars-0bucket-200325/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer Archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            | "Separar Palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar Palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText("gs://my_maincesars-0bucket-200325/output/wordcount")
        )
    print("Done")
if __name__ == "__main__":
    run()  
