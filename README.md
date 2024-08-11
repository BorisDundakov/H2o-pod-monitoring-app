# H2o Pod monitoring application

Monitor your pod performance in a Kubernetes cluster using the h2o-wave-app library

![Screenshot from 2023-04-06 12-39-36](https://user-images.githubusercontent.com/71731579/230340281-0d8c63a0-310e-410d-a866-6f0a3824ea69.png)


## How to run

### Prerequisites:


- minikube installed and configured
- minikube running


### Steps:


#### Clone the repo

```
git clone https://github.com/BorisDundakov/H2o-pod-monitoring-app.git
```

#### Run the deployment

```
kubectl apply -f deployment/deployment.yml
```


## References
- Kubernetes docs: https://kubernetes.io/docs/concepts/architecture/

- H2o wave library: https://wave.h2o.ai/

- H2o app reference guide: https://github.com/srini-x/wave-heroku

- H2o system monitor tutorial: https://wave.h2o.ai/docs/tutorial-monitor
