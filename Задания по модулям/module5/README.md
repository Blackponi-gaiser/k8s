```sh
helm list
NAME    NAMESPACE               REVISION        UPDATED                                 STATUS          CHART           APP VERSION
podinfo user64r3ad1k64rk4e9r    4               2025-03-17 20:08:06.278044875 +0700 +07 deployed        podinfo-1.0.0   6.6.3   
```

```sh
helm get values podinfo
USER-SUPPLIED VALUES:
config:
  enabled: false
```