gcloud container clusters get-credentials load-test --region us-central1

export LOCUST_IMAGE_NAME=locust-tasks
export LOCUST_IMAGE_TAG=latest
export REGION=us-central1
export PROJECT=bridgesplit-backend
export AR_REPO=dist-lt-repo
gcloud builds submit \
    --tag ${REGION}-docker.pkg.dev/${PROJECT}/${AR_REPO}/${LOCUST_IMAGE_NAME}:${LOCUST_IMAGE_TAG} \
    docker-image

kubectl get services - to get external ip [will be mp http://34.27.89.169:8089/]
kubectl rollout restart deployment locust-worker - to redeploy a newly updated container
kubectl scale deployment/locust-worker --replicas=20 -- to increase the number of VMs [please make 1 before ending your load test]