        regex_matches = self.regex.search(str(value))
        invalid_input = regex_matches if self.inverse_match else not regex_matches
        if invalid_input:
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (

    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError(self.message, code=self.code)
        # Check if the scheme is valid.
        scheme = value.split('://')[0].lower()
        if scheme not in self.schemes:
            raise ValidationError(self.message, code=self.code)

        # Then check full URL
        try:
                try:
                    scheme, netloc, path, query, fragment = urlsplit(value)
                except ValueError:  # for example, "Invalid IPv6 URL"
                    raise ValidationError(self.message, code=self.code)
                try:
                    netloc = punycode(netloc)  # IDN -> ACE
                except UnicodeError:  # invalid domain part
                try:
                    validate_ipv6_address(potential_ip)
                except ValidationError:
                    raise ValidationError(self.message, code=self.code)

        # The maximum length of a full host name is 253 characters per RFC 1034
        # section 3.1. It's defined to be 255 bytes or less, but this includes
        # one byte for the length of the name and one byte for the trailing dot
        # that's used to indicate absolute names in DNS.
        if len(urlsplit(value).netloc) > 253:
            raise ValidationError(self.message, code=self.code)


integer_validator = RegexValidator(

    def __call__(self, value):
        if not value or '@' not in value:
            raise ValidationError(self.message, code=self.code)

        user_part, domain_part = value.rsplit('@', 1)

        if not self.user_regex.match(user_part):
            raise ValidationError(self.message, code=self.code)

        if (domain_part not in self.domain_allowlist and
                not self.validate_domain_part(domain_part)):
            else:
                if self.validate_domain_part(domain_part):
                    return
            raise ValidationError(self.message, code=self.code)

    def validate_domain_part(self, domain_part):
        if self.domain_regex.match(domain_part):
    try:
        ipaddress.IPv4Address(value)
    except ValueError:
        raise ValidationError(_('Enter a valid IPv4 address.'), code='invalid')


def validate_ipv6_address(value):
    if not is_valid_ipv6_address(value):
        raise ValidationError(_('Enter a valid IPv6 address.'), code='invalid')


def validate_ipv46_address(value):
        try:
            validate_ipv6_address(value)
        except ValidationError:
            raise ValidationError(_('Enter a valid IPv4 or IPv6 address.'), code='invalid')


ip_address_validator_map = {
            raise ValidationError(
                self.messages['max_digits'],
                code='max_digits',
                params={'max': self.max_digits},
            )
        if self.decimal_places is not None and decimals > self.decimal_places:
            raise ValidationError(
                self.messages['max_decimal_places'],
                code='max_decimal_places',
                params={'max': self.decimal_places},
            )
        if (self.max_digits is not None and self.decimal_places is not None and
                whole_digits > (self.max_digits - self.decimal_places)):
            raise ValidationError(
                self.messages['max_whole_digits'],
                code='max_whole_digits',
                params={'max': (self.max_digits - self.decimal_places)},
            )

    def __eq__(self, other):
                code=self.code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )


    def __call__(self, value):
        if '\x00' in str(value):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (