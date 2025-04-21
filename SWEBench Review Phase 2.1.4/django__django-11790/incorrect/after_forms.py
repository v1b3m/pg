@@ -191,7 +191,16 @@ class AuthenticationForm(forms.Form):

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        # Set the field's max_length and update widget attrs accordingly
        max_length_val = self.username_field.max_length or 254
        self.fields['username'].max_length = max_length_val
        # Update the widget's attrs 'maxlength' to reflect the field's max_length
        try:
            if not self.fields['username'].widget.is_hidden:
                self.fields['username'].widget.attrs['maxlength'] = str(max_length_val)
        except AttributeError:
            # In case widget has no attrs dict, ignore
            pass
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)
