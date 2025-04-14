    <field name="pub_date" type="DateTimeField">2006-06-16T11:00:00</field>
    <field name="categories" rel="ManyToManyRel" to="serializers.category"><object pk="%(first_category_pk)s"></object><object pk="%(second_category_pk)s"></object></field>
    <field name="meta_data" rel="ManyToManyRel" to="serializers.categorymetadata"></field>
  </object>
</django-objects>"""  # NOQA
