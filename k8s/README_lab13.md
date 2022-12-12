## Lab 13
`minikube kubectl -- get pods,sts,svc,pvc `
```
NAME               READY   STATUS    RESTARTS   AGE
pod/devops-time-app-0  1/1     Running   0          3m44s
pod/devops-time-app-1   1/1     Running   0          3m33s
pod/devops-time-app-2   1/1     Running   0          3m17s
NAME                          READY   AGE
statefulset.apps/devops-time-app   3/3     3m54s
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        346d
service/devops-time-app   LoadBalancer   10.107.195.47   <pending>     80:31447/TCP   3m54s
NAME                                                   STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/persistent-volume-devops-time-app-0   Bound    pvc-892cf287-e7dd-d67e-648b-2949bf0eb777   128Mi      RWO            standard       3m54s
persistentvolumeclaim/persistent-volume-devops-time-app-1   Bound    pvc-231304c0-0001-8057-ad19-0d3ed92a6e7b   128Mi      RWO            standard       3m43s
persistentvolumeclaim/persistent-volume-devops-time-app-2   Bound    pvc-bc8f4838-b745-4519-a9b0-c697b65e1651   128Mi      RWO            standard       3m24s
```
 `minikube kubectl -- exec pod/devops-time-app-0 -- cat /home/labs_devops/k8s/lab12/files/config.json`
 ```
Accessed at: 10:24:27
Accessed at: 10:24:30
Accessed at: 10:24:31
Accessed at: 10:24:36
Accessed at: 10:24:36
 ```
`minikube kubectl -- exec pod/devops-time-app-1 -- cat /home/labs_devops/k8s/lab12/files/config.json`

  ```
Accessed at: 10:27:13
Accessed at: 10:27:15
Accessed at: 10:27:17
Accessed at: 10:27:20
Accessed at: 10:27:21
  ```
  `minikube kubectl -- exec pod/devops-time-app-2 -- cat /home/labs_devops/k8s/lab12/files/config.json`

```
Accessed at: 10:27:22
Accessed at: 10:27:24
```

In each pod we have different mounted volumes. Number of accesses depends on the load balancer



