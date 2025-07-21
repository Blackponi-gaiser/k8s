```sh
ubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
nginx-cdn-74bd85d6fc-59ckh   1/1     Running   0          69s
```

```sh
kubectl events
LAST SEEN   TYPE     REASON              OBJECT                            MESSAGE
89s         Normal   ScalingReplicaSet   Deployment/nginx-cdn              Scaled up replica set nginx-cdn-74bd85d6fc to 1
88s         Normal   SuccessfulCreate    ReplicaSet/nginx-cdn-74bd85d6fc   Created pod: nginx-cdn-74bd85d6fc-59ckh
88s         Normal   Pulled              Pod/nginx-cdn-74bd85d6fc-59ckh    Successfully pulled image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest" in 234ms (234ms including waiting). Image size: 36345415 bytes.
88s         Normal   Created             Pod/nginx-cdn-74bd85d6fc-59ckh    Created container nginx-cdn-init
88s         Normal   Scheduled           Pod/nginx-cdn-74bd85d6fc-59ckh    Successfully assigned user64r3ad1k64rk4e9r/nginx-cdn-74bd85d6fc-59ckh to cl1jepu1h9j5n3g00iug-udop
88s         Normal   Pulling             Pod/nginx-cdn-74bd85d6fc-59ckh    Pulling image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest"
87s         Normal   Started             Pod/nginx-cdn-74bd85d6fc-59ckh    Started container nginx-cdn-init
87s         Normal   Pulling             Pod/nginx-cdn-74bd85d6fc-59ckh    Pulling image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest"
87s         Normal   Pulled              Pod/nginx-cdn-74bd85d6fc-59ckh    Successfully pulled image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest" in 194ms (195ms including waiting). Image size: 36345415 bytes.
87s         Normal   Created             Pod/nginx-cdn-74bd85d6fc-59ckh    Created container nginx-cdn
87s         Normal   Started             Pod/nginx-cdn-74bd85d6fc-59ckh    Started container nginx-cdn
78s         Normal   Killing             Pod/nginx-cdn-779c7c79db-g7c7f    Stopping container nginx-cdn
78s         Normal   SuccessfulDelete    ReplicaSet/nginx-cdn-779c7c79db   Deleted pod: nginx-cdn-779c7c79db-g7c7f
78s         Normal   ScalingReplicaSet   Deployment/nginx-cdn              Scaled down replica set nginx-cdn-779c7c79db to 0 from 1
```

```sh
kubectl describe pods/nginx-cdn-74bd85d6fc-59ckh
Name:             nginx-cdn-74bd85d6fc-59ckh
Namespace:        user64r3ad1k64rk4e9r
Priority:         0
Service Account:  default
Node:             cl1jepu1h9j5n3g00iug-udop/10.129.0.12
Start Time:       Wed, 05 Mar 2025 22:21:54 +0700
Labels:           app=nginx-cdn
                  pod-template-hash=74bd85d6fc
Annotations:      kubernetes.io/limit-ranger:
                    LimitRanger plugin set: memory request for container nginx-cdn; memory limit for container nginx-cdn; memory request for init container ng...
Status:           Running
IP:               10.112.255.247
IPs:
  IP:           10.112.255.247
Controlled By:  ReplicaSet/nginx-cdn-74bd85d6fc
Init Containers:
  nginx-cdn-init:
    Container ID:  containerd://d838d0d7d3375cdbc447d70e6b3e006c5f467f6d15007435cd86489f3f1e991d
    Image:         cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest
    Image ID:      cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn@sha256:689448a093acba97d4cdf8294acc14cc48af77a0a951972339787700023819b7
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      ./download.sh
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 05 Mar 2025 22:21:54 +0700
      Finished:     Wed, 05 Mar 2025 22:21:55 +0700
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  3000Mi
    Requests:
      cpu:     200m
      memory:  200Mi
    Environment:
      URL:  https://code.s3.yandex.net/Kubernetes/barsik.jpg
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dn9rd (ro)
      /var/www/html/ from shared-data (rw)
Containers:
  nginx-cdn:
    Container ID:  containerd://bf4073d28e59064434d6ef2b08db45c8101cfd32c61853b672f243068ef1e7eb
    Image:         cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest
    Image ID:      cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn@sha256:689448a093acba97d4cdf8294acc14cc48af77a0a951972339787700023819b7
    Port:          80/TCP
    Host Port:     0/TCP
    Command:
      sh
      -c
      nginx -g 'daemon off;'
    State:          Running
      Started:      Wed, 05 Mar 2025 22:21:55 +0700
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  3000Mi
    Requests:
      cpu:        200m
      memory:     200Mi
    Liveness:     http-get http://:80/ delay=10s timeout=1s period=5s #success=1 #failure=3
    Readiness:    http-get http://:80/.done delay=5s timeout=1s period=5s #success=1 #failure=1
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dn9rd (ro)
      /var/www/html/ from shared-data (rw)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  shared-data:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     
    SizeLimit:  <unset>
  kube-api-access-dn9rd:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m25s  default-scheduler  Successfully assigned user64r3ad1k64rk4e9r/nginx-cdn-74bd85d6fc-59ckh to cl1jepu1h9j5n3g00iug-udop
  Normal  Pulling    2m25s  kubelet            Pulling image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest"
  Normal  Pulled     2m25s  kubelet            Successfully pulled image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest" in 234ms (234ms including waiting). Image size: 36345415 bytes.
  Normal  Created    2m25s  kubelet            Created container nginx-cdn-init
  Normal  Started    2m24s  kubelet            Started container nginx-cdn-init
  Normal  Pulling    2m24s  kubelet            Pulling image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest"
  Normal  Pulled     2m24s  kubelet            Successfully pulled image "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest" in 194ms (195ms including waiting). Image size: 36345415 bytes.
  Normal  Created    2m24s  kubelet            Created container nginx-cdn
  Normal  Started    2m24s  kubelet            Started container nginx-cdn
```
```json
kubectl get po nginx-cdn-74bd85d6fc-59ckh -o json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "annotations": {
            "kubernetes.io/limit-ranger": "LimitRanger plugin set: memory request for container nginx-cdn; memory limit for container nginx-cdn; memory request for init container nginx-cdn-init; memory limit for init container nginx-cdn-init"
        },
        "creationTimestamp": "2025-03-05T15:21:53Z",
        "generateName": "nginx-cdn-74bd85d6fc-",
        "labels": {
            "app": "nginx-cdn",
            "pod-template-hash": "74bd85d6fc"
        },
        "name": "nginx-cdn-74bd85d6fc-59ckh",
        "namespace": "user64r3ad1k64rk4e9r",
        "ownerReferences": [
            {
                "apiVersion": "apps/v1",
                "blockOwnerDeletion": true,
                "controller": true,
                "kind": "ReplicaSet",
                "name": "nginx-cdn-74bd85d6fc",
                "uid": "f4121ae0-28bb-47e6-985a-a572cf3839b5"
            }
        ],
        "resourceVersion": "103839880",
        "uid": "a7422b8d-5f07-431a-a5eb-e651f112f716"
    },
    "spec": {
        "containers": [
            {
                "command": [
                    "sh",
                    "-c",
                    "nginx -g 'daemon off;'"
                ],
                "image": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest",
                "imagePullPolicy": "Always",
                "livenessProbe": {
                    "failureThreshold": 3,
                    "httpGet": {
                        "path": "/",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "initialDelaySeconds": 10,
                    "periodSeconds": 5,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "name": "nginx-cdn",
                "ports": [
                    {
                        "containerPort": 80,
                        "protocol": "TCP"
                    }
                ],
                "readinessProbe": {
                    "failureThreshold": 1,
                    "httpGet": {
                        "path": "/.done",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "initialDelaySeconds": 5,
                    "periodSeconds": 5,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "resources": {
                    "limits": {
                        "cpu": "2",
                        "memory": "3000Mi"
                    },
                    "requests": {
                        "cpu": "200m",
                        "memory": "200Mi"
                    }
                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/www/html/",
                        "name": "shared-data"
                    },
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-dn9rd",
                        "readOnly": true
                    }
                ]
            }
        ],
        "dnsPolicy": "ClusterFirst",
        "enableServiceLinks": true,
        "initContainers": [
            {
                "command": [
                    "sh",
                    "-c",
                    "./download.sh"
                ],
                "env": [
                    {
                        "name": "URL",
                        "value": "https://code.s3.yandex.net/Kubernetes/barsik.jpg"
                    }
                ],
                "image": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest",
                "imagePullPolicy": "Always",
                "name": "nginx-cdn-init",
                "resources": {
                    "limits": {
                        "cpu": "2",
                        "memory": "3000Mi"
                    },
                    "requests": {
                        "cpu": "200m",
                        "memory": "200Mi"
                    }
                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/www/html/",
                        "name": "shared-data"
                    },
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-dn9rd",
                        "readOnly": true
                    }
                ]
            }
        ],
        "nodeName": "cl1jepu1h9j5n3g00iug-udop",
        "preemptionPolicy": "PreemptLowerPriority",
        "priority": 0,
        "restartPolicy": "Always",
        "schedulerName": "default-scheduler",
        "securityContext": {},
        "serviceAccount": "default",
        "serviceAccountName": "default",
        "terminationGracePeriodSeconds": 30,
        "tolerations": [
            {
                "effect": "NoExecute",
                "key": "node.kubernetes.io/not-ready",
                "operator": "Exists",
                "tolerationSeconds": 300
            },
            {
                "effect": "NoExecute",
                "key": "node.kubernetes.io/unreachable",
                "operator": "Exists",
                "tolerationSeconds": 300
            }
        ],
        "volumes": [
            {
                "emptyDir": {},
                "name": "shared-data"
            },
            {
                "name": "kube-api-access-dn9rd",
                "projected": {
                    "defaultMode": 420,
                    "sources": [
                        {
                            "serviceAccountToken": {
                                "expirationSeconds": 3607,
                                "path": "token"
                            }
                        },
                        {
                            "configMap": {
                                "items": [
                                    {
                                        "key": "ca.crt",
                                        "path": "ca.crt"
                                    }
                                ],
                                "name": "kube-root-ca.crt"
                            }
                        },
                        {
                            "downwardAPI": {
                                "items": [
                                    {
                                        "fieldRef": {
                                            "apiVersion": "v1",
                                            "fieldPath": "metadata.namespace"
                                        },
                                        "path": "namespace"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    },
    "status": {
        "conditions": [
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2025-03-05T15:21:55Z",
                "status": "True",
                "type": "PodReadyToStartContainers"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2025-03-05T15:21:55Z",
                "status": "True",
                "type": "Initialized"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2025-03-05T15:22:04Z",
                "status": "True",
                "type": "Ready"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2025-03-05T15:22:04Z",
                "status": "True",
                "type": "ContainersReady"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2025-03-05T15:21:54Z",
                "status": "True",
                "type": "PodScheduled"
            }
        ],
        "containerStatuses": [
            {
                "containerID": "containerd://bf4073d28e59064434d6ef2b08db45c8101cfd32c61853b672f243068ef1e7eb",
                "image": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest",
                "imageID": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn@sha256:689448a093acba97d4cdf8294acc14cc48af77a0a951972339787700023819b7",
                "lastState": {},
                "name": "nginx-cdn",
                "ready": true,
                "restartCount": 0,
                "started": true,
                "state": {
                    "running": {
                        "startedAt": "2025-03-05T15:21:55Z"
                    }
                }
            }
        ],
        "hostIP": "10.129.0.12",
        "hostIPs": [
            {
                "ip": "10.129.0.12"
            }
        ],
        "initContainerStatuses": [
            {
                "containerID": "containerd://d838d0d7d3375cdbc447d70e6b3e006c5f467f6d15007435cd86489f3f1e991d",
                "image": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn:latest",
                "imageID": "cr.yandex/crpcqt038mmskd2ime3g/nginx_cdn@sha256:689448a093acba97d4cdf8294acc14cc48af77a0a951972339787700023819b7",
                "lastState": {},
                "name": "nginx-cdn-init",
                "ready": true,
                "restartCount": 0,
                "started": false,
                "state": {
                    "terminated": {
                        "containerID": "containerd://d838d0d7d3375cdbc447d70e6b3e006c5f467f6d15007435cd86489f3f1e991d",
                        "exitCode": 0,
                        "finishedAt": "2025-03-05T15:21:55Z",
                        "reason": "Completed",
                        "startedAt": "2025-03-05T15:21:54Z"
                    }
                }
            }
        ],
        "phase": "Running",
        "podIP": "10.112.255.247",
        "podIPs": [
            {
                "ip": "10.112.255.247"
            }
        ],
        "qosClass": "Burstable",
        "startTime": "2025-03-05T15:21:54Z"
    }
}
```