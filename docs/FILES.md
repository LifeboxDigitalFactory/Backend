# Archivos locales en Django

Este proyecto guarda archivos en disco local (`MEDIA_ROOT`), sin Azure ni S3.

## Configuración (ya incluida)

En `academy/settings.py`:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

En desarrollo, `academy/urls.py` sirve los archivos cuando `DEBUG=True`.

La carpeta `media/` está en `.gitignore`.

## FileField (ejemplo)

```python
def activity_upload_path(instance, filename):
    return f"activities/{instance.course_id}/{filename}"

class Activity(models.Model):
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=20)  # READING | VIDEO | AUDIO
    file = models.FileField(upload_to=activity_upload_path)
```

## Upload con DRF

Usa `multipart/form-data` y `MultiPartParser`:

```python
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.generics import CreateAPIView

class ActivityCreateView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    # ...
```

En la respuesta de lectura, expón una URL absoluta:

```python
def get_file_url(self, obj):
    request = self.context.get("request")
    if obj.file and request:
        return request.build_absolute_uri(obj.file.url)
    return None
```

## Validación sugerida

Valida por `content_type` y/o extensión, y un tamaño máximo según el tipo
(PDF/audio ~10–20 MB, video ~50 MB).

## Frontend (FormData)

```typescript
const formData = new FormData()
formData.append('name', name)
formData.append('activity_type', activityType)
formData.append('file', file)
// No setear Content-Type manualmente
await $fetch(url, { method: 'POST', body: formData })
```

## Visualización

- PDF / lectura: `<iframe :src="fileUrl">`
- Video: `<video controls :src="fileUrl">`
- Audio: `<audio controls :src="fileUrl">`
