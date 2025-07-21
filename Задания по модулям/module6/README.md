```sh
kubectl get events --field-selector involvedObject.kind=HorizontalPodAutoscaler --sort-by=.lastTimestamp
LAST SEEN   TYPE     REASON              OBJECT                                 MESSAGE
10m         Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 3; reason: cpu resource utilization (percentage of request) above target
9m58s       Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 5; reason: cpu resource utilization (percentage of request) above target
6m13s       Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 6; reason: cpu resource utilization (percentage of request) above target
4m27s       Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 5; reason: All metrics below target
3m27s       Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 4; reason: All metrics below target
2m27s       Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 3; reason: All metrics below target
87s         Normal   SuccessfulRescale   horizontalpodautoscaler/test-app-hpa   New size: 2; reason: All metrics below target
```