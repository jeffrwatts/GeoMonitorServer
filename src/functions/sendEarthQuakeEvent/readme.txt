Local Debug
export GOOGLE_CLOUD_PROJECT="projectId"

functions-framework --target=sendEarthQuakeEvent --debug

curl -X POST [endpoint] \
-H "Content-Type: application/json" \
-d '{"magnitude": "4.7", "depth": "20"}'


Check Function Available
gcloud functions describe 

 --gen2 --region us-central1 --format="value(serviceConfig.uri)"

Deploy
gcloud functions deploy send_earthquake_event \
    --gen2 \
    --runtime=python312 \
    --region=us-central1 \
    --source=. \
    --entry-point=sendEarthQuakeEvent \
    --trigger-http 