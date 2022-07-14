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

1. To set the current gcp region

```
$ pulumi config set gcp:region <region-name>
```
2. To Create a new Pulumi project

```
$ pulumi new gcp-python
```
3. Apply changes in __main__.py and activate the virtual environment

```
$ source venv/bin/activate
```

4. Create or update the resources in a stack

```
$ pulumi up --yes
```
5. Destroy all existing resources in the stack

```
$ pulumi destroy
```
