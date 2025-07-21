# Stateful- и Stateless-приложения в Kubernetes

## 1. Введение
Kubernetes поддерживает различные виды приложений: веб-сервисы, базы данных, одиночные задания, демоны и службы. Для выбора подходящей абстракции важно понимать разницу между **stateful** и **stateless** приложениями.

## 2. Понятие состояния (state)
Состояние (**state**) – это данные, необходимые для работы приложения и взаимодействия с клиентами. Это могут быть:
- Данные пользовательской сессии
- История запросов
- Информация об авторизации

## 3. Stateless-приложения
**Stateless-приложения** не сохраняют состояние между запросами. Каждое взаимодействие с клиентом обрабатывается независимо.

### 🔹 Примеры:
- Веб-сервер, обрабатывающий HTTP-запросы
- API Gateway
- Load Balancer

### ✅ Преимущества:
- Легко масштабируются (можно запустить несколько копий)
- Меньше требований к хранилищу
- Упрощённое развертывание и восстановление

### ❌ Недостатки:
- Клиенту нужно каждый раз передавать всю необходимую информацию
- Может потребоваться дополнительный внешний сервис для хранения данных (например, Redis)

### 🍪 Пример с печеньем:
Вы покупаете круассаны в супермаркете с кассами самообслуживания. Кассиру всё равно, что вы покупали раньше — каждый раз он обслуживает вас заново.

---

## 4. Stateful-приложения
**Stateful-приложения** хранят состояние и используют его при обработке запросов.

### 🔹 Примеры:
- Базы данных (PostgreSQL, MongoDB)
- Чаты и мессенджеры
- Игровые серверы

### ✅ Преимущества:
- Позволяют сохранять пользовательские данные
- Упрощают взаимодействие клиента с сервером

### ❌ Недостатки:
- Сложнее масштабировать и балансировать нагрузку
- Требуют постоянного хранилища данных (Persistent Volume в Kubernetes)

### 🥐 Пример с круассанами:
Вы приходите в небольшую пекарню, где продавец помнит, какие круассаны вы любите, и предлагает их вам без напоминания.

---

## 5. Stateful vs Stateless в Kubernetes
| Характеристика       | Stateless             | Stateful              |
|----------------------|----------------------|----------------------|
| Хранение данных     | Не хранит состояние  | Хранит состояние    |
| Масштабируемость    | Легко масштабируется | Сложнее масштабировать |
| Завиcимость от диска | Нет                  | Требуется хранилище  |
| Примеры             | Веб-серверы, API      | Базы данных, чаты    |

# Deployment и запуск stateless-приложений в Kubernetes

## 1. Введение
В Kubernetes используется декларативный подход: мы описываем желаемое состояние объектов, а кластер поддерживает его. Для этого применяются YAML-манифесты.

## 2. Основные поля YAML-манифеста
Каждый объект Kubernetes включает:
- **apiVersion** — версия API Kubernetes.
- **kind** — тип объекта (Pod, Deployment и т. д.).
- **metadata** — метаинформация (имя, метки).
- **spec** — желаемое состояние объекта.

## 3. Пример Pod в Kubernetes
Запуск Pod с Nginx с помощью `kubectl`:
```bash
kubectl run nginx --image=nginx:1.24

```yaml
apiVersion: v1 # версия API
kind: Pod # тип объекта — под
metadata: # метаданные, идентифицирующие объект
  name: nginx # имя пода
  namespace: default # namespace, в котором создан под
spec: # описание состояния объекта
  containers:  # список контейнеров в поде
  - image: nginx:1.24 # образ, на базе которого запущен контейнер
    name: nginx # имя контейнера
```
# Запуск stateless-приложений в Kubernetes: Pod, ReplicaSet, Deployment

## 1. Введение  
Kubernetes предоставляет различные абстракции для запуска приложений. В этом уроке рассматриваются **Pod, ReplicaSet и Deployment**, а также их применение для запуска **Traefik** — прокси-сервера и балансировщика нагрузки.

## 2. Запуск Pod  
Самый простой способ развернуть приложение — использовать объект **Pod**.  
Однако Pod не поддерживает масштабирование и обновление, поэтому на практике его редко используют напрямую.  

### Пример манифеста Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: traefik
spec:
  containers:
    - name: traefik
      image: traefik:v2.10
      ports:
        - containerPort: 80
```
# Kubernetes: ReplicaSet и Deployment
**ReplicaSet** — это объект Kubernetes, который позволяет запускать заданное количество реплик приложения и поддерживать их работоспособность.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: traefik
  labels:
    name: traefik
spec:
  replicas: 3
  selector:
    matchLabels:
      name: traefik
  template:
    metadata:
      labels:
        name: traefik
    spec:
      containers:
      - image: traefik:v2.10.1
        name: traefik
        args:
          - '--api.dashboard=true'
          - '--api.insecure=true'
          - '--accesslog=true'
        ports:
        - containerPort: 8080
          name: http
```

### Основные параметры:
- `spec.replicas` — количество реплик.
- `spec.selector` — селектор для управления подами.
- `spec.template` — шаблон пода.

### Команды управления ReplicaSet:
```sh
kubectl apply -f replicaset.yaml  # Создание ReplicaSet
kubectl get rs  # Получение информации о ReplicaSet
```

**Deployment** — это объект Kubernetes, который позволяет управлять обновлениями приложения без потери доступности.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: traefik
  labels:
    name: traefik
spec:
  replicas: 3
  selector:
    matchLabels:
      name: traefik
  template:
    metadata:
      labels:
        name: traefik
    spec:
      containers:
      - image: traefik:v2.10.1
        name: traefik
        args:
          - '--api.dashboard=true'
          - '--api.insecure=true'
          - '--accesslog=true'
        ports:
        - containerPort: 8080
          name: http
```

### Команды управления Deployment:
```sh
kubectl apply -f deployment.yaml  # Создание Deployment
kubectl get deployments  # Получение списка Deployment
```
### Проверка созданных объектов:
```sh
kubectl get rs  # Список ReplicaSet
kubectl get pods  # Список подов
```

## Откат изменений

Deployment сохраняет предыдущие версии, что позволяет делать откат:
```sh
kubectl rollout undo deployment traefik  # Откат к предыдущей версии
```
Можно откатиться к конкретной версии:
```sh
kubectl rollout history deployment/traefik  # Получение списка версий
kubectl rollout undo deployment/traefik --to-revision=<номер_версии>
```

## Стратегии обновления

### Доступные стратегии обновления:
- `Recreate` — удаляет старые поды перед созданием новых.
- `RollingUpdate` (по умолчанию) — плавное обновление без потери доступности.

### Опции стратегии RollingUpdate:
- `maxUnavailable` — количество подов, которое может быть недоступно во время обновления.
- `maxSurge` — количество подов, которое можно создать сверх желаемого.

Пример настройки стратегии:
```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```
## Получение детальной информации
Команда `kubectl describe` позволяет получить полную информацию о ресурсах Kubernetes:
```sh
kubectl describe deployment traefik
```
- **ReplicaSet** поддерживает нужное количество подов, но не управляет обновлениями.
- **Deployment** обеспечивает управление версиями и обновления без потери доступности.
- Возможность **отката** и **управления стратегиями обновления** делает Deployment удобным инструментом для развёртывания stateless-приложений.
# Kubernetes: PersistentVolume (PV) и PersistentVolumeClaim (PVC)

## Введение

В Kubernetes постоянные тома (Persistent Volumes, PV) и запросы на их выделение (Persistent Volume Claims, PVC) используются для хранения данных, которые сохраняются даже при удалении или перезапуске подов.

## Основные понятия

- **PersistentVolume (PV)** — ресурс на уровне кластера, представляющий собой выделенное хранилище данных.
- **PersistentVolumeClaim (PVC)** — запрос от пользователя на использование определённого объёма хранилища с заданными параметрами.
- **StorageClass** — механизм, определяющий тип и характеристики хранилища (например, NFS, Ceph, AWS EBS).

## Создание PersistentVolume (PV)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: "/mnt/data"
```

### Основные параметры PV:
- **capacity.storage** — размер хранилища.
- **accessModes**:
  - `ReadWriteOnce` (RWO) — доступ с одного узла.
  - `ReadOnlyMany` (ROX) — доступ только на чтение с нескольких узлов.
  - `ReadWriteMany` (RWX) — доступ на запись с нескольких узлов.
- **persistentVolumeReclaimPolicy**:
  - `Retain` — сохраняет данные после удаления PVC.
  - `Delete` — автоматически удаляет PV после удаления PVC.
  - `Recycle` — очищает данные перед повторным использованием.
- **storageClassName** — определяет тип хранилища.
- **hostPath** — используется для локального хранения на узлах кластера (не рекомендуется для продакшена).

## Создание PersistentVolumeClaim (PVC)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: example-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

### Основные параметры PVC:
- **accessModes** — те же режимы доступа, что и у PV.
- **resources.requests.storage** — запрашиваемый размер хранилища.
- **storageClassName** — соответствует `storageClassName` PV, если используется динамическое выделение.

## Использование PVC в поде

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-using-pvc
spec:
  containers:
    - name: app-container
      image: nginx
      volumeMounts:
        - mountPath: "/data"
          name: storage
  volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: example-pvc
```

## Динамическое выделение хранилища

Если в кластере настроен `StorageClass`, PVC автоматически создаёт PV при запросе.

### Пример StorageClass:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
```

### PVC, использующий StorageClass:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: fast-storage
```
# Kubernetes: DaemonSet и управление демонами

## Введение

**DaemonSet** — это объект Kubernetes, предназначенный для управления демонами, которые должны выполняться на каждом узле кластера или на определённой группе узлов.

## Отличия DaemonSet от Deployment и StatefulSet
- **Не управляет количеством реплик** — вместо этого гарантирует запуск пода на всех или определённых узлах.
- **Используется для служебных задач**, таких как сбор логов, мониторинг, сетевые прокси.
- **Поддерживает выбор узлов через nodeSelector**, позволяя запускать демоны только на нужных узлах.

## Пример манифеста DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: podinfo
spec:
  selector:
    matchLabels:
      app: podinfo
  template:
    metadata:
      labels:
        app: podinfo
    spec:
      containers:
        - name: podinfo
          image: ghcr.io/stefanprodan/podinfo:6.6.3
          command:
            - ./podinfo
            - '--port=9000'
          ports:
            - name: http
              containerPort: 9000
              protocol: TCP
```

### Основные параметры:
- **Нет `spec.replicas`** — под создаётся на всех узлах автоматически.
- **`spec.selector`** — определяет, какие поды принадлежат DaemonSet.
- **`spec.template`** — шаблон для создаваемых подов.

## Размещение подов на определённых узлах

Можно указать, что DaemonSet должен запускаться только на узлах с определённой меткой:

```yaml
spec:
  template:
    spec:
      nodeSelector:
        gpu-type: nvidia
```

### Проверка запущенных подов
```sh
kubectl get pod -o wide
```

## Обновление DaemonSet

### RollingUpdate (по умолчанию)
```yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 2
```
- Поды обновляются последовательно.
- Можно задать `maxUnavailable` (количество недоступных подов в процессе обновления).

### OnDelete
```yaml
spec:
  updateStrategy:
    type: OnDelete
```
- Новые поды создаются только после ручного удаления старых.

## Применение манифеста
```sh
kubectl apply -f daemonset.yaml
```

## Удаление DaemonSet
```sh
kubectl delete daemonset podinfo
```

## Ключевые мысли о DaemonSet
- Позволяет управлять приложениями-демонами на всех узлах кластера или на конкретной группе узлов.
- Как правило, используется администраторами кластера для служебных задач и обеспечения работоспособности кластера.
- Гарантирует работу копии приложений на каждом узле желаемой группы, даже в случае ошибок или изменения группы узлов.
- Является рекомендуемым инструментом для запуска демон-процессов в Kubernetes и решает проблемы, характерные для других способов развёртывания.

## Заключение
- **DaemonSet** используется для запуска демонов на всех или определённых узлах кластера.
- **Поддерживает nodeSelector** для фильтрации узлов.
- **Обновления возможны через RollingUpdate или OnDelete**.
- **Применяется для мониторинга, логирования, сетевого проксирования** и других задач.

# Kubernetes: Job и CronJob

Для управления процессами, которые должны завершиться после выполнения задачи, в **Kubernetes** используются абстракции:
- **Job** — выполняет разовые задачи.
- **CronJob** — выполняет задачи по расписанию.

Они полезны для следующих задач:
- Создание бэкапов баз данных.
- Обработка медиафайлов.
- Расчёт статистики.
- Инференс моделей машинного обучения и т. д.

---
## Job

**Job** создаёт один или несколько подов для выполнения разовой задачи. Когда контейнер в поде завершает выполнение, **Job** получает статус `Complete`. Если контейнер завершился с ошибкой, **Job** перезапускает его.
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: alpine-job
spec:
  completions: 3
  parallelism: 2
  ttlSecondsAfterFinished: 100
  backoffLimit: 2
  activeDeadlineSeconds: 60
  template:
    metadata:
      name: alpine-sleep
    spec:
      restartPolicy: OnFailure
      containers:
        - image: alpine
          name: alpine-sleep
          command:
            - 'sh'
            - '-c'
            - 'sleep 5'
---
### Основные параметры:
- completions — количество подов, успешное выполнение которых завершает Job.
- parallelism — количество одновременно работающих подов.
- ttlSecondsAfterFinished — время в секундах, через которое Job удаляется после завершения.
- backoffLimit — число попыток перезапуска при ошибке (по умолчанию: 6).
- activeDeadlineSeconds — максимальное время выполнения Job.
- restartPolicy — политика рестарта контейнера (OnFailure или Never).

### Расписание (schedule)
Формат **cron** (`* * * * *`):
- `* * * * *` — каждую минуту.
- `0 9,18 * * *` — каждый день в 9:00 и 18:00.
- `*/15 * 1-10 * *` — каждые 15 минут с 1-го по 10-е число месяца.

### Политика выполнения (concurrencyPolicy)
- `Allow` (по умолчанию) — допускает параллельные запуски.
- `Forbid` — не запускает новую задачу, если предыдущая ещё выполняется.
- `Replace` — заменяет запущенную задачу новой.

### Управление историей задач
- `successfulJobsHistoryLimit` — хранение завершённых задач.
- `failedJobsHistoryLimit` — хранение неуспешных задач.

### Дополнительные настройки
- `suspend` — приостанавливает выполнение **CronJob** (`false` по умолчанию).

---

## Рекомендации по использованию Job и CronJob

✅ **Ограничивайте время выполнения задач**: используйте `activeDeadlineSeconds`.  
✅ **Контролируйте количество перезапусков**: настройте `backoffLimit`.  
✅ **Ограничивайте количество одновременно работающих Job**: параметр `parallelism`.  
✅ **Храните только нужную историю заданий**: параметры `successfulJobsHistoryLimit` и `failedJobsHistoryLimit`.  
✅ **Автоматически удаляйте завершённые задачи**: настройка `ttlSecondsAfterFinished`.  
✅ **Не перегружайте кластер частыми CronJob**: следите за нагрузкой на API-сервер.

---

## Возможные проблемы

⚠ **Ошибка в имени образа** → под зависает в `Pending`, что может привести к превышению лимита подов.  
⚠ **Слишком много одновременно работающих Job** → нехватка ресурсов в кластере.  
⚠ **Частый запуск CronJob** → высокая нагрузка на API-сервер и хранилище Kubernetes.  

