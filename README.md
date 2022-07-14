# pulumi using gcp-python

#### Reserving the static internal ip using pulumi:


Following is the file which need to  be changed :
```
__main__.py
```
## prerequisite

```
$ curl -fsSL https://get.pulumi.com | sh
```

## Commands to apply the script:

1. First configure the gcp credentials using cli

```
$ gcloud config set project $MY_PROJECT_ID
$ gcloud config list
```

2. To set the current gcp region

```
$ pulumi config set gcp:region <region-name>
```
3. To Create a new Pulumi project

```
$ pulumi new gcp-python
```
4. Apply changes in __main__.py and activate the virtual environment

```
$ source venv/bin/activate
```

5. Create or update the resources in a stack

```
$ pulumi up --yes
```
6. Destroy all existing resources in the stack

```
$ pulumi destroy
```
