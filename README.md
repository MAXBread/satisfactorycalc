# Satisfactorycalc

### Git

```
git remote set-url origin https://oauth2:TOKEN@github.com/MAXBread/satisfactorycalc.git
```

### Django 
```
python manage.py collectstatic
```

#### Run in development mode
```
cd kstore
python manage.py runserver
python3 manage.py runserver 192.168.0.101:8000
```

#### Release hanging port for Linux
```
sudo fuser -k 8000/tcp
```
#### Create django application
```
django-admin startapp cart
```

#### Run test
```
cd kstore
python manage.py test
```
### Models
```shell
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py showmigrations
./manage.py squashmigrations store 0009
```


#### DB Export|Import <=> file : format json|xml|yaml
```
./manage.py dumpdata main.Fabric --indent 4 > Fabric.json
./manage.py dumpdata main.Item --indent 4 > Item.json
./manage.py dumpdata main.VariantInput --indent 4 > VariantInput.json
./manage.py dumpdata main.VariantOutput --indent 4 > VariantOutput.json
./manage.py dumpdata main.Recipe --indent 4 > Recipe.json
./manage.py dumpdata main --indent 4 > main.json

./manage.py loaddata Fabric.json
./manage.py loaddata Item.json
./manage.py loaddata VariantInput.json
./manage.py loaddata VariantOutput.json
./manage.py loaddata Recipe.json

# exmples
./manage.py dumpdata > db.json
./manage.py dumpdata store > store.json
./manage.py dumpdata store.product > product.json
./manage.py dumpdata --exclude auth.permission > db.json
./manage.py dumpdata auth.user --indent 2 > user.json
./manage.py dumpdata auth.user --indent 2 --format xml > user.xml
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

./manage.py loaddata user.json
```

#### Session parameters
```
from django.contrib.sessions.models import Session
session_k = Session.objects.get(pk='axi3op5uxkj10xe0i1lit21pyoxpz387')
session_k.get_decoded()
```

{'session_key': {}}
