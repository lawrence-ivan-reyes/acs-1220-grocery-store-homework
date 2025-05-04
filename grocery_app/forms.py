from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Grocery Store Title', validators=[DataRequired(), Length(min=3, max=100)])
    address = StringField('Address', validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    title = StringField('Item Name', validators=[(DataRequired(), Length(min=2, max=100))])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('produce', 'Produce'),
        ('deli', 'Deli'),
        ('bakery', 'Bakery'),
        ('pantry', 'Pantry'),
        ('frozen', 'Frozen'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    photo_url = StringField('Item Photo', validators=URL())
    store = QuerySelectField('Store', 
                            query_factory=lambda: GroceryStore.query.all(),
                            get_label='title')
    submit = SubmitField('Submit')
