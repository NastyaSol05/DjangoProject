from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):

    INCORRECT_NAME = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        name_check = self.cleaned_data["name"]
        if name_check.lower() in self.INCORRECT_NAME:
            raise ValidationError("Имя продукта не должно содержать неправильные слова.")
        return name_check

    def clean_description(self):
        description_check = self.cleaned_data["description"]
        for i in self.INCORRECT_NAME:
            if i in description_check:
                raise ValidationError("Описание продукта не должно содержать неправильные слова.")
        return description_check

    def clean_price(self):
        price_check = self.cleaned_data["price"]
        if price_check < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price_check
