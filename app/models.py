from tortoise import fields, models
#from tortoise.models import Model

class InputContent(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    source = fields.CharField(max_length=255)
    timestamp = fields.CharField(max_length=255)  # ISO format string
    content = fields.TextField() # text original
    # les champs suivants sont calculer par utils.py et stocker
    translate_content = fields.TextField() # transcrit en anglais
    subject = fields.CharField(max_length=255, null=True)  # Subjet calculé
    sentiment = fields.FloatField(null=True)  # Sentiment calculé

    class Meta:
        table = "input_content"