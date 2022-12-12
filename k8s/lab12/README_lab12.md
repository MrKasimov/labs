## Lab 12
`kubectl get po`
```
NAME                                               READY   STATUS    RESTARTS   AGE
devops-time-app-c955c4545-tjsrr                    1/1     Running   0          1h
devops-time-app-c955c4545-tjsrr-5c9746d475-qlllr   1/1     Running   0          26s
```
`kubectl exec devops-time-app-c955c4545-tjsrr-5c9746d475-qlllr   -- ls -l`
```
total 28
-rw-r--r-- 1 root root  615 Dec 11 20:47 DOCKER.md
-rw-r--r-- 1 root root  152 Dec 11 20:47 Dockerfile
-rw-r--r-- 1 root root  923 Dec 11 20:47 PYTHON.md
-rw-r--r-- 1 root root 2122 Dec 11 20:47 README.md
-rw-r--r-- 1 root root  469 Dec 11 20:47 main_app.py
-rw-r--r-- 1 root root  223 Dec 11 20:47 requirements.txt
drwxr-xr-x 2 root root 4096 Dec 11 20:47 tests
```
`kubectl exec devops-time-app-c955c4545-tjsrr-5c9746d475-qlllr -- cat config.json`
```yaml
    {
    "version": "1.0.0",
    "history_text": "Moscow time"
}
```