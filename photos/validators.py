from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self,file_size,message=None):
        self.file_size=file_size
        self.message=message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self,value):
        if not value:
            self._message = f'The image can not be more than {self.file_size}MB'
        else:
            self._message = value


    def __call__(self,image):
        if image.size > self.file_size * 1024 * 1024:
            raise ValidationError(message=self.message)

@deconstructible
class MinimumLengthValidator:

    def __init__(self,min_len,message=None):
        self.min_len = min_len
        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self,value):
        if not value:
            self._message = f'The text must be at least {self.min_len} symbols long!'
        else:
            self._message = value

    def __call__(self,text):
        if len(text) < self.min_len:
            raise ValidationError(message=self.message)


