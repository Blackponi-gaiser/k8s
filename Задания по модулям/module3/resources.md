```sh
kubectl get pods 
NAME                           READY   STATUS    RESTARTS   AGE
details-54cd5f87b4-7j2cf       1/1     Running   0          3m55s
details-54cd5f87b4-hbktm       1/1     Running   0          3m54s
nginx-7787d4775-4fmld          1/1     Running   0          3m54s
nginx-7787d4775-5lrnj          1/1     Running   0          3m55s
nginx-7787d4775-s5kzm          1/1     Running   0          3m55s
productpage-7d879f569d-46xk7   1/1     Running   0          3m55s
productpage-7d879f569d-64t5f   1/1     Running   0          3m51s
ratings-cd557f6b4-48g2k        1/1     Running   0          3m50s
ratings-cd557f6b4-fns4r        1/1     Running   0          3m54s
reviews-v1-69c9797f94-j42kz    1/1     Running   0          3m50s
reviews-v2-7b96497584-zfxs4    1/1     Running   0          3m53s
reviews-v3-64fb5df4b-65jhx     1/1     Running   0          3m53s
```

---

```sh
kubectl get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
details       ClusterIP   10.96.131.177   <none>        9080/TCP   101s
productpage   ClusterIP   10.96.232.227   <none>        9080/TCP   88s
ratings       ClusterIP   10.96.203.137   <none>        9080/TCP   82s
reviews       ClusterIP   10.96.194.33    <none>        9080/TCP   76s
```